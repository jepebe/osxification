import ctypes
from unittest import TestCase
from osxification.security import AuthorizationFlags, AuthorizationItem, AuthorizationRights, Authorization
from osxification.system_configuration import SCPreferences


class SCPreferencesTest(TestCase):

    def test_creation(self):

        scp = SCPreferences("preferences", None)

        key_list = scp.keys()

        self.assertEqual(len(key_list), 6)


    def test_creation_with_authorization(self):
        flags = (
            AuthorizationFlags.kAuthorizationFlagDefaults
            | AuthorizationFlags.kAuthorizationFlagInteractionAllowed
            | AuthorizationFlags.kAuthorizationFlagPreAuthorize
            | AuthorizationFlags.kAuthorizationFlagExtendRights
        )

        item = AuthorizationItem("net.prador.proxychanger", 0, None, 0)
        rights = AuthorizationRights(1, ctypes.pointer(item))

        # authorization = Authorization(rights=rights, flags=flags)
        #
        # scp = SCPreferences("with.authorization", authorization=authorization)
        #
        # lock_state = scp.lock(wait=True)
        # self.assertTrue(lock_state)
        #
        # unlock_state = scp.unlock()
        # self.assertTrue(unlock_state)