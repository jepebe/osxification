from unittest import TestCase
from osxification.appkit import NSImage


class NSImageTest(TestCase):

    def test_creation(self):
        image = NSImage("../img/statoil_slack_neg.png")
        print(image.size.width)
        print(image.size.height)

