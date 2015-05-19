import ctypes
import logging
from osxification.core_foundation import CFFunction, Prototype

FORMAT = '%(levelname)-8s [%(filename)s %(funcName)s %(lineno)s]: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

Prototype.registerType("CFIndex", ctypes.c_long)
Prototype.registerType("CFTypeID", ctypes.c_ulong)

class MetaCFType(type):
    REGISTERED_TYPES = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)

        cls.TYPE_ID = None

        if "type_id_function" in dct:
            if dct["type_id_function"] is not None:
                cls.TYPE_ID = dct["type_id_function"]()
                MetaCFType.REGISTERED_TYPES[cls.TYPE_ID] = cls
        else:
            print("[%s] Warning: Class does not provide a type_id_function!" % cls.__name__)


class CFType(object, metaclass=MetaCFType):
    type_id_function = None

    def __init__(self, c_pointer):
        self.__c_pointer = c_pointer

    @classmethod
    def from_param(cls, c_class_object):
        if c_class_object is not None and not isinstance(c_class_object, CFType):
            raise ValueError("c_class_object must be a CFType instance!")

        if c_class_object is None:
            return ctypes.c_void_p()
        else:
            # logging.debug("Used through from_param: %s", cls.__name__)
            return ctypes.c_void_p(c_class_object.__c_pointer)

    @property
    def _as_parameter_(self):
        """
        :rtype: (str, int)
        """
        # logging.debug("Used directly through as_parameter: %s", self.__class__.__name__)
        return ctypes.c_void_p(self.__c_pointer)

    @classmethod
    def createCReference(cls, pointer):
        if pointer is not None:
            new_obj = cls.__new__(cls)
            CFType.__init__(new_obj, c_pointer=pointer)
            new_obj.retain()
            return new_obj
        else:
            return None

    @classmethod
    def createPythonObject(cls, pointer):
        if pointer is not None:
            new_obj = cls.__new__(cls)
            CFType.__init__(new_obj, c_pointer=pointer)
            return new_obj
        else:
            return None

    def getTypeID(self):
        """
        :rtype: int
        """
        return CFType._get_type_id(self.__c_pointer)

    @classmethod
    def getTypeIDForClass(cls):
        return cls.TYPE_ID

    @classmethod
    def getTypeIDFromPointer(cls, c_pointer):
        """
        :type c_pointer: c_void_p
        :rtype: int
        """
        return CFType._get_type_id(c_pointer)

    def show(self):
        CFType._show(self.__c_pointer)

    def getRetainCount(self):
        return CFType._get_retain_count(self.__c_pointer)

    @classmethod
    def getTypeDescription(cls, cf_type_id):
        """
        :type cf_type_id: CFTypeID
        :rtype: osxification.core_foundation.CFString
        """
        from . import CFString
        ptr = CFType._copy_type_id_description(cf_type_id)
        return CFString.createPythonObject(ptr)

    @staticmethod
    def convertPointerToType(c_pointer, reference=True):
        type_id = CFType.getTypeIDFromPointer(c_pointer)
        if type_id in MetaCFType.REGISTERED_TYPES:
            cftype = MetaCFType.REGISTERED_TYPES[type_id]
            if reference:
                return cftype.createCReference(c_pointer)
            else:
                return cftype.createPythonObject(c_pointer)

        logging.warning("Unable to convert pointer with type id: %d [%s]", type_id, CFType.getTypeDescription(type_id))

        return c_pointer

    @staticmethod
    def convertToPointer(instance):
        if isinstance(instance, CFType):
            return instance.from_param(instance)
        elif isinstance(instance, str):
            for cftype in MetaCFType.REGISTERED_TYPES.values():
                try:
                    return cftype.from_param(instance)
                except ValueError:
                    pass

        raise UserWarning("Unable to convert type: %s" % instance)


    def retain(self):
        if hasattr(self, "_CFType__c_pointer") and self.__c_pointer is not None:
            # print("Retaining %d" % self.__c_pointer)
            return CFType._retain(self.__c_pointer)

    def __release(self):
        if hasattr(self, "_CFType__c_pointer") and self.__c_pointer is not None:
            # print("Releasing %d" % self.__c_pointer)
            # self.show()
            # print("Retain count for %d: %d" % (self.__c_pointer, self.getRetainCount()))
            CFType._release(self.__c_pointer)


    def __del__(self):
        self.__release()


CFType._retain = CFFunction("c_void_p CFRetain(c_void_p)")
CFType._release = CFFunction("void CFRelease(c_void_p)")
CFType._show = CFFunction("void CFShow(c_void_p)")
CFType._get_type_id = CFFunction("CFTypeID CFGetTypeID(c_void_p)")
CFType._get_retain_count = CFFunction("CFIndex CFGetRetainCount(c_void_p)")
CFType._copy_type_id_description = CFFunction("c_void_p CFCopyTypeIDDescription(CFTypeID)")