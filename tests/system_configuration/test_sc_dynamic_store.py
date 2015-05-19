from unittest import TestCase
from osxification.core_foundation import CFRunLoop, CFString, CFArray
from osxification.system_configuration import SCDynamicStore, SCDynamicStoreCallBack

class SCDynamicStoreTest(TestCase):

    def test_creation(self):
        def testCallback(store, keys, info):
            store = SCDynamicStore.createCReference(store)
            keys = CFArray.createCReference(keys)

            for key in keys:
                print(key)
                dictionary = store.getValue(key)
                # dictionary.show()

                for key in dictionary.keys():
                    self.assertTrue(key in dictionary)
                    value = dictionary[key]
                    print("\t%s: %s" % (key, value))


            #print(store, keys, info)

            # CFRunLoop.stop(CFRunLoop.getCurrentRunLoop())

        callback = SCDynamicStoreCallBack(testCallback)
        dynamic_store = SCDynamicStore("test-of-global-network-watcher", callback)

        # success = dynamic_store.addTemporaryValue("State:test_key", CFString("test_value"))
        # print("Temporary key: %s" % success)

        keys = dynamic_store.keys('State:/Network/.*')

        self.assertTrue(len(keys) > 0)

        pattern = CFArray(['State:/Network/Interface/.*/AirPort'])
        # pattern = CFArray(['State:/Network/Interface/.*/AirPort', 'State:/Network/(Service/.+|Global)/Proxies'])

        success = dynamic_store.setNotificationKeys(pattern=pattern)
        self.assertTrue(success)

        run_loop = CFRunLoop.getCurrentRunLoop()
        self.assertIsNotNone(run_loop)


        # run_loop.addSource(dynamic_store.createRunLoopSource(), "test_mode")
        run_loop.addSource(dynamic_store.createRunLoopSource(), "kCFRunLoopDefaultMode")

        # time.sleep(10)
        # notified_keys = dynamic_store.notifiedKeys()
        # for key in notified_keys:
        #     print(key)

        result = CFRunLoop.runInMode(seconds=1, return_after_source_handled=False)
        #print(result)
        #
        #CFRunLoop.run()
