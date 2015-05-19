from unittest import TestCase

from osxification.appkit import NSApplication, NSApplicationDelegate
from osxification.foundation import NSObject
from osxification.objc import objc


class TestDelegate(NSObject):

    def __init__(self):
        identifier = self.new()
        super().__init__(identifier)
        self.did_finish_launching = False

    def applicationDidFinishLaunching(self, notification):
        self.did_finish_launching = True


class NSApplicationTest(TestCase):

    def test_ns_application(self):
        nsapp = NSApplication.sharedApplication()

        self.assertEqual(nsapp, NSApplication())

        self.assertFalse(nsapp.running)

        delegate = TestDelegate()
        protocol = objc.getProtocol("_NSApplicationLightLaunchDelegate") #NSApplicationDelegate not avaConverted Convilable at runtime unless compiled
        self.assertIsNotNone(protocol)
        self.assertTrue(delegate.getClass().addProtocol(protocol))
        self.assertTrue(delegate.conformsToProtocol(protocol))


        print(protocol.getMethodDescription("applicationDidFinishLaunching:"))

        nsapp.delegate = delegate

        self.assertEqual(delegate, nsapp.delegate)

        # protocol.createProtocolMethod("applicationDidFinishLaunching:")


        # nsapp.run()

