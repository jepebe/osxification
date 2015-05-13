import ctypes
import ctypes.util
from osxification.c import Prototype
import osxification.foundation as Foundation
from osxification.objc import ObjCProperty

APPKIT_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library("AppKit"))

def AppKitFunction(c_prototype):
    return Prototype.prototype(c_prototype, APPKIT_LIB)

from .ns_image import NSImage

Foundation.NSUserNotification.contentImage = ObjCProperty("contentImage", property_type=NSImage) # update the property due to circular dependency
