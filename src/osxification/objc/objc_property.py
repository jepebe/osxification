from osxification.objc import Identifier, objc


class ObjCProperty(object):
    def __init__(self, name, property_type=Identifier, read_only=False):
        super(ObjCProperty, self).__init__()

        if isinstance(property_type, str):
            print(globals()[property_type])

        self._name = name
        self._type = property_type

        self._getter = objc.createFunction(self._name, return_type=property_type)

        self._setter = None
        if not read_only:
            setter_name = "set" + name[0].upper() + name[1:] + ":"
            self._setter = objc.createFunction(setter_name, argument_types=[property_type])


    def __get__(self, instance, owner=None):
        return self._getter(instance)

    def __set__(self, instance, value):
        if self._setter is None:
            raise AttributeError("can't set property")
        self._setter(instance, value)
