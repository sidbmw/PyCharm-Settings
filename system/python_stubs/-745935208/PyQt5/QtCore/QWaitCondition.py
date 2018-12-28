# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.146
# no doc

# imports
import sip as __sip


class QWaitCondition(__sip.simplewrapper):
    """ QWaitCondition() """
    def wait(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        wait(self, QMutex, msecs: int = ULONG_MAX) -> bool
        wait(self, QReadWriteLock, msecs: int = ULONG_MAX) -> bool
        """
        return False

    def wakeAll(self): # real signature unknown; restored from __doc__
        """ wakeAll(self) """
        pass

    def wakeOne(self): # real signature unknown; restored from __doc__
        """ wakeOne(self) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



