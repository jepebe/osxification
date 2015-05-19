import ctypes
from osxification.c import Prototype
from osxification.objc import ObjCFunction, Selector, objc_method_description


class Protocol(object):

    def __init__(self, identifier):
        super().__init__()
        self._identifier = identifier

    @property
    def _as_parameter_(self):
       """
       :rtype: Identifier
       """
       return Protocol.from_param(self)

    @staticmethod
    def _asReturnType(value):
        if value is None or value == 0:
            return None
        return Protocol(value)

    @classmethod
    def from_param(cls, identifier):
        if identifier is not None and not isinstance(identifier, Protocol):
            raise ValueError("Identifier must be a pointer to an instance of a Protocol! Received: %s" % type(identifier))

        if identifier is None:
            return ctypes.c_void_p()
        else:
            return ctypes.c_void_p(identifier._identifier)


    def getName(self):
        """ :rtype: str """
        return Protocol._getName(self)

    def getMethodDescription(self, selector, is_required_method=False, is_instance_method=True):
        """ :rtype: objc_method_description """
        selector = Selector.checkSelector(selector)
        method_description = Protocol._getMethodDescription(self, selector, is_required_method, is_instance_method)

        if method_description.name.value is None and method_description.types is None:
            method_description = None
        return method_description

    def __eq__(self, other):
        if isinstance(other, Protocol):
            return Protocol._isEqual(self, other)
        return False

    def __str__(self):
        return self.getName()

    def __repr__(self):
        return "<ObjectiveC Protocol with name: %s>" % self.getName()



Prototype.registerType("Protocol", Protocol)

Protocol._getName = ObjCFunction("char* protocol_getName(Protocol)")
Protocol._isEqual = ObjCFunction("bool protocol_isEqual(Protocol, Protocol)")
Protocol._getMethodDescription = ObjCFunction("objc_method_description protocol_getMethodDescription(Protocol, SEL, bool, bool)")
