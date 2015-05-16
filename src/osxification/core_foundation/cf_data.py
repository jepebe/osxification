from osxification.core_foundation import CFType, Prototype, CFFunction


class CFData(CFType):
    type_id_function = CFFunction("CFTypeID CFDataGetTypeID()")

    def __len__(self):
        return CFData._GetLength(self)

    def __str__(self):
        return "CFData of length %d" % len(self)

    def __repr__(self):
        return str(self)

Prototype.registerObjectType("CFData", CFData)

CFData._GetLength = CFFunction("CFIndex CFDataGetLength(CFData)")

