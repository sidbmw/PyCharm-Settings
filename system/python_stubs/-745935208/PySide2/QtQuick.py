# encoding: utf-8
# module PySide2.QtQuick
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PySide2\QtQuick.pyd
# by generator 1.146
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import PySide2.QtQml as __PySide2_QtQml
import Shiboken as __Shiboken


# no functions
# classes

class QQuickImageProvider(__PySide2_QtQml.QQmlImageProviderBase):
    # no doc
    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def imageType(self, *args, **kwargs): # real signature unknown
        pass

    def requestImage(self, *args, **kwargs): # real signature unknown
        pass

    def requestPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def requestTexture(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QQuickAsyncImageProvider(QQuickImageProvider):
    # no doc
    def requestImageResponse(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QQuickItem(__PySide2_QtCore.QObject, __PySide2_QtQml.QQmlParserStatus):
    # no doc
    def acceptedMouseButtons(self, *args, **kwargs): # real signature unknown
        pass

    def acceptHoverEvents(self, *args, **kwargs): # real signature unknown
        pass

    def acceptTouchEvents(self, *args, **kwargs): # real signature unknown
        pass

    def activeFocusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def activeFocusOnTab(self, *args, **kwargs): # real signature unknown
        pass

    def activeFocusOnTabChanged(self, *args, **kwargs): # real signature unknown
        pass

    def antialiasing(self, *args, **kwargs): # real signature unknown
        pass

    def antialiasingChanged(self, *args, **kwargs): # real signature unknown
        pass

    def baselineOffset(self, *args, **kwargs): # real signature unknown
        pass

    def baselineOffsetChanged(self, *args, **kwargs): # real signature unknown
        pass

    def boundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def childAt(self, *args, **kwargs): # real signature unknown
        pass

    def childItems(self, *args, **kwargs): # real signature unknown
        pass

    def childMouseEventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def childrenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRect(self, *args, **kwargs): # real signature unknown
        pass

    def childrenRectChanged(self, *args, **kwargs): # real signature unknown
        pass

    def classBegin(self, *args, **kwargs): # real signature unknown
        pass

    def clip(self, *args, **kwargs): # real signature unknown
        pass

    def clipChanged(self, *args, **kwargs): # real signature unknown
        pass

    def clipRect(self, *args, **kwargs): # real signature unknown
        pass

    def componentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def containmentMask(self, *args, **kwargs): # real signature unknown
        pass

    def containmentMaskChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def cursor(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChanged(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def filtersChildMouseEvents(self, *args, **kwargs): # real signature unknown
        pass

    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def focusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def forceActiveFocus(self, *args, **kwargs): # real signature unknown
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def grabMouse(self, *args, **kwargs): # real signature unknown
        pass

    def grabToImage(self, *args, **kwargs): # real signature unknown
        pass

    def grabTouchPoints(self, *args, **kwargs): # real signature unknown
        pass

    def hasActiveFocus(self, *args, **kwargs): # real signature unknown
        pass

    def hasFocus(self, *args, **kwargs): # real signature unknown
        pass

    def height(self, *args, **kwargs): # real signature unknown
        pass

    def heightChanged(self, *args, **kwargs): # real signature unknown
        pass

    def heightValid(self, *args, **kwargs): # real signature unknown
        pass

    def hoverEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def hoverMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def implicitHeight(self, *args, **kwargs): # real signature unknown
        pass

    def implicitHeightChanged(self, *args, **kwargs): # real signature unknown
        pass

    def implicitWidth(self, *args, **kwargs): # real signature unknown
        pass

    def implicitWidthChanged(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodQuery(self, *args, **kwargs): # real signature unknown
        pass

    def isAncestorOf(self, *args, **kwargs): # real signature unknown
        pass

    def isComponentComplete(self, *args, **kwargs): # real signature unknown
        pass

    def isEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def isFocusScope(self, *args, **kwargs): # real signature unknown
        pass

    def isTextureProvider(self, *args, **kwargs): # real signature unknown
        pass

    def isUnderMouse(self, *args, **kwargs): # real signature unknown
        pass

    def isVisible(self, *args, **kwargs): # real signature unknown
        pass

    def itemTransform(self, *args, **kwargs): # real signature unknown
        pass

    def keepMouseGrab(self, *args, **kwargs): # real signature unknown
        pass

    def keepTouchGrab(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mapFromGlobal(self, *args, **kwargs): # real signature unknown
        pass

    def mapFromItem(self, *args, **kwargs): # real signature unknown
        pass

    def mapFromScene(self, *args, **kwargs): # real signature unknown
        pass

    def mapRectFromItem(self, *args, **kwargs): # real signature unknown
        pass

    def mapRectFromScene(self, *args, **kwargs): # real signature unknown
        pass

    def mapRectToItem(self, *args, **kwargs): # real signature unknown
        pass

    def mapRectToScene(self, *args, **kwargs): # real signature unknown
        pass

    def mapToGlobal(self, *args, **kwargs): # real signature unknown
        pass

    def mapToItem(self, *args, **kwargs): # real signature unknown
        pass

    def mapToScene(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseUngrabEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nextItemInFocusChain(self, *args, **kwargs): # real signature unknown
        pass

    def opacity(self, *args, **kwargs): # real signature unknown
        pass

    def opacityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def parentChanged(self, *args, **kwargs): # real signature unknown
        pass

    def parentItem(self, *args, **kwargs): # real signature unknown
        pass

    def polish(self, *args, **kwargs): # real signature unknown
        pass

    def position(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self, *args, **kwargs): # real signature unknown
        pass

    def resetAntialiasing(self, *args, **kwargs): # real signature unknown
        pass

    def resetHeight(self, *args, **kwargs): # real signature unknown
        pass

    def resetWidth(self, *args, **kwargs): # real signature unknown
        pass

    def rotation(self, *args, **kwargs): # real signature unknown
        pass

    def rotationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def scale(self, *args, **kwargs): # real signature unknown
        pass

    def scaleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def scopedFocusItem(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptedMouseButtons(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptHoverEvents(self, *args, **kwargs): # real signature unknown
        pass

    def setAcceptTouchEvents(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveFocusOnTab(self, *args, **kwargs): # real signature unknown
        pass

    def setAntialiasing(self, *args, **kwargs): # real signature unknown
        pass

    def setBaselineOffset(self, *args, **kwargs): # real signature unknown
        pass

    def setClip(self, *args, **kwargs): # real signature unknown
        pass

    def setContainmentMask(self, *args, **kwargs): # real signature unknown
        pass

    def setCursor(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def setFiltersChildMouseEvents(self, *args, **kwargs): # real signature unknown
        pass

    def setFlag(self, *args, **kwargs): # real signature unknown
        pass

    def setFlags(self, *args, **kwargs): # real signature unknown
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown
        pass

    def setHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setImplicitHeight(self, *args, **kwargs): # real signature unknown
        pass

    def setImplicitSize(self, *args, **kwargs): # real signature unknown
        pass

    def setImplicitWidth(self, *args, **kwargs): # real signature unknown
        pass

    def setKeepMouseGrab(self, *args, **kwargs): # real signature unknown
        pass

    def setKeepTouchGrab(self, *args, **kwargs): # real signature unknown
        pass

    def setOpacity(self, *args, **kwargs): # real signature unknown
        pass

    def setParentItem(self, *args, **kwargs): # real signature unknown
        pass

    def setPosition(self, *args, **kwargs): # real signature unknown
        pass

    def setRotation(self, *args, **kwargs): # real signature unknown
        pass

    def setScale(self, *args, **kwargs): # real signature unknown
        pass

    def setSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSmooth(self, *args, **kwargs): # real signature unknown
        pass

    def setState(self, *args, **kwargs): # real signature unknown
        pass

    def setTransformOrigin(self, *args, **kwargs): # real signature unknown
        pass

    def setTransformOriginPoint(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, *args, **kwargs): # real signature unknown
        pass

    def setWidth(self, *args, **kwargs): # real signature unknown
        pass

    def setX(self, *args, **kwargs): # real signature unknown
        pass

    def setY(self, *args, **kwargs): # real signature unknown
        pass

    def setZ(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def smooth(self, *args, **kwargs): # real signature unknown
        pass

    def smoothChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stackAfter(self, *args, **kwargs): # real signature unknown
        pass

    def stackBefore(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textureProvider(self, *args, **kwargs): # real signature unknown
        pass

    def touchEvent(self, *args, **kwargs): # real signature unknown
        pass

    def touchUngrabEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transformOrigin(self, *args, **kwargs): # real signature unknown
        pass

    def transformOriginChanged(self, *args, **kwargs): # real signature unknown
        pass

    def transformOriginPoint(self, *args, **kwargs): # real signature unknown
        pass

    def ungrabMouse(self, *args, **kwargs): # real signature unknown
        pass

    def ungrabTouchPoints(self, *args, **kwargs): # real signature unknown
        pass

    def unsetCursor(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def updateInputMethod(self, *args, **kwargs): # real signature unknown
        pass

    def updatePaintNode(self, *args, **kwargs): # real signature unknown
        pass

    def updatePolish(self, *args, **kwargs): # real signature unknown
        pass

    def visibleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def visibleChildrenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def width(self, *args, **kwargs): # real signature unknown
        pass

    def widthChanged(self, *args, **kwargs): # real signature unknown
        pass

    def widthValid(self, *args, **kwargs): # real signature unknown
        pass

    def window(self, *args, **kwargs): # real signature unknown
        pass

    def windowChanged(self, *args, **kwargs): # real signature unknown
        pass

    def windowDeactivateEvent(self, *args, **kwargs): # real signature unknown
        pass

    def x(self, *args, **kwargs): # real signature unknown
        pass

    def xChanged(self, *args, **kwargs): # real signature unknown
        pass

    def y(self, *args, **kwargs): # real signature unknown
        pass

    def yChanged(self, *args, **kwargs): # real signature unknown
        pass

    def z(self, *args, **kwargs): # real signature unknown
        pass

    def zChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Bottom = None # (!) real value is ''
    BottomLeft = None # (!) real value is ''
    BottomRight = None # (!) real value is ''
    Center = None # (!) real value is ''
    Flag = None # (!) real value is ''
    Flags = None # (!) real value is ''
    ItemAcceptsDrops = None # (!) real value is ''
    ItemAcceptsInputMethod = None # (!) real value is ''
    ItemActiveFocusHasChanged = None # (!) real value is ''
    ItemAntialiasingHasChanged = None # (!) real value is ''
    ItemChange = None # (!) real value is ''
    ItemChildAddedChange = None # (!) real value is ''
    ItemChildRemovedChange = None # (!) real value is ''
    ItemClipsChildrenToShape = None # (!) real value is ''
    ItemDevicePixelRatioHasChanged = None # (!) real value is ''
    ItemEnabledHasChanged = None # (!) real value is ''
    ItemHasContents = None # (!) real value is ''
    ItemIsFocusScope = None # (!) real value is ''
    ItemOpacityHasChanged = None # (!) real value is ''
    ItemParentHasChanged = None # (!) real value is ''
    ItemRotationHasChanged = None # (!) real value is ''
    ItemSceneChange = None # (!) real value is ''
    ItemVisibleHasChanged = None # (!) real value is ''
    Left = None # (!) real value is ''
    Right = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    Top = None # (!) real value is ''
    TopLeft = None # (!) real value is ''
    TopRight = None # (!) real value is ''
    TransformOrigin = None # (!) real value is ''
    UpdatePaintNodeData = None # (!) real value is ''


class QQuickFramebufferObject(QQuickItem):
    # no doc
    def createRenderer(self, *args, **kwargs): # real signature unknown
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isTextureProvider(self, *args, **kwargs): # real signature unknown
        pass

    def mirrorVertically(self, *args, **kwargs): # real signature unknown
        pass

    def mirrorVerticallyChanged(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self, *args, **kwargs): # real signature unknown
        pass

    def setMirrorVertically(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureFollowsItemSize(self, *args, **kwargs): # real signature unknown
        pass

    def textureFollowsItemSize(self, *args, **kwargs): # real signature unknown
        pass

    def textureFollowsItemSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textureProvider(self, *args, **kwargs): # real signature unknown
        pass

    def updatePaintNode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Renderer = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''


class QQuickImageResponse(__PySide2_QtCore.QObject):
    # no doc
    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def textureFactory(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QQuickItemGrabResult(__PySide2_QtCore.QObject):
    # no doc
    def event(self, *args, **kwargs): # real signature unknown
        pass

    def image(self, *args, **kwargs): # real signature unknown
        pass

    def ready(self, *args, **kwargs): # real signature unknown
        pass

    def saveToFile(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QQuickPaintedItem(QQuickItem):
    # no doc
    def antialiasing(self, *args, **kwargs): # real signature unknown
        pass

    def contentsBoundingRect(self, *args, **kwargs): # real signature unknown
        pass

    def contentsScale(self, *args, **kwargs): # real signature unknown
        pass

    def contentsScaleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contentsSize(self, *args, **kwargs): # real signature unknown
        pass

    def contentsSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def fillColor(self, *args, **kwargs): # real signature unknown
        pass

    def fillColorChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isTextureProvider(self, *args, **kwargs): # real signature unknown
        pass

    def mipmap(self, *args, **kwargs): # real signature unknown
        pass

    def opaquePainting(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, *args, **kwargs): # real signature unknown
        pass

    def performanceHints(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self, *args, **kwargs): # real signature unknown
        pass

    def renderTarget(self, *args, **kwargs): # real signature unknown
        pass

    def renderTargetChanged(self, *args, **kwargs): # real signature unknown
        pass

    def resetContentsSize(self, *args, **kwargs): # real signature unknown
        pass

    def setAntialiasing(self, *args, **kwargs): # real signature unknown
        pass

    def setContentsScale(self, *args, **kwargs): # real signature unknown
        pass

    def setContentsSize(self, *args, **kwargs): # real signature unknown
        pass

    def setFillColor(self, *args, **kwargs): # real signature unknown
        pass

    def setMipmap(self, *args, **kwargs): # real signature unknown
        pass

    def setOpaquePainting(self, *args, **kwargs): # real signature unknown
        pass

    def setPerformanceHint(self, *args, **kwargs): # real signature unknown
        pass

    def setPerformanceHints(self, *args, **kwargs): # real signature unknown
        pass

    def setRenderTarget(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureSize(self, *args, **kwargs): # real signature unknown
        pass

    def textureProvider(self, *args, **kwargs): # real signature unknown
        pass

    def textureSize(self, *args, **kwargs): # real signature unknown
        pass

    def textureSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def updatePaintNode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    FastFBOResizing = None # (!) real value is ''
    FramebufferObject = None # (!) real value is ''
    Image = None # (!) real value is ''
    InvertedYFramebufferObject = None # (!) real value is ''
    PerformanceHint = None # (!) real value is ''
    PerformanceHints = None # (!) real value is ''
    RenderTarget = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''


class QQuickRenderControl(__PySide2_QtCore.QObject):
    # no doc
    def grab(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def invalidate(self, *args, **kwargs): # real signature unknown
        pass

    def polishItems(self, *args, **kwargs): # real signature unknown
        pass

    def prepareThread(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, *args, **kwargs): # real signature unknown
        pass

    def renderRequested(self, *args, **kwargs): # real signature unknown
        pass

    def renderWindow(self, *args, **kwargs): # real signature unknown
        pass

    def renderWindowFor(self, *args, **kwargs): # real signature unknown
        pass

    def sceneChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sync(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QQuickTextDocument(__PySide2_QtCore.QObject):
    # no doc
    def textDocument(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QQuickTextureFactory(__PySide2_QtCore.QObject):
    # no doc
    def createTexture(self, *args, **kwargs): # real signature unknown
        pass

    def image(self, *args, **kwargs): # real signature unknown
        pass

    def textureByteCount(self, *args, **kwargs): # real signature unknown
        pass

    def textureFactoryForImage(self, *args, **kwargs): # real signature unknown
        pass

    def textureSize(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QQuickTransform(__PySide2_QtCore.QObject):
    # no doc
    def appendToItem(self, *args, **kwargs): # real signature unknown
        pass

    def applyTo(self, *args, **kwargs): # real signature unknown
        pass

    def prependToItem(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QQuickWindow(__PySide2_QtGui.QWindow):
    # no doc
    def accessibleRoot(self, *args, **kwargs): # real signature unknown
        pass

    def activeFocusItem(self, *args, **kwargs): # real signature unknown
        pass

    def activeFocusItemChanged(self, *args, **kwargs): # real signature unknown
        pass

    def afterAnimating(self, *args, **kwargs): # real signature unknown
        pass

    def afterRendering(self, *args, **kwargs): # real signature unknown
        pass

    def afterSynchronizing(self, *args, **kwargs): # real signature unknown
        pass

    def beforeRendering(self, *args, **kwargs): # real signature unknown
        pass

    def beforeSynchronizing(self, *args, **kwargs): # real signature unknown
        pass

    def clearBeforeRendering(self, *args, **kwargs): # real signature unknown
        pass

    def closing(self, *args, **kwargs): # real signature unknown
        pass

    def color(self, *args, **kwargs): # real signature unknown
        pass

    def colorChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contentItem(self, *args, **kwargs): # real signature unknown
        pass

    def createTextureFromId(self, *args, **kwargs): # real signature unknown
        pass

    def createTextureFromImage(self, *args, **kwargs): # real signature unknown
        pass

    def effectiveDevicePixelRatio(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def exposeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusObject(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def frameSwapped(self, *args, **kwargs): # real signature unknown
        pass

    def grabWindow(self, *args, **kwargs): # real signature unknown
        pass

    def hasDefaultAlphaBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def incubationController(self, *args, **kwargs): # real signature unknown
        pass

    def isPersistentOpenGLContext(self, *args, **kwargs): # real signature unknown
        pass

    def isPersistentSceneGraph(self, *args, **kwargs): # real signature unknown
        pass

    def isSceneGraphInitialized(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseGrabberItem(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def openglContext(self, *args, **kwargs): # real signature unknown
        pass

    def openglContextCreated(self, *args, **kwargs): # real signature unknown
        pass

    def releaseResources(self, *args, **kwargs): # real signature unknown
        pass

    def renderTarget(self, *args, **kwargs): # real signature unknown
        pass

    def renderTargetId(self, *args, **kwargs): # real signature unknown
        pass

    def renderTargetSize(self, *args, **kwargs): # real signature unknown
        pass

    def resetOpenGLState(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphAboutToStop(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphBackend(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphError(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphInitialized(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphInvalidated(self, *args, **kwargs): # real signature unknown
        pass

    def scheduleRenderJob(self, *args, **kwargs): # real signature unknown
        pass

    def sendEvent(self, *args, **kwargs): # real signature unknown
        pass

    def setClearBeforeRendering(self, *args, **kwargs): # real signature unknown
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultAlphaBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def setPersistentOpenGLContext(self, *args, **kwargs): # real signature unknown
        pass

    def setPersistentSceneGraph(self, *args, **kwargs): # real signature unknown
        pass

    def setRenderTarget(self, *args, **kwargs): # real signature unknown
        pass

    def setSceneGraphBackend(self, *args, **kwargs): # real signature unknown
        pass

    def setTextRenderType(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def textRenderType(self, *args, **kwargs): # real signature unknown
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AfterRenderingStage = None # (!) real value is ''
    AfterSwapStage = None # (!) real value is ''
    AfterSynchronizingStage = None # (!) real value is ''
    BeforeRenderingStage = None # (!) real value is ''
    BeforeSynchronizingStage = None # (!) real value is ''
    ContextNotAvailable = None # (!) real value is ''
    CreateTextureOption = None # (!) real value is ''
    CreateTextureOptions = None # (!) real value is ''
    NativeTextRendering = None # (!) real value is ''
    NoStage = None # (!) real value is ''
    QtTextRendering = None # (!) real value is ''
    RenderStage = None # (!) real value is ''
    SceneGraphError = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    TextRenderType = None # (!) real value is ''
    TextureCanUseAtlas = None # (!) real value is ''
    TextureHasAlphaChannel = None # (!) real value is ''
    TextureHasMipmaps = None # (!) real value is ''
    TextureIsOpaque = None # (!) real value is ''
    TextureOwnsGLTexture = None # (!) real value is ''


class QQuickView(QQuickWindow):
    # no doc
    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def errors(self, *args, **kwargs): # real signature unknown
        pass

    def initialSize(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeMode(self, *args, **kwargs): # real signature unknown
        pass

    def rootContext(self, *args, **kwargs): # real signature unknown
        pass

    def rootObject(self, *args, **kwargs): # real signature unknown
        pass

    def setContent(self, *args, **kwargs): # real signature unknown
        pass

    def setResizeMode(self, *args, **kwargs): # real signature unknown
        pass

    def setSource(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def source(self, *args, **kwargs): # real signature unknown
        pass

    def status(self, *args, **kwargs): # real signature unknown
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Error = None # (!) real value is ''
    Loading = None # (!) real value is ''
    Null = None # (!) real value is ''
    Ready = None # (!) real value is ''
    ResizeMode = None # (!) real value is ''
    SizeRootObjectToView = None # (!) real value is ''
    SizeViewToRootObject = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    Status = None # (!) real value is ''


class QSGAbstractRenderer(__PySide2_QtCore.QObject):
    # no doc
    def clearColor(self, *args, **kwargs): # real signature unknown
        pass

    def clearMode(self, *args, **kwargs): # real signature unknown
        pass

    def deviceRect(self, *args, **kwargs): # real signature unknown
        pass

    def nodeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def projectionMatrix(self, *args, **kwargs): # real signature unknown
        pass

    def renderScene(self, *args, **kwargs): # real signature unknown
        pass

    def sceneGraphChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setClearColor(self, *args, **kwargs): # real signature unknown
        pass

    def setClearMode(self, *args, **kwargs): # real signature unknown
        pass

    def setDeviceRect(self, *args, **kwargs): # real signature unknown
        pass

    def setProjectionMatrix(self, *args, **kwargs): # real signature unknown
        pass

    def setProjectionMatrixToRect(self, *args, **kwargs): # real signature unknown
        pass

    def setViewportRect(self, *args, **kwargs): # real signature unknown
        pass

    def viewportRect(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    ClearColorBuffer = None # (!) real value is ''
    ClearDepthBuffer = None # (!) real value is ''
    ClearMode = None # (!) real value is ''
    ClearModeBit = None # (!) real value is ''
    ClearStencilBuffer = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''


class QSGNode(__Shiboken.Object):
    # no doc
    def appendChildNode(self, *args, **kwargs): # real signature unknown
        pass

    def childAtIndex(self, *args, **kwargs): # real signature unknown
        pass

    def childCount(self, *args, **kwargs): # real signature unknown
        pass

    def clearDirty(self, *args, **kwargs): # real signature unknown
        pass

    def dirtyState(self, *args, **kwargs): # real signature unknown
        pass

    def firstChild(self, *args, **kwargs): # real signature unknown
        pass

    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def insertChildNodeAfter(self, *args, **kwargs): # real signature unknown
        pass

    def insertChildNodeBefore(self, *args, **kwargs): # real signature unknown
        pass

    def isSubtreeBlocked(self, *args, **kwargs): # real signature unknown
        pass

    def lastChild(self, *args, **kwargs): # real signature unknown
        pass

    def markDirty(self, *args, **kwargs): # real signature unknown
        pass

    def nextSibling(self, *args, **kwargs): # real signature unknown
        pass

    def parent(self, *args, **kwargs): # real signature unknown
        pass

    def prependChildNode(self, *args, **kwargs): # real signature unknown
        pass

    def preprocess(self, *args, **kwargs): # real signature unknown
        pass

    def previousSibling(self, *args, **kwargs): # real signature unknown
        pass

    def removeAllChildNodes(self, *args, **kwargs): # real signature unknown
        pass

    def removeChildNode(self, *args, **kwargs): # real signature unknown
        pass

    def reparentChildNodesTo(self, *args, **kwargs): # real signature unknown
        pass

    def setFlag(self, *args, **kwargs): # real signature unknown
        pass

    def setFlags(self, *args, **kwargs): # real signature unknown
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

    BasicNodeType = None # (!) real value is ''
    ClipNodeType = None # (!) real value is ''
    DirtyForceUpdate = None # (!) real value is ''
    DirtyGeometry = None # (!) real value is ''
    DirtyMaterial = None # (!) real value is ''
    DirtyMatrix = None # (!) real value is ''
    DirtyNodeAdded = None # (!) real value is ''
    DirtyNodeRemoved = None # (!) real value is ''
    DirtyOpacity = None # (!) real value is ''
    DirtyPropagationMask = None # (!) real value is ''
    DirtyState = None # (!) real value is ''
    DirtyStateBit = None # (!) real value is ''
    DirtySubtreeBlocked = None # (!) real value is ''
    DirtyUsePreprocess = None # (!) real value is ''
    Flag = None # (!) real value is ''
    Flags = None # (!) real value is ''
    GeometryNodeType = None # (!) real value is ''
    IsVisitableNode = None # (!) real value is ''
    NodeType = None # (!) real value is ''
    OpacityNodeType = None # (!) real value is ''
    OwnedByParent = None # (!) real value is ''
    OwnsGeometry = None # (!) real value is ''
    OwnsMaterial = None # (!) real value is ''
    OwnsOpaqueMaterial = None # (!) real value is ''
    RenderNodeType = None # (!) real value is ''
    RootNodeType = None # (!) real value is ''
    TransformNodeType = None # (!) real value is ''
    UsePreprocess = None # (!) real value is ''


class QSGBasicGeometryNode(QSGNode):
    # no doc
    def clipList(self, *args, **kwargs): # real signature unknown
        pass

    def geometry(self, *args, **kwargs): # real signature unknown
        pass

    def matrix(self, *args, **kwargs): # real signature unknown
        pass

    def setGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def setRendererClipList(self, *args, **kwargs): # real signature unknown
        pass

    def setRendererMatrix(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QSGClipNode(QSGBasicGeometryNode):
    # no doc
    def clipRect(self, *args, **kwargs): # real signature unknown
        pass

    def isRectangular(self, *args, **kwargs): # real signature unknown
        pass

    def setClipRect(self, *args, **kwargs): # real signature unknown
        pass

    def setIsRectangular(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QSGTexture(__PySide2_QtCore.QObject):
    # no doc
    def anisotropyLevel(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def convertToNormalizedSourceRect(self, *args, **kwargs): # real signature unknown
        pass

    def filtering(self, *args, **kwargs): # real signature unknown
        pass

    def hasAlphaChannel(self, *args, **kwargs): # real signature unknown
        pass

    def hasMipmaps(self, *args, **kwargs): # real signature unknown
        pass

    def horizontalWrapMode(self, *args, **kwargs): # real signature unknown
        pass

    def isAtlasTexture(self, *args, **kwargs): # real signature unknown
        pass

    def mipmapFiltering(self, *args, **kwargs): # real signature unknown
        pass

    def normalizedTextureSubRect(self, *args, **kwargs): # real signature unknown
        pass

    def removedFromAtlas(self, *args, **kwargs): # real signature unknown
        pass

    def setAnisotropyLevel(self, *args, **kwargs): # real signature unknown
        pass

    def setFiltering(self, *args, **kwargs): # real signature unknown
        pass

    def setHorizontalWrapMode(self, *args, **kwargs): # real signature unknown
        pass

    def setMipmapFiltering(self, *args, **kwargs): # real signature unknown
        pass

    def setVerticalWrapMode(self, *args, **kwargs): # real signature unknown
        pass

    def textureId(self, *args, **kwargs): # real signature unknown
        pass

    def textureSize(self, *args, **kwargs): # real signature unknown
        pass

    def updateBindOptions(self, *args, **kwargs): # real signature unknown
        pass

    def verticalWrapMode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Anisotropy16x = None # (!) real value is ''
    Anisotropy2x = None # (!) real value is ''
    Anisotropy4x = None # (!) real value is ''
    Anisotropy8x = None # (!) real value is ''
    AnisotropyLevel = None # (!) real value is ''
    AnisotropyNone = None # (!) real value is ''
    ClampToEdge = None # (!) real value is ''
    Filtering = None # (!) real value is ''
    Linear = None # (!) real value is ''
    MirroredRepeat = None # (!) real value is ''
    Nearest = None # (!) real value is ''
    Repeat = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    WrapMode = None # (!) real value is ''


class QSGDynamicTexture(QSGTexture):
    # no doc
    def updateTexture(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QSGEngine(__PySide2_QtCore.QObject):
    # no doc
    def createRenderer(self, *args, **kwargs): # real signature unknown
        pass

    def createTextureFromId(self, *args, **kwargs): # real signature unknown
        pass

    def createTextureFromImage(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def invalidate(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CreateTextureOption = None # (!) real value is ''
    CreateTextureOptions = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    TextureCanUseAtlas = None # (!) real value is ''
    TextureHasAlphaChannel = None # (!) real value is ''
    TextureIsOpaque = None # (!) real value is ''
    TextureOwnsGLTexture = None # (!) real value is ''


class QSGGeometry(__Shiboken.Object):
    # no doc
    def allocate(self, *args, **kwargs): # real signature unknown
        pass

    def attributeCount(self, *args, **kwargs): # real signature unknown
        pass

    def attributes(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAttributes_ColoredPoint2D(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAttributes_Point2D(self, *args, **kwargs): # real signature unknown
        pass

    def defaultAttributes_TexturedPoint2D(self, *args, **kwargs): # real signature unknown
        pass

    def drawingMode(self, *args, **kwargs): # real signature unknown
        pass

    def indexCount(self, *args, **kwargs): # real signature unknown
        pass

    def indexData(self, *args, **kwargs): # real signature unknown
        pass

    def indexDataAsUInt(self, *args, **kwargs): # real signature unknown
        pass

    def indexDataAsUShort(self, *args, **kwargs): # real signature unknown
        pass

    def indexDataPattern(self, *args, **kwargs): # real signature unknown
        pass

    def indexType(self, *args, **kwargs): # real signature unknown
        pass

    def lineWidth(self, *args, **kwargs): # real signature unknown
        pass

    def markIndexDataDirty(self, *args, **kwargs): # real signature unknown
        pass

    def markVertexDataDirty(self, *args, **kwargs): # real signature unknown
        pass

    def setDrawingMode(self, *args, **kwargs): # real signature unknown
        pass

    def setIndexDataPattern(self, *args, **kwargs): # real signature unknown
        pass

    def setLineWidth(self, *args, **kwargs): # real signature unknown
        pass

    def setVertexDataPattern(self, *args, **kwargs): # real signature unknown
        pass

    def sizeOfIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sizeOfVertex(self, *args, **kwargs): # real signature unknown
        pass

    def updateColoredRectGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def updateRectGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def updateTexturedRectGeometry(self, *args, **kwargs): # real signature unknown
        pass

    def vertexCount(self, *args, **kwargs): # real signature unknown
        pass

    def vertexData(self, *args, **kwargs): # real signature unknown
        pass

    def vertexDataAsColoredPoint2D(self, *args, **kwargs): # real signature unknown
        pass

    def vertexDataAsPoint2D(self, *args, **kwargs): # real signature unknown
        pass

    def vertexDataAsTexturedPoint2D(self, *args, **kwargs): # real signature unknown
        pass

    def vertexDataPattern(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AlwaysUploadPattern = None # (!) real value is ''
    Attribute = None # (!) real value is ''
    AttributeSet = None # (!) real value is ''
    AttributeType = None # (!) real value is ''
    ByteType = None # (!) real value is ''
    ColorAttribute = None # (!) real value is ''
    ColoredPoint2D = None # (!) real value is ''
    DataPattern = None # (!) real value is ''
    DrawingMode = None # (!) real value is ''
    DrawLineLoop = None # (!) real value is ''
    DrawLines = None # (!) real value is ''
    DrawLineStrip = None # (!) real value is ''
    DrawPoints = None # (!) real value is ''
    DrawTriangleFan = None # (!) real value is ''
    DrawTriangles = None # (!) real value is ''
    DrawTriangleStrip = None # (!) real value is ''
    DynamicPattern = None # (!) real value is ''
    FloatType = None # (!) real value is ''
    IntType = None # (!) real value is ''
    Point2D = None # (!) real value is ''
    PositionAttribute = None # (!) real value is ''
    ShortType = None # (!) real value is ''
    StaticPattern = None # (!) real value is ''
    StreamPattern = None # (!) real value is ''
    TexCoord1Attribute = None # (!) real value is ''
    TexCoord2Attribute = None # (!) real value is ''
    TexCoordAttribute = None # (!) real value is ''
    TexturedPoint2D = None # (!) real value is ''
    Type = None # (!) real value is ''
    UnknownAttribute = None # (!) real value is ''
    UnsignedByteType = None # (!) real value is ''
    UnsignedIntType = None # (!) real value is ''
    UnsignedShortType = None # (!) real value is ''


class QSGGeometryNode(QSGBasicGeometryNode):
    # no doc
    def inheritedOpacity(self, *args, **kwargs): # real signature unknown
        pass

    def renderOrder(self, *args, **kwargs): # real signature unknown
        pass

    def setInheritedOpacity(self, *args, **kwargs): # real signature unknown
        pass

    def setRenderOrder(self, *args, **kwargs): # real signature unknown
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


class QSGMaterialType(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QSGOpacityNode(QSGNode):
    # no doc
    def combinedOpacity(self, *args, **kwargs): # real signature unknown
        pass

    def isSubtreeBlocked(self, *args, **kwargs): # real signature unknown
        pass

    def opacity(self, *args, **kwargs): # real signature unknown
        pass

    def setCombinedOpacity(self, *args, **kwargs): # real signature unknown
        pass

    def setOpacity(self, *args, **kwargs): # real signature unknown
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


class QSGSimpleRectNode(QSGGeometryNode):
    # no doc
    def color(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self, *args, **kwargs): # real signature unknown
        pass

    def setColor(self, *args, **kwargs): # real signature unknown
        pass

    def setRect(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QSGSimpleTextureNode(QSGGeometryNode):
    # no doc
    def filtering(self, *args, **kwargs): # real signature unknown
        pass

    def ownsTexture(self, *args, **kwargs): # real signature unknown
        pass

    def rect(self, *args, **kwargs): # real signature unknown
        pass

    def setFiltering(self, *args, **kwargs): # real signature unknown
        pass

    def setOwnsTexture(self, *args, **kwargs): # real signature unknown
        pass

    def setRect(self, *args, **kwargs): # real signature unknown
        pass

    def setSourceRect(self, *args, **kwargs): # real signature unknown
        pass

    def setTexture(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureCoordinatesTransform(self, *args, **kwargs): # real signature unknown
        pass

    def sourceRect(self, *args, **kwargs): # real signature unknown
        pass

    def texture(self, *args, **kwargs): # real signature unknown
        pass

    def textureCoordinatesTransform(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    MirrorHorizontally = None # (!) real value is ''
    MirrorVertically = None # (!) real value is ''
    NoTransform = None # (!) real value is ''
    TextureCoordinatesTransformFlag = None # (!) real value is ''
    TextureCoordinatesTransformMode = None # (!) real value is ''


class QSGTextureProvider(__PySide2_QtCore.QObject):
    # no doc
    def texture(self, *args, **kwargs): # real signature unknown
        pass

    def textureChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QSGTransformNode(QSGNode):
    # no doc
    def combinedMatrix(self, *args, **kwargs): # real signature unknown
        pass

    def matrix(self, *args, **kwargs): # real signature unknown
        pass

    def setCombinedMatrix(self, *args, **kwargs): # real signature unknown
        pass

    def setMatrix(self, *args, **kwargs): # real signature unknown
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


class QSharedPointer<QQuickItemGrabResult >(__Shiboken.Object):
    # no doc
    def data(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

