# encoding: utf-8
# module PySide2.QtWinExtras
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PySide2\QtWinExtras.pyd
# by generator 1.146
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QWinEvent(__PySide2_QtCore.QEvent):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    ColorizationChange = 65535
    CompositionChange = 65534
    TaskbarButtonCreated = 65533
    ThemeChange = 65532


class QWinColorizationChangeEvent(QWinEvent):
    # no doc
    def color(self, *args, **kwargs): # real signature unknown
        pass

    def opaqueBlend(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWinCompositionChangeEvent(QWinEvent):
    # no doc
    def isCompositionEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWinJumpList(__PySide2_QtCore.QObject):
    # no doc
    def addCategory(self, *args, **kwargs): # real signature unknown
        pass

    def categories(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def frequent(self, *args, **kwargs): # real signature unknown
        pass

    def identifier(self, *args, **kwargs): # real signature unknown
        pass

    def recent(self, *args, **kwargs): # real signature unknown
        pass

    def setIdentifier(self, *args, **kwargs): # real signature unknown
        pass

    def tasks(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QWinJumpListCategory(__Shiboken.Object):
    # no doc
    def addDestination(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, *args, **kwargs): # real signature unknown
        pass

    def addLink(self, *args, **kwargs): # real signature unknown
        pass

    def addSeparator(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, *args, **kwargs): # real signature unknown
        pass

    def setTitle(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, *args, **kwargs): # real signature unknown
        pass

    def title(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Custom = None # (!) real value is ''
    Frequent = None # (!) real value is ''
    Recent = None # (!) real value is ''
    Tasks = None # (!) real value is ''
    Type = None # (!) real value is ''


class QWinJumpListItem(__Shiboken.Object):
    # no doc
    def arguments(self, *args, **kwargs): # real signature unknown
        pass

    def description(self, *args, **kwargs): # real signature unknown
        pass

    def filePath(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self, *args, **kwargs): # real signature unknown
        pass

    def setArguments(self, *args, **kwargs): # real signature unknown
        pass

    def setDescription(self, *args, **kwargs): # real signature unknown
        pass

    def setFilePath(self, *args, **kwargs): # real signature unknown
        pass

    def setIcon(self, *args, **kwargs): # real signature unknown
        pass

    def setTitle(self, *args, **kwargs): # real signature unknown
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        pass

    def setWorkingDirectory(self, *args, **kwargs): # real signature unknown
        pass

    def title(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def workingDirectory(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Destination = None # (!) real value is ''
    Link = None # (!) real value is ''
    Separator = None # (!) real value is ''
    Type = None # (!) real value is ''


class QWinTaskbarButton(__PySide2_QtCore.QObject):
    # no doc
    def clearOverlayIcon(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def overlayAccessibleDescription(self, *args, **kwargs): # real signature unknown
        pass

    def overlayIcon(self, *args, **kwargs): # real signature unknown
        pass

    def progress(self, *args, **kwargs): # real signature unknown
        pass

    def setOverlayAccessibleDescription(self, *args, **kwargs): # real signature unknown
        pass

    def setOverlayIcon(self, *args, **kwargs): # real signature unknown
        pass

    def setWindow(self, *args, **kwargs): # real signature unknown
        pass

    def window(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QWinTaskbarProgress(__PySide2_QtCore.QObject):
    # no doc
    def hide(self, *args, **kwargs): # real signature unknown
        pass

    def isPaused(self, *args, **kwargs): # real signature unknown
        pass

    def isStopped(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self, *args, **kwargs): # real signature unknown
        pass

    def maximum(self, *args, **kwargs): # real signature unknown
        pass

    def maximumChanged(self, *args, **kwargs): # real signature unknown
        pass

    def minimum(self, *args, **kwargs): # real signature unknown
        pass

    def minimumChanged(self, *args, **kwargs): # real signature unknown
        pass

    def pause(self, *args, **kwargs): # real signature unknown
        pass

    def pausedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setMaximum(self, *args, **kwargs): # real signature unknown
        pass

    def setMinimum(self, *args, **kwargs): # real signature unknown
        pass

    def setPaused(self, *args, **kwargs): # real signature unknown
        pass

    def setRange(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, *args, **kwargs): # real signature unknown
        pass

    def show(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def stoppedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def visibilityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QWinThumbnailToolBar(__PySide2_QtCore.QObject):
    # no doc
    def addButton(self, *args, **kwargs): # real signature unknown
        pass

    def buttons(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def iconicLivePreviewPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def iconicLivePreviewPixmapRequested(self, *args, **kwargs): # real signature unknown
        pass

    def iconicPixmapNotificationsEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def iconicThumbnailPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def iconicThumbnailPixmapRequested(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, *args, **kwargs): # real signature unknown
        pass

    def setButtons(self, *args, **kwargs): # real signature unknown
        pass

    def setIconicLivePreviewPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def setIconicPixmapNotificationsEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def setIconicThumbnailPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def setWindow(self, *args, **kwargs): # real signature unknown
        pass

    def window(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QWinThumbnailToolButton(__PySide2_QtCore.QObject):
    # no doc
    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def click(self, *args, **kwargs): # real signature unknown
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        pass

    def dismissOnClick(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self, *args, **kwargs): # real signature unknown
        pass

    def isEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def isFlat(self, *args, **kwargs): # real signature unknown
        pass

    def isInteractive(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self, *args, **kwargs): # real signature unknown
        pass

    def setDismissOnClick(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def setFlat(self, *args, **kwargs): # real signature unknown
        pass

    def setIcon(self, *args, **kwargs): # real signature unknown
        pass

    def setInteractive(self, *args, **kwargs): # real signature unknown
        pass

    def setToolTip(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self, *args, **kwargs): # real signature unknown
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

