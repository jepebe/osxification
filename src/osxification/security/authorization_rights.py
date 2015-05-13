import ctypes
from osxification.security import AuthorizationItem


class AuthorizationRights(ctypes.Structure):
    _fields_ = [
        ('count', ctypes.c_uint32),
        ('items', ctypes.POINTER(AuthorizationItem)),
    ]

