from osxification.security import Authorization
from osxification.core_foundation import CFType, Prototype, CFString, CFArray
from osxification.system_configuration import SCFunction

class SCPreferences(CFType):
    type_id_function = SCFunction("CFTypeID SCPreferencesGetTypeID()")

    def __init__(self, name, prefsID=None, authorization=None):
        if authorization is not None:
            assert isinstance(authorization, Authorization)
            c_ptr = SCPreferences._create_with_auth(None, name, prefsID, authorization)
        else:
            c_ptr = SCPreferences._create(None, name, prefsID)
        super(SCPreferences, self).__init__(c_ptr)

    def lock(self, wait=True):
        return bool(SCPreferences._lock(self, wait))

    def unlock(self):
        return bool(SCPreferences._unlock(self))

    def keys(self):
        return SCPreferences._keys(self)

Prototype.registerObjectType("SCPreferences", SCPreferences)

SCPreferences._create = SCFunction("c_void_p SCPreferencesCreate(c_void_p, CFString, CFString)")
SCPreferences._create_with_auth = SCFunction("c_void_p SCPreferencesCreateWithAuthorization(c_void_p, CFString, CFString, Authorization)")
SCPreferences._keys = SCFunction("CFArrayObj SCPreferencesCopyKeyList(SCPreferences)")
SCPreferences._lock = SCFunction("Boolean SCPreferencesLock(SCPreferences, Boolean)")
SCPreferences._unlock = SCFunction("Boolean SCPreferencesUnlock(SCPreferences)")