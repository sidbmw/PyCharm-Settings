# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.146
# no doc

# imports
import sip as __sip


class QMetaEnum(__sip.simplewrapper):
    """
    QMetaEnum()
    QMetaEnum(QMetaEnum)
    """
    def isFlag(self): # real signature unknown; restored from __doc__
        """ isFlag(self) -> bool """
        return False

    def isScoped(self): # real signature unknown; restored from __doc__
        """ isScoped(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def key(self, p_int): # real signature unknown; restored from __doc__
        """ key(self, int) -> str """
        return ""

    def keyCount(self): # real signature unknown; restored from __doc__
        """ keyCount(self) -> int """
        return 0

    def keysToValue(self, p_str): # real signature unknown; restored from __doc__
        """ keysToValue(self, str) -> Tuple[int, bool] """
        pass

    def keyToValue(self, p_str): # real signature unknown; restored from __doc__
        """ keyToValue(self, str) -> Tuple[int, bool] """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def scope(self): # real signature unknown; restored from __doc__
        """ scope(self) -> str """
        return ""

    def value(self, p_int): # real signature unknown; restored from __doc__
        """ value(self, int) -> int """
        return 0

    def valueToKey(self, p_int): # real signature unknown; restored from __doc__
        """ valueToKey(self, int) -> str """
        return ""

    def valueToKeys(self, p_int): # real signature unknown; restored from __doc__
        """ valueToKeys(self, int) -> QByteArray """
        return QByteArray

    def __init__(self, QMetaEnum=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



