import ctypes
import ctypes.util
from unittest import TestCase
from osxification.foundation import NSObject
from osxification.objc import objc, Protocol, Selector, ProtocolType


class ProtocolTest(TestCase):
    def setUp(self):
        self.FOUNDATION = ctypes.cdll.LoadLibrary(ctypes.util.find_library("foundation"))

    def test_protocol(self):

        ns_object_protocol = objc.getProtocol("NSObject")

        self.assertIsNotNone(ns_object_protocol)
        self.assertIsInstance(ns_object_protocol, Protocol)

        self.assertEqual(ns_object_protocol.getName(), "NSObject")


    def test_protocol_list(self):
        protocols = objc.getProtocols()

        names = [protocol.getName() for protocol in protocols]

        self.assertTrue("NSLocking" in names)

    def test_equality(self):

        ns_object_protocol_1 = objc.getProtocol("NSObject")
        ns_object_protocol_2 = objc.getProtocol("NSObject")
        ns_locking_protocol = objc.getProtocol("NSLocking")

        self.assertIsNotNone(ns_object_protocol_1)
        self.assertIsNotNone(ns_object_protocol_2)
        self.assertIsNotNone(ns_locking_protocol)

        self.assertNotEqual(id(ns_object_protocol_1), id(ns_object_protocol_2))

        self.assertEqual(ns_object_protocol_1, ns_object_protocol_2)
        self.assertNotEqual(ns_object_protocol_1, ns_locking_protocol)
        self.assertNotEqual(ns_object_protocol_1, "string")


    def test_method_description(self):
        ns_locking_protocol = objc.getProtocol("NSLocking")

        method_description = ns_locking_protocol.getMethodDescription("lock", is_required_method=True)

        self.assertEqual(method_description.name.getName(), "lock")
        self.assertEqual(method_description.types, "v16@0:8")

        self.assertIsNone(ns_locking_protocol.getMethodDescription("lock", is_required_method=True, is_instance_method=False))
        self.assertIsNone(ns_locking_protocol.getMethodDescription("lock", is_instance_method=False))
        self.assertIsNone(ns_locking_protocol.getMethodDescription("lock"))


    def test_add_protocol(self):
        class Proto(NSObject):
            def __init__(self):
                identifier = self.new()
                super(Proto, self).__init__(identifier)

        proto_object = Proto()

        locking_protocol = objc.getProtocol("NSLocking")

        self.assertFalse(proto_object.conformsToProtocol(locking_protocol))

        self.assertTrue(proto_object.getClass().addProtocol(locking_protocol))

        self.assertTrue(proto_object.conformsToProtocol(locking_protocol))

        self.assertFalse(proto_object.getClass().respondsToSelector("lock"))
        self.assertFalse(proto_object.getClass().respondsToSelector("unlock"))


    def test_add_protocol_implementation(self):

        # class NSLocking()

        class Locking(NSObject):

            def __init__(self):
                identifier = self.new()
                super(Locking, self).__init__(identifier)
                self._locked = False


            def lock(self):
                self._locked = True

            def unlock(self):
                self._locked = False



        proto_object = Locking()

        locking_protocol = objc.getProtocol("NSLocking")

        self.assertFalse(proto_object.conformsToProtocol(locking_protocol))

        self.assertTrue(proto_object.getClass().addProtocol(locking_protocol))

        self.assertTrue(proto_object.conformsToProtocol(locking_protocol))

        self.assertFalse(proto_object.getClass().respondsToSelector("lock"))
        self.assertFalse(proto_object.getClass().respondsToSelector("unlock"))

    # def test_protocol_subclassing(self):
    #
    #     class NSLocking(ProtocolClass):
    #
    #         def lock(self):
    #             pass
    #
    #         def unlock(self):
    #             pass
    #
    #     NSLocking.setProtocolMethod("lock", "lock", )
    #
    #     class Proto(NSObject):
    #
    #         def __init__(self):
    #             identifier = self.new()
    #             super(Proto, self).__init__(identifier)
    #
    #             self._locked = False
    #
    #
    #         def lock(self):
    #             self._locked = True
    #
    #         def unlock(self):
    #             self._locked = False
    #
    #
    #
    #     proto_object = Proto()
    #     proto_object.lock()
    #
    #     locking_protocol = objc.getProtocol("NSLocking")
    #
    #     self.assertFalse(proto_object.conformsToProtocol(locking_protocol))
    #
    #     self.assertTrue(proto_object.getClass().addProtocol(locking_protocol))
    #
    #     self.assertTrue(proto_object.conformsToProtocol(locking_protocol))