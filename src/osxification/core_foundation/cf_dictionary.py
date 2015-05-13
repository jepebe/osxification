import ctypes
from osxification.core_foundation import CFType, Prototype, CFFunction


class CFDictionary(CFType):
    type_id_function = CFFunction("CFTypeID CFDictionaryGetTypeID()")

    def keys(self):
        count = len(self)
        keys = (ctypes.c_void_p * count)()
        CFDictionary._GetKeysAndValues(self, keys, None)
        result = []
        for key in keys:
            result.append(CFType.convertPointerToType(key))
        return result

    def __len__(self):
        return CFDictionary._GetCount(self)

    def __contains__(self, item):
        return CFDictionary._ContainsKey(self, CFType.convertToPointer(item))

    def __getitem__(self, item):
        pointer = CFDictionary._GetValue(self, CFType.convertToPointer(item))
        return CFType.convertPointerToType(pointer)

Prototype.registerObjectType("CFDictionary", CFDictionary)

CFDictionary._GetCount = CFFunction("CFIndex CFDictionaryGetCount(CFDictionary)")
CFDictionary._ContainsKey = CFFunction("bool CFDictionaryContainsKey(CFDictionary, void*)")
CFDictionary._GetKeysAndValues = CFFunction("void CFDictionaryGetKeysAndValues(CFDictionary, void**, void**)")
CFDictionary._GetValue = CFFunction("void* CFDictionaryGetValue(CFDictionary, void*)")
