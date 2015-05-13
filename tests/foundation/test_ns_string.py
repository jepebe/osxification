from unittest import TestCase
from osxification.foundation import NSString


class NSStringTest(TestCase):

    def test_numbers(self):
        num = NSString("3.45")

        self.assertEqual(float(num), 3.45)
        self.assertEqual(int(num), 3)

    def test_creation(self):
        string = NSString("ns_test_string")

        self.assertEqual(str(string), "ns_test_string")

    def test_equality(self):
        string_1 = NSString("string 1")
        string_2 = NSString("string 2")
        string_3 = NSString("string 1")


        self.assertEqual(string_1, string_1)
        self.assertEqual(string_1, string_3)
        self.assertEqual(string_3, string_1)
        self.assertEqual(string_1, "string 1")
        self.assertNotEqual(string_1, string_2)