import ctypes
import datetime
from osxification.core_foundation import CFType, Prototype, CFFunction


class CFDate(CFType):
    type_id_function = CFFunction("CFTypeID CFDateGetTypeID()")


    def __str__(self):
        seconds = CFDate._GetAbsoluteTime(self)
        date = datetime.datetime(2001, 1, 1, 0, 0, 0, 0)
        date = date + datetime.timedelta(seconds=seconds)
        return date.isoformat(" ")

    def __repr__(self):
        return str(self)

Prototype.registerObjectType("CFDate", CFDate)
Prototype.registerType("CFAbsoluteTime", ctypes.c_double)

CFDate._GetAbsoluteTime = CFFunction("CFAbsoluteTime CFDateGetAbsoluteTime(CFDate)")

