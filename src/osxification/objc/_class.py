import ctypes
from osxification.c import Prototype, STDLIB
from osxification.objc import ObjCFunction, Method, Selector, Identifier


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

    def addProtocol(self, protocol):
        """ :rtype: bool """
        return Class._addProtocol(self, protocol)

    def respondsToSelector(self, selector):
        """ :rtype: bool """
        selector = Selector.checkSelector(selector)
        return Class._respondsToSelector(self, selector)


    def addMethod(self, selector, function, types="@@:"):
        """
        :type selector: str or Selector
        :type function: python function
        :type types: str
        :rtype: bool
        """
        selector = Selector.checkSelector(selector)

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

    def __str__(self):
        return self.getName()

    def __repr__(self):
        return "<ObjectiveC Class with name: %s>" % self.getName()


Prototype.registerType("Class", Class)

Class._getName = ObjCFunction("char* class_getName(Class)")
Class._getSuperclass = ObjCFunction("Class class_getSuperclass(Class)")
Class._getMethodList = ObjCFunction("void** class_copyMethodList(Class, uint*)")
Class._addMethod = ObjCFunction("bool class_addMethod(Class, SEL, void*, char*)")
Class._addProtocol = ObjCFunction("bool class_addProtocol(Class, Protocol)")
Class._respondsToSelector = ObjCFunction("bool class_respondsToSelector(Class, SEL)")
