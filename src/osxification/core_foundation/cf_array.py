import ctypes
from osxification.core_foundation import CFType, Prototype, CFFunction


class CFArray(CFType):
    type_id_function = CFFunction("CFTypeID CFArrayGetTypeID()")

    def __init__(self, values=None):
        count = 0
        if values is not None:
            count = len(values)

        c_array = None

        if values is not None:
            values = [CFType.convertToPointer(item) for item in values]
            c_array = (ctypes.c_void_p * count)(*values)

        c_ptr = CFArray._create(None, c_array, count, None)
        super(CFArray, self).__init__(c_ptr)

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError("Index out of bounds: 0 <= %d < %d" % (index, len(self)))

        pointer = CFArray._get_value_at(self, index)

        value = CFType.convertPointerToType(pointer)
        return value

    def __len__(self):
        return CFArray._length(self)


Prototype.registerObjectType("CFArray", CFArray)

CFArray._create = CFFunction("c_void_p CFArrayCreate(c_void_p, c_void_p, CFIndex, c_void_p)")
CFArray._length = CFFunction("CFIndex CFArrayGetCount(CFArray)")
CFArray._get_value_at = CFFunction("c_void_p CFArrayGetValueAtIndex(CFArray, CFIndex)")