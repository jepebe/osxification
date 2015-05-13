import ctypes
import ctypes.util
from .prototype import Prototype, PrototypeError
from .enum import Enum

STDLIB = ctypes.cdll.LoadLibrary(ctypes.util.find_library("stdlib"))


