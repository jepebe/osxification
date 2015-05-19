import ctypes
from osxification.c import Prototype


class Identifier(ctypes.c_void_p):

    def __eq__(self, other):
        if isinstance(other, ctypes.c_void_p):
            return self.value == other.value

        if hasattr(other, "_as_parameter_"):
            other = other._as_parameter_ #convert any ObjCClass (or anyone else) that are wrapping identifiers
            return self.value == other.value

        return False

    @classmethod
    def from_param(cls, identifier):
        if hasattr(identifier, "_as_parameter_"):
            identifier = identifier._as_parameter_ #convert any ObjCClass (or anyone else) that are wrapping identifiers

        if identifier is not None and not isinstance(identifier, ctypes.c_void_p):
            raise ValueError("Identifier must be a pointer to an instance! Received: %s" % type(identifier))

        if identifier is None:
            return ctypes.c_void_p()
        else:
            return identifier

    def __bool__(self):
        return bool(self.value)



Prototype.registerType("id", Identifier)