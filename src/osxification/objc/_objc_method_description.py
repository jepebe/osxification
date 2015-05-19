import ctypes
from osxification.c import Prototype
from osxification.objc import Selector


class objc_method_description(ctypes.Structure):
    _fields_ = [
        ('_name', Selector),
        ('_types', ctypes.c_char_p),
    ]

    @property
    def name(self):
        """ :rtype: Selector """
        return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

    @property
    def types(self):
        """ :rtype: Selector """
        if self._types is not None:
            return self._types.decode()
        return None

    # @types.setter
    # def types(self, types):
    #     self._types = types

    def __repr__(self):
        return "<objc_method_description: %s %s>" % (self.name.getName(), self.types)

Prototype.registerType("objc_method_description", objc_method_description)