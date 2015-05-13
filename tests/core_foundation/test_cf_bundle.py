import ctypes
from unittest import TestCase
from osxification.core_foundation import CFString, CFBundle
from osxification.foundation import NSString


class CFBundleTest(TestCase):

    def test_main(self):
        # bundle = CFBundle()
        # bundle = CFBundle("com.apple.CoreFoundation")
        bundle = CFBundle("com.apple.Foundation")
        name = CFString("NSUserNotificationDefaultSoundName")
        result = bundle.pointerForName(name)
        #print(NSString._as_return_type_(result[0]))
        # result_string = CFString.getCStringFromPointer(result)

        # print(result_string)

    def test_core_foundation(self):
        bundle = CFBundle("com.apple.CoreFoundation")
        name = CFString("kCFRunLoopCommonModes")
        result = bundle.pointerForName(name)
        self.assertEqual("kCFRunLoopCommonModes", CFString.convertPointerToType(result[0]))
