from unittest import TestCase
import ctypes
import ctypes.util
from osxification.core_foundation import Prototype, CFString


class PrototypeTest(TestCase):

    def test_prototype(self):
        self.assertEqual(Prototype.parseType("int"), ctypes.c_int)

        Prototype.registerType("test_name", ctypes.c_uint32)
        self.assertEqual(Prototype.parseType("test_name"), ctypes.c_uint32)

        CORE_FOUNDATION_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library('CoreFoundation'))

        function = Prototype.prototype("double CFAbsoluteTimeGetCurrent()", CORE_FOUNDATION_LIB)


    def test_cfstring(self):
        name = CFString("cfstring")
        self.assertEqual(len(name), 8)

        for index, char in enumerate("cfstring"):
            self.assertEqual(char, name[index])

        self.assertEqual(str(name), "cfstring")

        CORE_FOUNDATION_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library('CoreFoundation'))

        compare = Prototype.prototype("int CFStringCompare(CFString, CFString, int)", CORE_FOUNDATION_LIB)

        self.assertEqual(compare("string", "string", 0), 0)
        self.assertEqual(compare("a", "b", 0), -1)
        self.assertEqual(compare("b", "a", 0), 1)



    def test_ref(self):
        CORE_FOUNDATION_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library('CoreFoundation'))

        get_name = Prototype.prototype("CFStringRef CFStringGetNameOfEncoding(int)", CORE_FOUNDATION_LIB)

        cfstring = get_name(0x08000100)

        for index, char in enumerate("Unicode (UTF-8)"):
            self.assertEqual(char, cfstring[index])


