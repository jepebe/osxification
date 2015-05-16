import ctypes
import ctypes.util
from osxification.c import Prototype, PrototypeError

Prototype.registerType("CFOptionFlags", ctypes.c_uint32)
Prototype.registerType("Boolean", ctypes.c_ubyte)
Prototype.registerType("UniChar", ctypes.c_ushort)
Prototype.registerType("UniChar*", ctypes.POINTER(ctypes.c_ushort))

CORE_FOUNDATION_LIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library('CoreFoundation'))

def CFFunction(c_prototype):
    return Prototype.prototype(c_prototype, CORE_FOUNDATION_LIB)

from .cf_type import CFType
from .cf_boolean import CFBoolean
from .cf_number_type import CFNumberType
from .cf_number import CFNumber
from .cf_date import CFDate
from .cf_data import CFData
from .cf_string import CFString
from .cf_array import CFArray
from .cf_bundle import CFBundle
from .cf_dictionary import CFDictionary
from .cf_run_loop import CFRunLoop


Prototype.registerObjectType("CFPropertyList", CFType)