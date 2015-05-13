import ctypes
from osxification.c import Prototype
from osxification.objc import ObjCFunction


class Selector(ctypes.c_void_p):

    def getName(self):
        """
        :rtype: str
        """
        return Selector._getName(self)

    @staticmethod
    def registerName(name):
        """
        :rtype: Selector
        """
        assert isinstance(name, (str, unicode))
        return Selector._registerName(name)


Prototype.registerType("SEL", Selector)

Selector._getName = ObjCFunction("char* sel_getName(SEL)")
Selector._registerName = ObjCFunction("SEL sel_registerName(char*)")