from unittest import TestCase
from osxification.core_foundation import CFNumber
from osxification.core_foundation.cf_number_type import CFNumberType


class CFNumberTest(TestCase):

    def test_cf_number(self):
        number = CFNumber(1)
        self.assertEqual(number.getType(), CFNumberType.kCFNumberSInt64Type)
        self.assertFalse(number.isFloatType())
        self.assertEqual(str(number), "1")
        self.assertEqual(int(number), 1)
        self.assertEqual(float(number), 1.0)

        number = CFNumber(1.1)
        self.assertEqual(number.getType(), CFNumberType.kCFNumberFloat64Type)
        self.assertTrue(number.isFloatType())
        self.assertEqual(str(number), "1.1")
        self.assertEqual(int(number), 1)
        self.assertAlmostEqual(float(number), 1.1)


    def test_fail(self):
        with self.assertRaises(TypeError):
            number = CFNumber("hello")



