import ctypes
import ctypes.util

from osxification.c import Prototype


FOUNDATION_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library("Foundation"))


def FoundationFunction(c_prototype):
    return Prototype.prototype(c_prototype, FOUNDATION_LIB)


class NSSize(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_longdouble),
        ('height', ctypes.c_longdouble)
    ]


Prototype.registerType("NSSize", NSSize)

from .ns_object import NSObject
from .ns_string_encoding import NSStringEncoding
from .ns_string import NSString
from .ns_user_notification import NSUserNotification
from .ns_user_notification_center import NSUserNotificationCenter

Prototype.registerType("NSString", NSString)

NSLog = FoundationFunction("void NSLog(NSString)")
