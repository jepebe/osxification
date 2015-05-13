import ctypes
from osxification.c import Prototype
from osxification.objc import ObjCFunction, Selector


class Method(ctypes.c_void_p):

    def getName(self):
        """
        :rtype: Selector
        """
        return Method._getName(self)

    def getReturnType(self):
        """
        :rtype:
        """
        return Method._copyReturnType(self)

    def getArguments(self):
        """
        :rtype: list of str
        """
        argument_count = Method._getArgumentCount(self)
        arguments = []
        for index in range(argument_count):
            argument = Method._copyArgumentType(self, index)
            arguments.append(argument)

        return arguments

    def getTypeEncoding(self):
        """
        :rtype: str
        """
        return Method._getTypeEncoding(self)

    def __str__(self):
        name_selector = self.getName()
        name = Selector.getName(name_selector)
        return_type = self.getReturnType()
        arguments = self.getArguments()
        arguments = ", ".join(arguments)

        return "%s %s(%s)" % (return_type, name, arguments)

Prototype.registerType("Method", Method)

Method._getName = ObjCFunction("SEL method_getName(Method)")
Method._copyReturnType = ObjCFunction("char* method_copyReturnType(Method)")
Method._getArgumentCount = ObjCFunction("uint method_getNumberOfArguments(Method)")
Method._copyArgumentType = ObjCFunction("char* method_copyArgumentType(Method, uint)")
Method._getTypeEncoding = ObjCFunction("char* method_getTypeEncoding(Method)")