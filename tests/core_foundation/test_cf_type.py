from unittest import TestCase

from osxification.core_foundation import CFString, CFType
from osxification.core_foundation.cf_array import CFArray


class CFTypeTest(TestCase):
    def test_types(self):
        cftypes = [CFString("cfstring"),
                   CFArray(None)
                   ]

        for cftype in cftypes:
            id = cftype.getTypeIDForClass()

            self.assertEqual(id, cftype.getTypeID())
            self.assertEqual(cftype.__class__.__name__, str(CFType.getTypeDescription(id)))


