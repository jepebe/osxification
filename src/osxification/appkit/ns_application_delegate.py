import logging


class NSApplicationDelegate(object):

    # @protocol
    def applicationDidFinishLaunching(self, notification):
        logging.info(notification)


#Need a class cache?
#NSApplicationDelegate.addInstanceMethod("applicationDidFinishLaunching:", attribute_name="applicationDidFinishLaunching", argument_types=[Identifier], return_type="None", signature="v@:@")