from osxification.foundation import NSObject
from osxification.objc import objc


class NSUserNotificationCenter(NSObject):

    def __init__(self):
        identifier = objc.invoke(self.getClass(), "defaultUserNotificationCenter")
        super(NSUserNotificationCenter, self).__init__(identifier)

    def schedule(self, notification):
        self._scheduleNotification(notification)

NSUserNotificationCenter._scheduleNotification = NSUserNotificationCenter.bindMethodToClass("scheduleNotification:")