import ctypes
from osxification.core_foundation import CFFunction, CFString


class CFBundle(object):

    def __init__(self, identifier=None):
        if identifier is None:
            self._pointer = CFBundle._GetMainBundle()
        else:
            self._pointer = CFBundle._GetBundleWithIdentifier(identifier)


    def pointerForName(self, name):
        return CFBundle._GetDataPointerForName(ctypes.c_void_p(self._pointer), name)



CFBundle._GetMainBundle = CFFunction("void* CFBundleGetMainBundle()")
CFBundle._GetBundleWithIdentifier = CFFunction("void* CFBundleGetBundleWithIdentifier(CFString)")
CFBundle._GetDataPointerForName = CFFunction("void** CFBundleGetDataPointerForName(void*, CFString)")

