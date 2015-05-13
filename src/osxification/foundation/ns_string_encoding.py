from osxification.c import Enum


class NSStringEncoding(Enum):
    NSASCIIStringEncoding = None
    NSNEXTSTEPStringEncoding = None
    NSJapaneseEUCStringEncoding = None
    NSUTF8StringEncoding = None
    NSISOLatin1StringEncoding = None
    NSSymbolStringEncoding = None
    NSNonLossyASCIIStringEncoding = None
    NSShiftJISStringEncoding = None
    NSISOLatin2StringEncoding = None
    NSUnicodeStringEncoding = None
    NSWindowsCP1251StringEncoding = None
    NSWindowsCP1252StringEncoding = None
    NSWindowsCP1253StringEncoding = None
    NSWindowsCP1254StringEncoding = None
    NSWindowsCP1250StringEncoding = None
    NSISO2022JPStringEncoding = None
    NSMacOSRomanStringEncoding = None
    NSUTF16StringEncoding = None
    NSUTF16BigEndianStringEncoding = None
    NSUTF16LittleEndianStringEncoding = None
    NSUTF32StringEncoding = None
    NSUTF32BigEndianStringEncoding = None
    NSUTF32LittleEndianStringEncoding = None
    NSProprietaryStringEncoding = None


NSStringEncoding.addEnum("NSASCIIStringEncoding", 1)
NSStringEncoding.addEnum("NSNEXTSTEPStringEncoding", 2)
NSStringEncoding.addEnum("NSJapaneseEUCStringEncoding", 3)
NSStringEncoding.addEnum("NSUTF8StringEncoding", 4)
NSStringEncoding.addEnum("NSISOLatin1StringEncoding", 5)
NSStringEncoding.addEnum("NSSymbolStringEncoding", 6)
NSStringEncoding.addEnum("NSNonLossyASCIIStringEncoding", 7)
NSStringEncoding.addEnum("NSShiftJISStringEncoding", 8)
NSStringEncoding.addEnum("NSISOLatin2StringEncoding", 9)
NSStringEncoding.addEnum("NSUnicodeStringEncoding", 10)
NSStringEncoding.addEnum("NSWindowsCP1251StringEncoding", 11)
NSStringEncoding.addEnum("NSWindowsCP1252StringEncoding", 12)
NSStringEncoding.addEnum("NSWindowsCP1253StringEncoding", 13)
NSStringEncoding.addEnum("NSWindowsCP1254StringEncoding", 14)
NSStringEncoding.addEnum("NSWindowsCP1250StringEncoding", 15)
NSStringEncoding.addEnum("NSISO2022JPStringEncoding", 21)
NSStringEncoding.addEnum("NSMacOSRomanStringEncoding", 30)
NSStringEncoding.addEnum("NSUTF16StringEncoding", 10) # NSUnicodeStringEncoding
NSStringEncoding.addEnum("NSUTF16BigEndianStringEncoding", 0x90000100)
NSStringEncoding.addEnum("NSUTF16LittleEndianStringEncoding", 0x94000100)
NSStringEncoding.addEnum("NSUTF32StringEncoding", 0x8c000100)
NSStringEncoding.addEnum("NSUTF32BigEndianStringEncoding", 0x98000100)
NSStringEncoding.addEnum("NSUTF32LittleEndianStringEncoding", 0x9c000100)
NSStringEncoding.addEnum("NSProprietaryStringEncoding", 65536)

NSStringEncoding.registerEnum("NSStringEncoding")


