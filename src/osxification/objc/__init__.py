import ctypes
import ctypes.util
from osxification.c import Prototype

OBJC_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library("objc"))

def ObjCFunction(c_prototype):
    return Prototype.prototype(c_prototype, OBJC_LIB)

from ._selector import Selector
from ._method import Method
from ._identifier import Identifier
from ._class import Class
from .objective_c import objc, autoreleasepool
from .objc_property import ObjCProperty
