from unittest import TestCase
from osxification.core_foundation import CFArray, CFString


class CFArrayTest(TestCase):

    def test_creation(self):

        array = CFArray(None)

        self.assertEqual(len(array), 0)


    def test_strings(self):
        items = ["A", "B", "C"]

        array = CFArray(items)
        self.assertEqual(len(array), 3)

        for index, item in enumerate(array):
            self.assertEqual(item, items[index])
