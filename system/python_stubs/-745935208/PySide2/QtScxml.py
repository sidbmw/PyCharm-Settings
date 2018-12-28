# encoding: utf-8
# module PySide2.QtScxml
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PySide2\QtScxml.pyd
# by generator 1.146
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QScxmlCompiler(__Shiboken.Object):
    # no doc
    def compile(self, *args, **kwargs): # real signature unknown
        pass

    def errors(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def loader(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, *args, **kwargs): # real signature unknown
        pass

    def setLoader(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Loader = None # (!) real value is ''


class QScxmlInvokableServiceFactory(__PySide2_QtCore.QObject):
    # no doc
    def invoke(self, *args, **kwargs): # real signature unknown
        pass

    def invokeInfo(self, *args, **kwargs): # real signature unknown
        pass

    def names(self, *args, **kwargs): # real signature unknown
        pass

    def parameters(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QScxmlDynamicScxmlServiceFactory(QScxmlInvokableServiceFactory):
    # no doc
    def invoke(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QScxmlError(__Shiboken.Object):
    # no doc
    def column(self, *args, **kwargs): # real signature unknown
        pass

    def description(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def line(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QScxmlEvent(__Shiboken.Object):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def delay(self, *args, **kwargs): # real signature unknown
        pass

    def errorMessage(self, *args, **kwargs): # real signature unknown
        pass

    def eventType(self, *args, **kwargs): # real signature unknown
        pass

    def invokeId(self, *args, **kwargs): # real signature unknown
        pass

    def isErrorEvent(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def origin(self, *args, **kwargs): # real signature unknown
        pass

    def originType(self, *args, **kwargs): # real signature unknown
        pass

    def scxmlType(self, *args, **kwargs): # real signature unknown
        pass

    def sendId(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setDelay(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorMessage(self, *args, **kwargs): # real signature unknown
        pass

    def setEventType(self, *args, **kwargs): # real signature unknown
        pass

    def setInvokeId(self, *args, **kwargs): # real signature unknown
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        pass

    def setOrigin(self, *args, **kwargs): # real signature unknown
        pass

    def setOriginType(self, *args, **kwargs): # real signature unknown
        pass

    def setSendId(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    EventType = None # (!) real value is ''
    ExternalEvent = None # (!) real value is ''
    InternalEvent = None # (!) real value is ''
    PlatformEvent = None # (!) real value is ''


class QScxmlExecutableContent(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AssignmentInfo = None # (!) real value is ''
    EvaluatorInfo = None # (!) real value is ''
    ForeachInfo = None # (!) real value is ''
    InvokeInfo = None # (!) real value is ''
    ParameterInfo = None # (!) real value is ''


class QScxmlInvokableService(__PySide2_QtCore.QObject):
    # no doc
    def id(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def parentStateMachine(self, *args, **kwargs): # real signature unknown
        pass

    def postEvent(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QScxmlStateMachine(__PySide2_QtCore.QObject):
    # no doc
    def activeStateNames(self, *args, **kwargs): # real signature unknown
        pass

    def cancelDelayedEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectToEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectToState(self, *args, **kwargs): # real signature unknown
        pass

    def dataModelChanged(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def fromData(self, *args, **kwargs): # real signature unknown
        pass

    def fromFile(self, *args, **kwargs): # real signature unknown
        pass

    def init(self, *args, **kwargs): # real signature unknown
        pass

    def initializedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def initialValues(self, *args, **kwargs): # real signature unknown
        pass

    def initialValuesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def invokedServices(self, *args, **kwargs): # real signature unknown
        pass

    def invokedServicesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isDispatchableTarget(self, *args, **kwargs): # real signature unknown
        pass

    def isInitialized(self, *args, **kwargs): # real signature unknown
        pass

    def isInvoked(self, *args, **kwargs): # real signature unknown
        pass

    def isRunning(self, *args, **kwargs): # real signature unknown
        pass

    def loader(self, *args, **kwargs): # real signature unknown
        pass

    def loaderChanged(self, *args, **kwargs): # real signature unknown
        pass

    def log(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def parseErrors(self, *args, **kwargs): # real signature unknown
        pass

    def reachedStableState(self, *args, **kwargs): # real signature unknown
        pass

    def runningChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sessionId(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialValues(self, *args, **kwargs): # real signature unknown
        pass

    def setLoader(self, *args, **kwargs): # real signature unknown
        pass

    def setRunning(self, *args, **kwargs): # real signature unknown
        pass

    def setTableData(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stateNames(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def submitEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tableData(self, *args, **kwargs): # real signature unknown
        pass

    def tableDataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QScxmlStaticScxmlServiceFactory(QScxmlInvokableServiceFactory):
    # no doc
    def invoke(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QScxmlTableData(__Shiboken.Object):
    # no doc
    def assignmentInfo(self, *args, **kwargs): # real signature unknown
        pass

    def dataNames(self, *args, **kwargs): # real signature unknown
        pass

    def evaluatorInfo(self, *args, **kwargs): # real signature unknown
        pass

    def foreachInfo(self, *args, **kwargs): # real signature unknown
        pass

    def initialSetup(self, *args, **kwargs): # real signature unknown
        pass

    def instructions(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def serviceFactory(self, *args, **kwargs): # real signature unknown
        pass

    def stateMachineTable(self, *args, **kwargs): # real signature unknown
        pass

    def string(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

