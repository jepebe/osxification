import ctypes
import ctypes.util
from unittest import TestCase
from osxification.foundation import NSObject, NSStringEncoding, NSLog, NSString
from osxification.objc import autoreleasepool, objc


class nsstring(NSObject):
    _objc_class_ = "NSString"

    def __init__(self, content):
        identifier = nsstring._init(self.alloc(), content, NSStringEncoding.NSUTF8StringEncoding)
        super(nsstring, self).__init__(identifier)

    def __str__(self):
        return self._asCString(NSStringEncoding.NSUTF8StringEncoding)

    def __int__(self):
        return self._intValue()

    def __float__(self):
        return self._floatValue()



nsstring._init = nsstring.bindMethodToClass("initWithCString:encoding:")
nsstring._asCString = nsstring.bindMethodToClass("cStringUsingEncoding:", returns=str)
nsstring._intValue = nsstring.bindMethodToClass("integerValue", returns=int)
nsstring._floatValue = nsstring.bindMethodToClass("doubleValue", returns=float)


class ObjCClassTest(TestCase):
    def setUp(self):
        super(ObjCClassTest, self).setUp()
        self.FOUNDATION = ctypes.cdll.LoadLibrary(ctypes.util.find_library("foundation"))

    def test_class_creation(self):
        test = nsstring("objc_class test_string")
        NSLog(test)

        self.assertEqual(str(test), "objc_class test_string")

    def test_conversion(self):
        num = nsstring("3.45")

        self.assertEqual(float(num), 3.45)
        self.assertEqual(int(num), 3)

    def test_pool(self):
        with autoreleasepool():
            text = nsstring("auto_release_pool_text_string")
            NSLog(text)

    def test_kind_of_class(self):
        from osxification.foundation import NSString
        string_1 = NSString("NSString")
        string_2 = nsstring("nsstring")
        self.assertTrue(string_2.isKindOfClass(string_1))

    def test_ns_log(self):
        NSLog("Auto Convert of str to NSString")

    def test_description(self):
        pointer = objc.invoke(NSObject.alloc(), "init")
        nsobject = NSObject(pointer)

        description = nsobject.description()
        self.assertTrue(str(description).startswith("<NSObject:"))


