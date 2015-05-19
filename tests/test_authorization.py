import ctypes
import unittest

from osxification.security import Authorization, AuthorizationItem, AuthorizationFlags
from osxification.security.authorization_rights import AuthorizationRights


class AuthorizationTest(unittest.TestCase):
    def test_creation(self):
        flags = (
            AuthorizationFlags.kAuthorizationFlagDefaults
            | AuthorizationFlags.kAuthorizationFlagInteractionAllowed
            | AuthorizationFlags.kAuthorizationFlagPreAuthorize
            | AuthorizationFlags.kAuthorizationFlagExtendRights
        )

        item = AuthorizationItem("net.prador.proxychanger", 0, None, 0)
        rights = AuthorizationRights(1, ctypes.pointer(item))

        # authorization = Authorization(rights=rights, flags=flags)