import ctypes

class AuthorizationItem(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('valueLength', ctypes.c_uint32),
        ('value', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
    ]

    def __init__(self, name, valueLength, value, flags):
        self.name = name.encode()
        self.valueLength = valueLength
        self.value = value
        self.flags = flags


