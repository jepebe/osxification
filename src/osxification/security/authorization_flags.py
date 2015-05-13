from osxification.c import Enum


class AuthorizationFlags(Enum):
    kAuthorizationFlagDefaults = None
    kAuthorizationFlagInteractionAllowed = None
    kAuthorizationFlagExtendRights = None
    kAuthorizationFlagPartialRights = None
    kAuthorizationFlagDestroyRights = None
    kAuthorizationFlagPreAuthorize = None
    kAuthorizationFlagNoData = None


AuthorizationFlags.addEnum("kAuthorizationFlagDefaults", 0)
AuthorizationFlags.addEnum("kAuthorizationFlagInteractionAllowed", (1 << 0))
AuthorizationFlags.addEnum("kAuthorizationFlagExtendRights", (1 << 1))
AuthorizationFlags.addEnum("kAuthorizationFlagPartialRights", (1 << 2))
AuthorizationFlags.addEnum("kAuthorizationFlagDestroyRights", (1 << 3))
AuthorizationFlags.addEnum("kAuthorizationFlagPreAuthorize", (1 << 4))
AuthorizationFlags.addEnum("kAuthorizationFlagNoData", (1 << 20))

AuthorizationFlags.registerEnum("authorization_flags")