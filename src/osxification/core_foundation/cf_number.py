import ctypes
from osxification.core_foundation import CFType, Prototype, CFFunction
from osxification.core_foundation.cf_number_type import CFNumberType


class CFNumber(CFType):
    type_id_function = CFFunction("CFTypeID CFNumberGetTypeID()")

    def __init__(self, value):
        assert value is not None

        if isinstance(value, int):
            value = ctypes.c_int32(value)
            pointer = CFNumber._Create(None, CFNumberType.kCFNumberSInt32Type, ctypes.pointer(value))
        elif isinstance(value, long):
            value = ctypes.c_int64(value)
            pointer = CFNumber._Create(None, CFNumberType.kCFNumberSInt64Type, ctypes.pointer(value))
        elif isinstance(value, float):
            value = ctypes.c_double(value)
            pointer = CFNumber._Create(None, CFNumberType.kCFNumberFloat64Type, ctypes.pointer(value))
        else:
            raise TypeError("Type must be on of int, long or float, got: %s" % value.__class__.__name__)

        super(CFNumber, self).__init__(pointer)

    def getType(self):
        """ :rtype: CFNumberType """
        return CFNumber._GetType(self)

    def isFloatType(self):
        """ :rtype: bool """
        return CFNumber._IsFloatType(self)

    def getValue(self):
        if self.isFloatType():
            value = ctypes.pointer(ctypes.c_double(0))
            success = CFNumber._GetValue(self, CFNumberType.kCFNumberFloat64Type, value)
        else:
            value = ctypes.pointer(ctypes.c_int64(0))
            success = CFNumber._GetValue(self, CFNumberType.kCFNumberSInt64Type, value)

        if not success:
            raise ValueError("Error converting value!")

        return value.contents.value


    def __int__(self):
        return int(self.getValue())

    def __long__(self):
        return long(self.getValue())

    def __float__(self):
        return float(self.getValue())

    def __str__(self):
        return str(self.getValue())

    def __repr__(self):
        return str(self)





Prototype.registerObjectType("CFNumber", CFNumber)

CFNumber._Create = CFFunction("void* CFNumberCreate(void*, CFNumberType, void*)")
CFNumber._GetType = CFFunction("CFNumberType CFNumberGetType(CFNumber)")
CFNumber._IsFloatType = CFFunction("bool CFNumberIsFloatType(CFNumber)")
CFNumber._GetValue = CFFunction("bool CFNumberGetValue(CFNumber, CFNumberType, void*)")

