import ctypes
from osxification.c import Prototype
from osxification.objc import ObjCFunction


class Selector(ctypes.c_void_p):
    @staticmethod
    def checkSelector(selector):
        if isinstance(selector, str):
            selector = Selector.registerName(selector)
        assert isinstance(selector, Selector)
        return selector

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
        assert isinstance(name, str)
        return Selector._registerName(name.encode())


Prototype.registerType("SEL", Selector)

Selector._getName = ObjCFunction("char* sel_getName(SEL)")
Selector._registerName = ObjCFunction("SEL sel_registerName(char*)")