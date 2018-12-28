# encoding: utf-8
# module PySide2.QtWebEngineCore
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PySide2\QtWebEngineCore.pyd
# by generator 1.146
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QWebEngineCookieStore(__PySide2_QtCore.QObject):
    # no doc
    def cookieAdded(self, *args, **kwargs): # real signature unknown
        pass

    def cookieRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def deleteAllCookies(self, *args, **kwargs): # real signature unknown
        pass

    def deleteSessionCookies(self, *args, **kwargs): # real signature unknown
        pass

    def loadAllCookies(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QWebEngineHttpRequest(__Shiboken.Object):
    # no doc
    def hasHeader(self, *args, **kwargs): # real signature unknown
        pass

    def header(self, *args, **kwargs): # real signature unknown
        pass

    def headers(self, *args, **kwargs): # real signature unknown
        pass

    def method(self, *args, **kwargs): # real signature unknown
        pass

    def postData(self, *args, **kwargs): # real signature unknown
        pass

    def postRequest(self, *args, **kwargs): # real signature unknown
        pass

    def setHeader(self, *args, **kwargs): # real signature unknown
        pass

    def setMethod(self, *args, **kwargs): # real signature unknown
        pass

    def setPostData(self, *args, **kwargs): # real signature unknown
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        pass

    def swap(self, *args, **kwargs): # real signature unknown
        pass

    def unsetHeader(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    Get = None # (!) real value is ''
    Method = None # (!) real value is ''
    Post = None # (!) real value is ''
    __hash__ = None


class QWebEngineUrlRequestInfo(__Shiboken.Object):
    # no doc
    def block(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def firstPartyUrl(self, *args, **kwargs): # real signature unknown
        pass

    def navigationType(self, *args, **kwargs): # real signature unknown
        pass

    def redirect(self, *args, **kwargs): # real signature unknown
        pass

    def requestMethod(self, *args, **kwargs): # real signature unknown
        pass

    def requestUrl(self, *args, **kwargs): # real signature unknown
        pass

    def resourceType(self, *args, **kwargs): # real signature unknown
        pass

    def setHttpHeader(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    NavigationType = None # (!) real value is ''
    NavigationTypeBackForward = None # (!) real value is ''
    NavigationTypeFormSubmitted = None # (!) real value is ''
    NavigationTypeLink = None # (!) real value is ''
    NavigationTypeOther = None # (!) real value is ''
    NavigationTypeReload = None # (!) real value is ''
    NavigationTypeTyped = None # (!) real value is ''
    ResourceType = None # (!) real value is ''
    ResourceTypeCspReport = None # (!) real value is ''
    ResourceTypeFavicon = None # (!) real value is ''
    ResourceTypeFontResource = None # (!) real value is ''
    ResourceTypeImage = None # (!) real value is ''
    ResourceTypeLast = None # (!) real value is ''
    ResourceTypeMainFrame = None # (!) real value is ''
    ResourceTypeMedia = None # (!) real value is ''
    ResourceTypeObject = None # (!) real value is ''
    ResourceTypePing = None # (!) real value is ''
    ResourceTypePluginResource = None # (!) real value is ''
    ResourceTypePrefetch = None # (!) real value is ''
    ResourceTypeScript = None # (!) real value is ''
    ResourceTypeServiceWorker = None # (!) real value is ''
    ResourceTypeSharedWorker = None # (!) real value is ''
    ResourceTypeStylesheet = None # (!) real value is ''
    ResourceTypeSubFrame = None # (!) real value is ''
    ResourceTypeSubResource = None # (!) real value is ''
    ResourceTypeUnknown = None # (!) real value is ''
    ResourceTypeWorker = None # (!) real value is ''
    ResourceTypeXhr = None # (!) real value is ''


class QWebEngineUrlRequestInterceptor(__PySide2_QtCore.QObject):
    # no doc
    def interceptRequest(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QWebEngineUrlRequestJob(__PySide2_QtCore.QObject):
    # no doc
    def fail(self, *args, **kwargs): # real signature unknown
        pass

    def initiator(self, *args, **kwargs): # real signature unknown
        pass

    def redirect(self, *args, **kwargs): # real signature unknown
        pass

    def reply(self, *args, **kwargs): # real signature unknown
        pass

    def requestMethod(self, *args, **kwargs): # real signature unknown
        pass

    def requestUrl(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Error = None # (!) real value is ''
    NoError = None # (!) real value is ''
    RequestAborted = None # (!) real value is ''
    RequestDenied = None # (!) real value is ''
    RequestFailed = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    UrlInvalid = None # (!) real value is ''
    UrlNotFound = None # (!) real value is ''


class QWebEngineUrlSchemeHandler(__PySide2_QtCore.QObject):
    # no doc
    def requestStarted(self, *args, **kwargs): # real signature unknown
        pass

    def _q_destroyedUrlSchemeHandler(self, *args, **kwargs): # real signature unknown
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

