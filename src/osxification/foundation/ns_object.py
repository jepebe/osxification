import ctypes
from functools import wraps
from types import MethodType
from osxification.objc import objc, Identifier, Class


class NSObject(object):

    def __init__(self, identifier):
        self._identifier = identifier

    def __eq__(self, other):
        if isinstance(other, NSObject):
            return self._identifier == other._identifier
        return False

    def description(self):
        from .ns_string import NSString
        return NSString._as_return_type_(self._description())

    @property
    def _as_parameter_(self):
        return self._identifier

    @classmethod
    def from_param(cls, instance):
        if instance is None:
            return ctypes.c_void_p()

        if isinstance(instance, cls):
            return instance._identifier

        # Checking if class is compatible
        if isinstance(instance, NSObject) and instance.isKindOfClass(cls.getClass()):
            return instance._identifier

        raise ValueError("Instance must be compatible with type: %s!" % cls.__name__)

    @classmethod
    def _as_return_type_(cls, identifier):
        if identifier is None or identifier.value is None:
            return None

        new_obj = cls.__new__(cls)
        NSObject.__init__(new_obj, identifier)
        return new_obj

    @classmethod
    def alloc(cls):
        class_def = cls.getClass()

        if class_def is not None:
            instance = objc.alloc(class_def)
            new_obj = cls.__new__(cls)
            NSObject.__init__(new_obj, instance)
            return new_obj
        else:
            return None

    @classmethod
    def init(cls, identifier):
        return objc.invoke(identifier, "init")

    @classmethod
    def new(cls):
        return objc.invoke(cls.alloc(), "init")

    def __del__(self):
        # print("[%s.__del__] Autoreleasing: %s" % (self.__class__.__name__, self._identifier.value))
        objc.autorelease(self._identifier)

    @classmethod
    def getClass(cls):
        """
        :rtype: Class
        """
        class_def = objc.getClass(cls.__name__)

        if class_def is None and hasattr(cls, "_objc_class_"):
            # print("Reverting to fallback for: %s" % cls.__name__)
            class_def = objc.getClass(cls._objc_class_)

        return class_def

    def isKindOfClass(self, class_instance):
        assert isinstance(class_instance, (Class, NSObject))
        if isinstance(class_instance, NSObject):
            class_instance = class_instance.getClass()
        return self._isKindOfClass(class_instance)

    @classmethod
    def bindMethodToClass(cls, selector, parameters=None, returns=None):
        func = objc.createFunction(selector, argument_types=parameters, return_type=returns)
        bound_method = MethodType(func, None, cls)
        return bound_method


NSObject._isKindOfClass = NSObject.bindMethodToClass("isKindOfClass:", returns=bool)
NSObject._description = NSObject.bindMethodToClass("description")


