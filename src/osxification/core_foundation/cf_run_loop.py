import ctypes
from osxification.c import Prototype
from osxification.core_foundation import CFType, CFFunction


class CFRunLoop(CFType):
    type_id_function = CFFunction("CFTypeID CFRunLoopGetTypeID()")

    def __init__(self):
        raise NotImplementedError("CFRunLoop can not be instantiated directly!")

    def addSource(self, source, mode="kCFRunLoopCommonModes"):
        CFRunLoop._AddSource(self, source, mode)

    @classmethod
    def run(cls):
        CFRunLoop._Run()

    @classmethod
    def runInMode(cls, mode="kCFRunLoopDefaultMode", seconds=0, return_after_source_handled=False):
        return CFRunLoop._RunInMode(mode, seconds, return_after_source_handled)


    def stop(self):
        CFRunLoop._Stop(self)

    @classmethod
    def getCurrentRunLoop(cls):
        return CFRunLoop._GetCurrent()

    @classmethod
    def getMainRunLoop(cls):
        return CFRunLoop._GetMain()


Prototype.registerObjectType("CFRunLoop", CFRunLoop)
Prototype.registerType("CFRunLoopSource", ctypes.c_void_p)
Prototype.registerType("CFRunLoopSourceRef", ctypes.c_void_p)
Prototype.registerType("CFRunLoopSourceObj", ctypes.c_void_p)


CFRunLoop._GetCurrent = CFFunction("CFRunLoopRef CFRunLoopGetCurrent()")
CFRunLoop._GetMain = CFFunction("CFRunLoopRef CFRunLoopGetMain()")
CFRunLoop._AddSource = CFFunction("void CFRunLoopAddSource(CFRunLoop, CFRunLoopSource, CFString)")
CFRunLoop._Run = CFFunction("void CFRunLoopRun()")
CFRunLoop._RunInMode = CFFunction("c_int32 CFRunLoopRunInMode(CFString, double, bool)")
CFRunLoop._Stop = CFFunction("void CFRunLoopStop(CFRunLoop)")