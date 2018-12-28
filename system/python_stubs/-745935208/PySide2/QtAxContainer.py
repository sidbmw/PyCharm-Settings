# encoding: utf-8
# module PySide2.QtAxContainer
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PySide2\QtAxContainer.pyd
# by generator 1.146
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtWidgets as __PySide2_QtWidgets
import Shiboken as __Shiboken


# no functions
# classes

class QAxBase(__Shiboken.Object):
    # no doc
    def argumentsToList(self, *args, **kwargs): # real signature unknown
        pass

    def asVariant(self, *args, **kwargs): # real signature unknown
        pass

    def className(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def control(self, *args, **kwargs): # real signature unknown
        pass

    def disableClassInfo(self, *args, **kwargs): # real signature unknown
        pass

    def disableEventSink(self, *args, **kwargs): # real signature unknown
        pass

    def disableMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def dynamicCall(self, *args, **kwargs): # real signature unknown
        pass

    def fallbackMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def generateDocumentation(self, *args, **kwargs): # real signature unknown
        pass

    def indexOfVerb(self, *args, **kwargs): # real signature unknown
        pass

    def initializeFrom(self, *args, **kwargs): # real signature unknown
        pass

    def internalRelease(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def propertyBag(self, *args, **kwargs): # real signature unknown
        pass

    def propertyWritable(self, *args, **kwargs): # real signature unknown
        pass

    def qObject(self, *args, **kwargs): # real signature unknown
        pass

    def querySubObject(self, *args, **kwargs): # real signature unknown
        pass

    def setControl(self, *args, **kwargs): # real signature unknown
        pass

    def setPropertyBag(self, *args, **kwargs): # real signature unknown
        pass

    def setPropertyWritable(self, *args, **kwargs): # real signature unknown
        pass

    def verbs(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass


class QAxObject(__PySide2_QtCore.QObject, QAxBase):
    # no doc
    def className(self, *args, **kwargs): # real signature unknown
        pass

    def doVerb(self, *args, **kwargs): # real signature unknown
        pass

    def fallbackMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def qObject(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAxScript(__PySide2_QtCore.QObject):
    # no doc
    def call(self, *args, **kwargs): # real signature unknown
        pass

    def entered(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def functions(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def scriptCode(self, *args, **kwargs): # real signature unknown
        pass

    def scriptEngine(self, *args, **kwargs): # real signature unknown
        pass

    def scriptName(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    FunctionFlags = None # (!) real value is ''
    FunctionNames = None # (!) real value is ''
    FunctionSignatures = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''


class QAxScriptEngine(QAxObject):
    # no doc
    def addItem(self, *args, **kwargs): # real signature unknown
        pass

    def hasIntrospection(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def scriptLanguage(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAxScriptManager(__PySide2_QtCore.QObject):
    # no doc
    def addObject(self, *args, **kwargs): # real signature unknown
        pass

    def call(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def functions(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def registerEngine(self, *args, **kwargs): # real signature unknown
        pass

    def script(self, *args, **kwargs): # real signature unknown
        pass

    def scriptFileFilter(self, *args, **kwargs): # real signature unknown
        pass

    def scriptNames(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAxSelect(__PySide2_QtWidgets.QDialog):
    # no doc
    def clsid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAxWidget(__PySide2_QtWidgets.QWidget, QAxBase):
    # no doc
    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def className(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def createHostWindow(self, *args, **kwargs): # real signature unknown
        pass

    def doVerb(self, *args, **kwargs): # real signature unknown
        pass

    def fallbackMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def qObject(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def translateKeyEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

