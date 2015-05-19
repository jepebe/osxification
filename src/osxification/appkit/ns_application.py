from osxification.foundation import NSObject
from osxification.objc import ObjCProperty, Identifier


class NSApplication(NSObject):

    def __init__(self):
        identifier = self.invokeClassMethod("sharedApplication")
        super(NSApplication, self).__init__(identifier)

    def run(self):
        self._run()


    @classmethod
    def sharedApplication(cls):
        return NSApplication()


    running = ObjCProperty("isRunning", property_type=bool, read_only=True)
    delegate = ObjCProperty("delegate", property_type=Identifier)

NSApplication._run = NSApplication.bindMethodToClass("run")