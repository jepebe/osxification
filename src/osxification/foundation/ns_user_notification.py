from osxification.foundation import NSObject, NSString
from osxification.objc import ObjCProperty


class NSUserNotification(NSObject):

    def __init__(self):
        identifier = NSUserNotification.new()
        super(NSUserNotification, self).__init__(identifier)

    title = ObjCProperty("title", property_type=NSString)
    subtitle = ObjCProperty("subtitle", property_type=NSString)
    informativeText = ObjCProperty("informativeText", property_type=NSString)
    identifier = ObjCProperty("identifier", property_type=NSString)
    soundName = ObjCProperty("soundName", property_type=NSString)

    contentImage = ObjCProperty("contentImage") # property_type updated in NSImage, due to circular dependency