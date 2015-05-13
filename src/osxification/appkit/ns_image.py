from osxification.objc import ObjCProperty
import osxification.foundation as Foundation

class NSImage(Foundation.NSObject):

    def __init__(self, path):
        identifier = self.alloc()
        identifier = NSImage._initByReferencingFile(identifier, path)
        super(NSImage, self).__init__(identifier)

    size = ObjCProperty("size", property_type=Foundation.NSSize)



NSImage._initByReferencingFile = NSImage.bindMethodToClass("initByReferencingFile:", parameters=[Foundation.NSString])
