import ctypes
import logging
from types import MethodType
from osxification.objc import objc, Identifier, Class, ProtocolType


class _MetaNSObjectType(type):


    @staticmethod
    def __new__(cls, name, bases, namespace, **options):
        return super().__new__(cls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, objc_class=None, **options):
        super(_MetaNSObjectType, cls).__init__(name, bases, namespace)
        class_def = cls.resolveClass(name, bases, objc_class)

        cls._objc_class_name_ = class_def.getName()

        # if "_protocols_" in dct:
        #     pass




    def resolveClass(cls, name, bases, objc_class):
        """ :rtype: Class """
        class_def = objc.getClass(name)

        if class_def is None and objc_class is not None:
            logging.warning("Using manual class override for class: %s (objc_class=\"%s\")", cls.__name__, objc_class)
            class_def = objc.getClass(objc_class)

            if class_def is None:
                raise TypeError("Objective C class with name: %s does not exist!" % objc_class)

        if class_def is None:
            super_class = objc.getClass("NSObject")
            for base in bases:
                if hasattr(base, "getClass"):
                    try:
                        test_super_class = base.getClass()
                        assert isinstance(test_super_class, Class)
                        super_class = test_super_class
                        break
                    except (AttributeError, AssertionError):
                        pass

            logging.warning("Class '%s' is not registered. Auto registering with super class: %s" , name, super_class)
            new_class = objc.allocateClassPair(super_class, name)
            objc.registerClassPair(new_class)
            class_def = new_class
        return class_def




class NSObject(object, metaclass=_MetaNSObjectType):

    def __init__(self, identifier):
        self._identifier = identifier

    def __eq__(self, other):
        if isinstance(other, NSObject):
            return self._identifier == other._identifier

        if isinstance(other, Identifier):
            return self._identifier == other

        return False

    def description(self):
        from .ns_string import NSString
        return NSString._as_return_type_(self._description())

    def conformsToProtocol(self, protocol):
        return bool(objc.invoke(self, "conformsToProtocol:", protocol))

    @property
    def _as_parameter_(self):
        """
        :rtype: Identifier
        """
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
        """ :rtype: cls """
        if identifier is None or identifier.value is None:
            return None

        logging.debug("Class %s used as return type", cls.__name__)

        new_obj = cls.__new__(cls)
        NSObject.__init__(new_obj, identifier)
        return new_obj

    @classmethod
    def alloc(cls):
        """ :rtype: cls """
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
        """ :rtype: Identifier """
        return objc.invoke(cls.alloc(), "init")

    def __del__(self):
        # print("[%s.__del__] Autoreleasing: %s" % (self.__class__.__name__, self._identifier.value))
        objc.autorelease(self._identifier)

    @classmethod
    def getClass(cls):
        """:rtype: Class """
        class_def = objc.getClass(cls.__name__)

        if class_def is None and hasattr(cls, "_objc_class_name_"):
            logging.debug("Using ObjectiveC class alias: %s for class: %s", cls._objc_class_name_, cls.__name__)
            class_def = objc.getClass(cls._objc_class_name_)

        return class_def

    def isKindOfClass(self, class_instance):
        """ :rtype: bool """
        assert isinstance(class_instance, (Class, NSObject))
        if isinstance(class_instance, NSObject):
            class_instance = class_instance.getClass()
        return self._isKindOfClass(class_instance)

    @classmethod
    def bindMethodToClass(cls, selector, parameters=None, returns=None):
        return objc.createFunction(selector, argument_types=parameters, return_type=returns)

    @classmethod
    def invokeClassMethod(cls, selector):
        return objc.invoke(cls.getClass(), selector)



NSObject._isKindOfClass = NSObject.bindMethodToClass("isKindOfClass:", returns=bool)
NSObject._description = NSObject.bindMethodToClass("description")


