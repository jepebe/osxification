from osxification.foundation import NSStringEncoding, NSObject

class NSString(NSObject):

    def __init__(self, content, encoding=None):
        if isinstance(content, str):
            encoding = NSStringEncoding.NSUTF8StringEncoding
        # elif isinstance(content, unicode):
        #     encoding = NSStringEncoding.NSUnicodeStringEncoding
        else:
            raise UserWarning("[%s] Error: 'content' should be a string, received: %s" % (self.__class__.__name__, type(content)))

        identifier = NSString._init(self.alloc(), content, encoding)
        super(NSString, self).__init__(identifier)

    def __str__(self):
        return self._asCString(NSStringEncoding.NSUTF8StringEncoding)

    # def __unicode__(self):
    #     return self._asCString(NSStringEncoding.NSUnicodeStringEncoding)

    def __int__(self):
        return self._intValue()

    def __float__(self):
        return self._floatValue()

    def __eq__(self, other):
        return self._isEqualToString(other)


    @classmethod
    def from_param(cls, instance):
        if isinstance(instance, str):
            instance = NSString(instance)

        return NSObject.from_param(instance)



NSString._init = NSString.bindMethodToClass("initWithCString:encoding:")
NSString._asCString = NSString.bindMethodToClass("cStringUsingEncoding:", returns=str)
NSString._intValue = NSString.bindMethodToClass("integerValue", returns=int)
NSString._floatValue = NSString.bindMethodToClass("doubleValue", returns=float)
NSString._isEqualToString = NSString.bindMethodToClass("isEqualToString:", parameters=[NSString], returns=bool)