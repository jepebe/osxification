from unittest import TestCase
from osxification.core_foundation import CFString


class CFStringTest(TestCase):

    def test_creation(self):

        string = CFString("Happy String")

        for index, char in enumerate("Happy String"):
            self.assertEqual(char, string[index])


        copy_of_string = string.copy()

        for index, char in enumerate(copy_of_string):
            self.assertEqual(char, string[index])

    def test_compare(self):
        A = "A"
        B = "B"
        cfA = CFString("A")
        cfB = CFString("B")

        self.assertEqual(A, cfA)
        self.assertEqual(cfA, cfA)
        self.assertEqual(cfA, A)

        self.assertNotEqual(B, cfA)
        self.assertNotEqual(cfB, cfA)

