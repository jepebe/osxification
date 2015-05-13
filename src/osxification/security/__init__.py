import ctypes
import ctypes.util
from osxification.core_foundation import Prototype

SECURITY_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library('Security'))

def SecurityFunction(c_prototype):
    return Prototype.prototype(c_prototype, SECURITY_LIB)


kAuthorizationEmptyEnvironment = None

from .authorization_status import AuthorizationStatus
from .authorization_flags import AuthorizationFlags
from .authorization_item import AuthorizationItem
from .authorization_rights import AuthorizationRights
from .authorization import Authorization