import ctypes
from osxification.c import Prototype
from osxification.core_foundation import CFType, CFArray, CFString, CFRunLoop
from osxification.system_configuration import SCFunction


class SCDynamicStore(CFType):
    type_id_function = SCFunction("CFTypeID SCDynamicStoreGetTypeID()")

    def __init__(self, name, callback=None):
        c_ptr = SCDynamicStore._Create(None, name, callback, None)
        super(SCDynamicStore, self).__init__(c_ptr)
        self.__callback_cache = callback

    def keys(self, pattern=".*"):
        return SCDynamicStore._CopyKeyList(self, pattern)

    def setNotificationKeys(self, keys=None, pattern=None):
        return SCDynamicStore._SetNotificationKeys(self, keys, pattern)

    def createRunLoopSource(self, order=0):
        return SCDynamicStore._CreateRunLoopSource(None, self, order)

    def notifiedKeys(self):
        return SCDynamicStore._CopyNotifiedKeys(self)

    def addTemporaryValue(self, key, value):
        return SCDynamicStore._AddTemporaryValue(self, key, value)

    def getValue(self, key):
        return CFType.convertPointerToType(SCDynamicStore._CopyValue(self, key), reference=False)



Prototype.registerObjectType("SCDynamicStore", SCDynamicStore)

SCDynamicStoreCallBack = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
Prototype.registerType("SCDynamicStoreCallBack", SCDynamicStoreCallBack)

SCDynamicStore._Create = SCFunction("void* SCDynamicStoreCreate(void*, CFString, SCDynamicStoreCallBack, void*)")
SCDynamicStore._CopyKeyList = SCFunction("CFArrayObj SCDynamicStoreCopyKeyList(SCDynamicStore, CFString)")
SCDynamicStore._SetNotificationKeys = SCFunction("bool SCDynamicStoreSetNotificationKeys(SCDynamicStore, CFArray, CFArray)")
SCDynamicStore._CreateRunLoopSource = SCFunction("CFRunLoopSourceObj SCDynamicStoreCreateRunLoopSource(void*, SCDynamicStore, CFIndex)")
SCDynamicStore._CopyNotifiedKeys = SCFunction("CFArrayObj SCDynamicStoreCopyNotifiedKeys(SCDynamicStore)")
SCDynamicStore._AddTemporaryValue = SCFunction("bool SCDynamicStoreAddTemporaryValue(SCDynamicStore, CFString, CFPropertyList)")
SCDynamicStore._CopyValue = SCFunction("void* SCDynamicStoreCopyValue(SCDynamicStore, CFString)")
