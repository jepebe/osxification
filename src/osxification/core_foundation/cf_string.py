import ctypes
from osxification.core_foundation import CFType, CFFunction, Prototype


class CFString(CFType):
    type_id_function = CFFunction("CFTypeID CFStringGetTypeID()")

    def __init__(self, content):
        c_ptr = CFString._create_with_c_string(None, content, len(content))
        super(CFString, self).__init__(c_ptr)

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return unichr(CFString._char_at(self, index))

        raise IndexError("Index out of bounds: 0 <= %d < %d" % (index, len(self)))

    def __len__(self):
        return CFString._length(self)

    def __str__(self):
        max_size = CFString._max_size_for_encoding(len(self), 0x08000100)
        string_buffer = ctypes.create_string_buffer(max_size)
        success = CFString._GetCString(self.convertToPointer(self), string_buffer, max_size, 0x08000100)
        if success:
            return string_buffer.value

        return None

    def copy(self):
        """
        :return: A copy of this string
        :rtype: CFString
        """
        return self.createCopy(self.convertToPointer(self))

    def __eq__(self, other):
        return CFString._compare(self, other, 0) == 0

    def __repr__(self):
        return str(self)

    @classmethod
    def from_param(cls, c_class_object):
        if isinstance(c_class_object, str):
            c_class_object = CFString(c_class_object)
            c_class_object.retain() #todo: for keeping objects alive, is this necessary? (SCPreferences fails without it)

        return super(CFString, cls).from_param(c_class_object)

    @classmethod
    def createCopy(cls, pointer):
        return CFString._create_copy(None, pointer)



Prototype.registerObjectType("CFString", CFString)
CFString._create_with_c_string = CFFunction("c_void_p CFStringCreateWithCString(c_void_p, char*, CFIndex)")
CFString._create_copy = CFFunction("CFStringObj CFStringCreateCopy(c_void_p, c_void_p)")
CFString._length = CFFunction("CFIndex CFStringGetLength(CFString)")
CFString._max_size_for_encoding = CFFunction("CFIndex CFStringGetMaximumSizeForEncoding(CFIndex, int)")
CFString._char_at = CFFunction("UniChar CFStringGetCharacterAtIndex(CFString, CFIndex)")
CFString._chars = CFFunction("char* CFStringGetCStringPtr(c_void_p, int)")
CFString._GetCString = CFFunction("bool CFStringGetCString(c_void_p, char*, CFIndex, int)")
CFString._compare = CFFunction("int CFStringCompare(CFString, CFString, int)")