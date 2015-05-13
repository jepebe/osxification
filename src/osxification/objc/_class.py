import ctypes
from osxification.c import Prototype, STDLIB
from osxification.objc import ObjCFunction, Method, Selector
from osxification.objc._identifier import Identifier


class Class(ctypes.c_void_p):

    @staticmethod
    def _asReturnType(value):
        if value is None or value == 0:
            return None
        return Class(value)

    def getName(self):
        """
        :rtype: str
        """
        return Class._getName(self)

    def getSuperClass(self):
        """
        :rtype: Class
        """
        return Class._getSuperclass(self)

    def getMethodList(self):
        """
        :rtype: list of Method
        """
        count = ctypes.c_uint(0)

        array = Class._getMethodList(self, ctypes.byref(count))

        methods = []
        for index in range(count.value):
            method = Method(array[index])
            # print(method)
            methods.append(method)

        STDLIB.free(array)
        return methods


    def addMethod(self, selector, function, types="@@:"):
        """
        :type selector: str or Selector
        :type function: python function
        :type types: str
        :rtype: bool
        """
        if isinstance(selector, (str, unicode)):
            selector = Selector.registerName(selector)

        return_type = Identifier
        if types[0] == "i":
            return_type = ctypes.c_int

        c_func_type = ctypes.CFUNCTYPE(return_type, ctypes.c_void_p, ctypes.c_void_p)

        c_function = c_func_type(function)
        c_function.func_type = c_func_type

        self.c_function = c_function #Function caching should be solved better


        return Class._addMethod(self, selector, c_function, types)

    def __eq__(self, other):
        if isinstance(other, (Class, ctypes.c_void_p)):
            return self.value == other.value
        return False


Prototype.registerType("Class", Class)

Class._getName = ObjCFunction("char* class_getName(Class)")
Class._getSuperclass = ObjCFunction("Class class_getSuperclass(Class)")
Class._getMethodList = ObjCFunction("void** class_copyMethodList(Class, uint*)")
Class._addMethod = ObjCFunction("bool class_addMethod(Class, SEL, void*, char*)")
