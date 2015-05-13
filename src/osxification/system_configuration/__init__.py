import ctypes
import ctypes.util
from osxification.core_foundation import Prototype


SYSTEM_CONFIGURATION_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library('SystemConfiguration'))

def SCFunction(c_prototype):
    return Prototype.prototype(c_prototype, SYSTEM_CONFIGURATION_LIB)

from .sc_preferences import SCPreferences
from .sc_network_set import SCNetworkSet
from .sc_network_service import SCNetworkService
from .sc_dynamic_store import SCDynamicStore, SCDynamicStoreCallBack

