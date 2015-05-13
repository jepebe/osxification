from osxification.c import Prototype
from osxification.core_foundation import CFType, CFArray
from osxification.system_configuration import SCFunction, SCPreferences


class SCNetworkSet(CFType):
    type_id_function = SCFunction("CFTypeID SCNetworkServiceGetTypeID()")

    def __init__(self, prefs):
        assert isinstance(prefs, SCPreferences)

        c_ptr = SCNetworkSet._copy_current(prefs)

        super(SCNetworkSet, self).__init__(c_ptr)

    def getServices(self):
        """
        :rtype: CFArray of SCNetworkService
        """
        return SCNetworkSet._copy_services(self)


Prototype.registerObjectType("SCNetworkSet", SCNetworkSet)

SCNetworkSet._copy_current = SCFunction("c_void_p SCNetworkSetCopyCurrent(SCPreferences)")
SCNetworkSet._copy_services = SCFunction("CFArrayObj SCNetworkSetCopyServices(SCNetworkSet)")