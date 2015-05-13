from unittest import TestCase
from osxification.core_foundation import CFType
from osxification.system_configuration import SCNetworkSet
from osxification.system_configuration.sc_preferences import SCPreferences


class SCNetworkSetTest(TestCase):

    def test_creation(self):
        prefs = SCPreferences("sc.network.set.test")
        scns = SCNetworkSet(prefs)

        services = scns.getServices()

        for service in services:
            # print(str(service.name()), service.isEnabled())
            # service.show()
            protocols = service.getProtocols()

            # for protocol in protocols:
            #     CFType.createCReference(protocol).show()
