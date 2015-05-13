from unittest import TestCase

from osxification.foundation import NSUserNotification, NSString, NSUserNotificationCenter, NSSize
from osxification.appkit import NSImage


class NSUserNotificationTest(TestCase):
    def test_creation(self):
        notification = NSUserNotification()

        notification.title = "Title"
        self.assertIsInstance(notification.title, NSString)
        self.assertEqual("Title", notification.title)

        notification.subtitle = "Subtitle"
        self.assertIsInstance(notification.subtitle, NSString)
        self.assertEqual("Subtitle", notification.subtitle)

        notification.informativeText = "InformativeText"
        self.assertIsInstance(notification.informativeText, NSString)
        self.assertEqual("InformativeText", notification.informativeText)

        notification.identifier = "Identifier"
        self.assertIsInstance(notification.identifier, NSString)
        self.assertEqual("Identifier", notification.identifier)

        notification.soundName = "NSUserNotificationDefaultSoundName"
        self.assertIsInstance(notification.soundName, NSString)
        self.assertEqual("NSUserNotificationDefaultSoundName", notification.soundName)

        image = NSImage("../img/statoil_slack_neg.png")
        #image.size = NSSize(64, 64)
        notification.contentImage = image
        self.assertIsInstance(notification.contentImage, NSImage)
        # self.assertEqual(image, notification.contentImage)

        notification_center = NSUserNotificationCenter()
        notification_center.schedule(notification)