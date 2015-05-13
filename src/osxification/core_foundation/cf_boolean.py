from osxification.core_foundation import CFType, Prototype, CFFunction


class CFBoolean(CFType):
    type_id_function = CFFunction("CFTypeID CFBooleanGetTypeID()")

    def __nonzero__(self):
        return CFBoolean._GetValue(self)

    def __int__(self):
        return 1 if self else 0

    def __str__(self):
        return "True" if self else "False"

    def __repr__(self):
        return str(self)

Prototype.registerObjectType("CFBoolean", CFBoolean)

CFBoolean._GetValue = CFFunction("bool CFBooleanGetValue(CFBoolean)")

