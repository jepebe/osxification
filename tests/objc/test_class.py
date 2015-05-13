from unittest import TestCase
from osxification.foundation import NSObject, NSString
from osxification.objc import Class, objc


class ClassTest(TestCase):

    def test_allocate_class(self):
        nsobject = objc.getClass("NSObject")

        my_class = objc.allocateClassPair(nsobject, "MyClass")

        self.assertEqual(my_class.getName(), "MyClass")
        self.assertEqual(my_class.getSuperClass(), nsobject)
        self.assertIsNone(objc.getClass("MyClass"))

        objc.registerClassPair(my_class)
        self.assertEqual(my_class, objc.getClass("MyClass"))

        objc.disposeClassPair(my_class)
        self.assertIsNone(objc.getClass("MyClass"))


    def test_add_method_to_class(self):
        nsobject = objc.getClass("NSObject")
        my_class = objc.allocateClassPair(nsobject, "FiveClass")
        objc.registerClassPair(my_class)

        def five(self, selector):
            return 5

        success = my_class.addMethod("five", five, "i@:")
        self.assertTrue(success)

        instance = objc.invoke(objc.alloc("FiveClass"), "init")
        self.assertIsNotNone(instance)
        self.assertEqual("FiveClass", objc.getClassName(instance))

        five_function = objc.createFunction("five", return_type=int)
        result = five_function(instance)
        self.assertEqual(result, 5)




