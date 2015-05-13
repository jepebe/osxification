from osxification.c import Enum


class AuthorizationStatus(Enum):
    errAuthorizationSuccess = None
    errAuthorizationInvalidSet = None
    errAuthorizationInvalidRef = None
    errAuthorizationInvalidTag = None
    errAuthorizationInvalidPointer = None
    errAuthorizationDenied = None
    errAuthorizationCanceled = None
    errAuthorizationInteractionNotAllowed = None
    errAuthorizationInternal = None
    errAuthorizationExternalizeNotAllowed = None
    errAuthorizationInternalizeNotAllowed = None
    errAuthorizationInvalidFlags = None
    errAuthorizationToolExecuteFailure = None
    errAuthorizationToolEnvironmentError = None
    errAuthorizationBadAddress = None

AuthorizationStatus.addEnum("errAuthorizationSuccess", 0)
AuthorizationStatus.addEnum("errAuthorizationInvalidSet", -60001) # The authorization rights are invalid.
AuthorizationStatus.addEnum("errAuthorizationInvalidRef", -60002) # The authorization reference is invalid.
AuthorizationStatus.addEnum("errAuthorizationInvalidTag", -60003) # The authorization tag is invalid.
AuthorizationStatus.addEnum("errAuthorizationInvalidPointer", -60004) # The returned authorization is invalid.
AuthorizationStatus.addEnum("errAuthorizationDenied", -60005) # The authorization was denied.
AuthorizationStatus.addEnum("errAuthorizationCanceled", -60006) # The authorization was cancelled by the user.
AuthorizationStatus.addEnum("errAuthorizationInteractionNotAllowed", -60007) # The authorization was denied since no user interaction was possible.
AuthorizationStatus.addEnum("errAuthorizationInternal", -60008) # Unable to obtain authorization for this operation.
AuthorizationStatus.addEnum("errAuthorizationExternalizeNotAllowed", -60009) # The authorization is not allowed to be converted to an external format.
AuthorizationStatus.addEnum("errAuthorizationInternalizeNotAllowed", -60010) # The authorization is not allowed to be created from an external format.
AuthorizationStatus.addEnum("errAuthorizationInvalidFlags", -60011) # The provided option flag(s) are invalid for this authorization operation.
AuthorizationStatus.addEnum("errAuthorizationToolExecuteFailure", -60031) # The specified program could not be executed.
AuthorizationStatus.addEnum("errAuthorizationToolEnvironmentError", -60032) # An invalid status was returned during execution of a privileged tool.
AuthorizationStatus.addEnum("errAuthorizationBadAddress", -60033) # The requested socket address is invalid (must be 0-1023 inclusive).
AuthorizationStatus.registerEnum("authorization_status")