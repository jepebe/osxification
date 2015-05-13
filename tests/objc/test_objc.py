import ctypes
import ctypes.util
from types import MethodType
from unittest import TestCase
from osxification.foundation import NSString
from osxification.foundation import NSStringEncoding
from osxification.objc import objc, Class, Selector, Identifier


class ObjCTest(TestCase):


    def setUp(self):
        super(ObjCTest, self).setUp()
        self.FOUNDATION = ctypes.cdll.LoadLibrary(ctypes.util.find_library("foundation"))

    def test_message_sending(self):
        class_def = objc.getClass("NSString")
        
        alloc_selector = Selector.registerName("alloc")
        self.assertIsInstance(alloc_selector, Selector)

        self.assertEqual(alloc_selector.getName(), "alloc")

        pointer = objc.msgSend(class_def, alloc_selector)

        self.assertIsInstance(pointer, Identifier)

        init_selector = Selector.registerName("initWithCString:encoding:")

        string_pointer = objc.msgSend(pointer, init_selector, "test_string", NSStringEncoding.NSUTF8StringEncoding)

        self.FOUNDATION.NSLog(string_pointer)

        get_selector = Selector.registerName("cStringUsingEncoding:")
        result = objc.msgSend(string_pointer, get_selector, NSStringEncoding.NSUTF8StringEncoding)

        ns_string_value = ctypes.c_char_p(result.value).value

        self.assertEqual(ns_string_value, "test_string")



    def test_classing(self):
        class_def = objc.getClass("NSString")
        self.assertEqual(class_def.getName(), "NSString")
        self.assertIsInstance(class_def, Class)

        super_class = class_def.getSuperClass()
        self.assertEqual(super_class.getName(), "NSObject")

        self.assertIsNone(super_class.getSuperClass())


    def test_invoke(self):
        pointer = objc.alloc("NSString")
        initialized_pointer = objc.invoke(pointer, "initWithCString:encoding:", "invoked_test_string", NSStringEncoding.NSUTF8StringEncoding)
        self.FOUNDATION.NSLog(initialized_pointer)

    def test_method_addition(self):
        class_def = objc.getClass("NSString")
        pointer = objc.invoke(class_def, "alloc")
        Identifier.init = objc.bindMethodToClass(Identifier, "initWithCString:encoding:")

        initialized_pointer = pointer.init("wrapped_and_invoked_test_string", NSStringEncoding.NSUTF8StringEncoding)
        self.FOUNDATION.NSLog(initialized_pointer)


    def test_class_methods(self):
        class_def = objc.getClass("NSObject")

        methods = class_def.getMethodList()


