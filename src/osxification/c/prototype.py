import ctypes
import re
import sys
import inspect

class UTF8String(object):
    @classmethod
    def from_param(cls, value):
        if isinstance(value, bytes):
            return value
        elif isinstance(value, ctypes.Array):
            return value
        else:
            return value.encode('UTF-8')

    @staticmethod
    def _asReturnType(value):
        if value is None or value == 0:
            return None
        return str(ctypes.c_char_p(value).value, encoding="UTF-8")

class PrototypeError(Exception):
    pass


class Prototype(object):
    PROTOTYPE_PATTERN = re.compile("(?P<return>[a-zA-Z][a-zA-Z0-9_*]*) +(?P<function>[a-zA-Z]\w*) *[(](?P<arguments>[a-zA-Z0-9_*, ]*)[)]")

    REGISTERED_TYPES = {
        "void":     None,
        "void*":    ctypes.c_void_p,
        "void**":   ctypes.POINTER(ctypes.c_void_p),
        "int":      ctypes.c_int,
        "int*":     ctypes.POINTER(ctypes.c_int),
        "uint":     ctypes.c_uint,
        "uint*":    ctypes.POINTER(ctypes.c_uint),
        "size_t":   ctypes.c_size_t,
        "size_t*":  ctypes.POINTER(ctypes.c_size_t),
        "bool":     ctypes.c_bool,
        "bool*":    ctypes.POINTER(ctypes.c_bool),
        "long":     ctypes.c_long,
        "long*":    ctypes.POINTER(ctypes.c_long),
        "char":     ctypes.c_char,
        "char*":    UTF8String,
        # "char**":   ctypes.POINTER(UTF8String),
        "wchar":    ctypes.c_wchar,
        "wchar*":   ctypes.c_wchar_p,
        "wchar**":  ctypes.POINTER(ctypes.c_wchar_p),
        "float":    ctypes.c_float,
        "float*":   ctypes.POINTER(ctypes.c_float),
        "double":   ctypes.c_double,
        "double*":  ctypes.POINTER(ctypes.c_double),
    }

    @classmethod
    def registerType(cls, type_name, value):
        """Register a type against a legal ctypes type or a callable (or class)"""
        cls.REGISTERED_TYPES[type_name] = value

    @classmethod
    def registerObjectType(cls, type_name, cftype):
        """Register a type against a legal ctypes type or a callable (or class)"""
        cls.REGISTERED_TYPES[type_name] = cftype
        cls.REGISTERED_TYPES["%sRef" % type_name] = cftype.createCReference
        cls.REGISTERED_TYPES["%sObj" % type_name] = cftype.createPythonObject


    @classmethod
    def parseType(cls, type_name):
        """Convert a prototype definition type from string to a registered ctypes compatible type."""
        type_name = type_name.strip()

        if type_name in cls.REGISTERED_TYPES:
            return cls.REGISTERED_TYPES[type_name]
        else:
            return getattr(ctypes, type_name)

    @classmethod
    def prototype(cls, prototype, lib):
        """
        Defines the return type and arguments for a C-function

        prototype expects a string formatted like this:

            "type functionName(type, ... ,type)"

        where type is a type available to ctypes
        Some type are automatically converted:
            int  -> c_int
            long -> c_long
            char -> c_char_p
            bool -> c_int
            void -> None
            double -> c_double
            float  -> c_float

        There are also pointer versions of these:
            long* -> POINTER(c_long)
            bool* -> POINTER(c_int)
            double* -> POINTER(c_double)
            char* -> c_char_p
            ...

        In addition, user register types are recognized and any type registered as a reference
        to BaseCClass createCReference and createPythonObject are treated as pointers and converted automatically.
        """

        match = re.match(cls.PROTOTYPE_PATTERN, prototype)
        if not match:
            raise PrototypeError("Illegal prototype definition: %s\n" % prototype)
        else:
            restype = match.groupdict()["return"]
            function_name = match.groupdict()["function"]
            arguments = match.groupdict()["arguments"].split(",")

            try:
                func = getattr(lib, function_name)
            except AttributeError:
                raise PrototypeError("Can not find function: %s in library: %s" % (function_name, lib))

            return_type = cls.parseType(restype)

            # if inspect.isclass(return_type) and issubclass(return_type, BaseCClass):
            #     sys.stderr.write("BaseCClass can not be used as a return type in prototype definition: %s\n" % prototype)
            #     sys.stderr.write("  Correct return type may be: %s_ref or %s_obj" % (restype, restype))
            #     return None

            func.restype = return_type

            if hasattr(return_type, "__call__"):
                if hasattr(return_type, "__self__"):
                    func.restype = ctypes.c_void_p

                    def returnFunction(result, func, arguments):
                        return return_type(result)

                    func.errcheck = returnFunction

            if hasattr(return_type, "_asReturnType"):
                func.restype = ctypes.c_void_p
                def returnFunction(result, func, arguments):
                    return return_type._asReturnType(result)

                func.errcheck = returnFunction

            if len(arguments) == 1 and arguments[0].strip() == "":
                func.argtypes = []
            else:
                argtypes = [cls.parseType(arg) for arg in arguments]
                if len(argtypes) == 1 and argtypes[0] is None:
                    argtypes = []
                func.argtypes = argtypes

            return func

    @classmethod
    def printRegisteredTypes(cls):
        for ctype in cls.REGISTERED_TYPES.keys():
            print("%16s -> %s" % (ctype, cls.REGISTERED_TYPES[ctype]))

