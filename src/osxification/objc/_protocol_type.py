from osxification.objc import objc


class ProtocolType(type):
    def __init__(cls, name, bases, dct):
        super(ProtocolType, cls).__init__(name, bases, dct)


        print("Protocolling: %s" % name)