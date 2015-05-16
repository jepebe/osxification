from osxification.c import Enum


class CFNumberType(Enum):
    kCFNumberSInt8Type = None
    kCFNumberSInt16Type = None
    kCFNumberSInt32Type = None
    kCFNumberSInt64Type = None
    kCFNumberFloat32Type = None
    kCFNumberFloat64Type = None
    kCFNumberCharType = None
    kCFNumberShortType = None
    kCFNumberIntType = None
    kCFNumberLongType = None
    kCFNumberLongLongType = None
    kCFNumberFloatType = None
    kCFNumberDoubleType = None
    kCFNumberCFIndexType = None
    kCFNumberNSIntegerType = None
    kCFNumberCGFloatType = None
    kCFNumberMaxType = None

CFNumberType.addEnum("kCFNumberSInt8Type", 1)
CFNumberType.addEnum("kCFNumberSInt16Type", 2)
CFNumberType.addEnum("kCFNumberSInt32Type", 3)
CFNumberType.addEnum("kCFNumberSInt64Type", 4)
CFNumberType.addEnum("kCFNumberFloat32Type", 5)
CFNumberType.addEnum("kCFNumberFloat64Type", 6)
CFNumberType.addEnum("kCFNumberCharType", 7)
CFNumberType.addEnum("kCFNumberShortType", 8)
CFNumberType.addEnum("kCFNumberIntType", 9)
CFNumberType.addEnum("kCFNumberLongType", 10)
CFNumberType.addEnum("kCFNumberLongLongType", 11)
CFNumberType.addEnum("kCFNumberFloatType", 12)
CFNumberType.addEnum("kCFNumberDoubleType", 13)
CFNumberType.addEnum("kCFNumberCFIndexType", 14)
CFNumberType.addEnum("kCFNumberNSIntegerType", 15)
CFNumberType.addEnum("kCFNumberCGFloatType", 16)
CFNumberType.addEnum("kCFNumberMaxType", 16)

CFNumberType.registerEnum("CFNumberType")


