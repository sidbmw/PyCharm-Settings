# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.146
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QTranslator(QObject):
    """ QTranslator(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, str, directory: str = '', searchDelimiters: str = '', suffix: str = '') -> bool
        load(self, QLocale, str, prefix: str = '', directory: str = '', suffix: str = '') -> bool
        """
        return False

    def loadFromData(self, bytes, directory=''): # real signature unknown; restored from __doc__
        """ loadFromData(self, bytes, directory: str = '') -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, p_str, p_str_1, disambiguation=None, n=-1): # real signature unknown; restored from __doc__
        """ translate(self, str, str, disambiguation: str = None, n: int = -1) -> str """
        return ""

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


