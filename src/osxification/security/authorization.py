import ctypes
from osxification.core_foundation import CFType, Prototype
from osxification.security import AuthorizationFlags, AuthorizationStatus, kAuthorizationEmptyEnvironment, \
    AuthorizationItem, AuthorizationRights, SecurityFunction


class Authorization(object):

    def __init__(self, rights=None, environment=kAuthorizationEmptyEnvironment, flags=AuthorizationFlags.kAuthorizationFlagDefaults):

        if rights is None:
            item = AuthorizationItem("osxification.default.rights", 0, None, 0)
            rights = AuthorizationRights(1, ctypes.pointer(item))

        self.__authorization_ptr = ctypes.c_void_p(0)
        status = Authorization._create(ctypes.byref(rights), environment, flags, ctypes.byref(self.__authorization_ptr))

        if status != AuthorizationStatus.errAuthorizationSuccess:
            self.__authorization_ptr = None
            raise UserWarning("[Authorization] Unable to create authorization: %d" % status)


    @classmethod
    def from_param(cls, c_class_object):
        if c_class_object is None:
            return ctypes.c_void_p()
        else:
            return c_class_object.__authorization_ptr


    def __del__(self):
        if self.__authorization_ptr is not None:
            status = Authorization._free(self, AuthorizationFlags.kAuthorizationFlagDestroyRights)
            if status != AuthorizationStatus.errAuthorizationSuccess:
                print("[Authorization] Error freeing Authorization: %d" % status)


Prototype.registerType("Authorization", Authorization)

Authorization._create = SecurityFunction("authorization_status AuthorizationCreate(void*, void*, authorization_flags, void*)")
Authorization._free = SecurityFunction("authorization_status AuthorizationFree(Authorization, authorization_flags)")