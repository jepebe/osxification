import contextlib
import ctypes
from types import MethodType
from osxification.objc import ObjCFunction, Class, Selector, Identifier

@contextlib.contextmanager
def autoreleasepool():
    identifier = objc._autoreleasePoolPush()
    yield
    objc._autoreleasePoolPop(identifier)



class objc(object):
    @staticmethod
    def getClass(class_name):
        """
        :rtype: Class
        """
        assert isinstance(class_name, (str, unicode))
        return objc._getClass(class_name)

    @staticmethod
    def msgSend(instance, selector, *args):
        """
        :rtype: Identifier
        """
        return objc._msgSend(instance, selector, *args)

    @staticmethod
    def msgSendFloatReturnType(instance, selector, *args):
        """
        :rtype: float
        """
        return objc._msgSend_fpret(instance, selector, *args)

    @staticmethod
    def invoke(instance, selector, *args):
        """
        :rtype: Identifier
        """
        if isinstance(selector, (str, unicode)):
            selector = Selector.registerName(selector)

        return objc.msgSend(instance, selector, *args)

    @classmethod
    def alloc(cls, class_identifier):
        if not isinstance(class_identifier, Class):
            class_identifier = cls.getClass(class_identifier)
        return cls.invoke(class_identifier, "alloc")

    @classmethod
    def autorelease(cls, pointer):
        cls.invoke(pointer, "autorelease")

    @classmethod
    def createFunction(cls, selector, argument_types=None, return_type=None):
        def func(self, *args):
            _selector = selector
            if isinstance(_selector, (str, unicode)):
                _selector = Selector.registerName(_selector)

            if argument_types is not None:
                new_args = []
                for index, arg in enumerate(args):
                    argument_type = argument_types[index]
                    if hasattr(argument_type, "from_param"):
                        new_args.append(argument_type.from_param(arg))

                args = new_args

            if return_type is float:
                result = cls.msgSendFloatReturnType(self, _selector, *args)
            else:
                result = cls.msgSend(self, _selector, *args)

            if return_type is float:
                result = return_type(result)
            elif return_type is str:
                result = ctypes.c_char_p(result.value).value
            elif hasattr(return_type, "_as_return_type_"):
                result = return_type._as_return_type_(result)
            elif return_type is not None:
                result = return_type(result.value)

            return result
        return func

    @classmethod
    def bindMethodToClass(cls, receiver_class, selector):
        func = cls.createFunction(selector)
        bound_method = MethodType(func, None, receiver_class)
        return bound_method

    @classmethod
    def allocateClassPair(cls, super_class, name):
        """
        :rtype: Class
        """
        return objc._allocateClassPair(super_class, name, 0)

    @classmethod
    def registerClassPair(cls, class_instance):
        objc._registerClassPair(class_instance)

    @classmethod
    def disposeClassPair(cls, class_instance):
        objc._disposeClassPair(class_instance)


    @classmethod
    def getClassName(cls, identifier):
        """
        :rtype: str
        """
        return objc._getClassName(identifier)



objc._getClass = ObjCFunction("Class objc_getClass(char*)")
objc._getClassName = ObjCFunction("char* object_getClassName(id)")

objc._msgSend = ObjCFunction("id objc_msgSend(id, SEL)")
objc._msgSend_fpret = ObjCFunction("double objc_msgSend_fpret(id, SEL)")

objc._autoreleasePoolPush = ObjCFunction("void* objc_autoreleasePoolPush()")
objc._autoreleasePoolPop = ObjCFunction("void objc_autoreleasePoolPop(void*)")

objc._allocateClassPair = ObjCFunction("Class objc_allocateClassPair(Class, char*, size_t)")
objc._registerClassPair = ObjCFunction("void objc_registerClassPair(Class)")
objc._disposeClassPair = ObjCFunction("void objc_disposeClassPair(Class)")
