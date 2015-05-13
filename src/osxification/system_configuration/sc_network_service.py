from osxification.c import Prototype
from osxification.core_foundation import CFType, CFString, CFArray
from osxification.system_configuration import SCFunction


class SCNetworkService(CFType):
    type_id_function = SCFunction("CFTypeID SCNetworkServiceGetTypeID()")

    def __init__(self):
        raise UserWarning("[SCNetworkService] Construction not supported")

    def name(self):
        """
        :rtype: CFString
        """
        return SCNetworkService._get_name(self)

    def getProtocols(self):
        """
        :rtype: CFArray of SCNetworkProtocol
        """
        return SCNetworkService._copy_protocols(self)

    def isEnabled(self):
        """
        :rtype: bool
        """
        return SCNetworkService._is_enabled(self)


Prototype.registerObjectType("SCNetworkService", SCNetworkService)

SCNetworkService._get_name = SCFunction("CFStringRef SCNetworkServiceGetName(SCNetworkService)")
SCNetworkService._copy_protocols = SCFunction("CFArrayRef SCNetworkServiceCopyProtocols(SCNetworkService)")
SCNetworkService._is_enabled = SCFunction("bool SCNetworkServiceGetEnabled(SCNetworkService)")
