# encoding: utf-8
# module PySide2.QtWebEngineWidgets
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PySide2\QtWebEngineWidgets.pyd
# by generator 1.146
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtWidgets as __PySide2_QtWidgets
import Shiboken as __Shiboken


# no functions
# classes

class QWebEngineCertificateError(__Shiboken.Object):
    # no doc
    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorDescription(self, *args, **kwargs): # real signature unknown
        pass

    def isOverridable(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CertificateAuthorityInvalid = None # (!) real value is ''
    CertificateCommonNameInvalid = None # (!) real value is ''
    CertificateContainsErrors = None # (!) real value is ''
    CertificateDateInvalid = None # (!) real value is ''
    CertificateInvalid = None # (!) real value is ''
    CertificateNameConstraintViolation = None # (!) real value is ''
    CertificateNonUniqueName = None # (!) real value is ''
    CertificateNoRevocationMechanism = None # (!) real value is ''
    CertificateRevoked = None # (!) real value is ''
    CertificateTransparencyRequired = None # (!) real value is ''
    CertificateUnableToCheckRevocation = None # (!) real value is ''
    CertificateValidityTooLong = None # (!) real value is ''
    CertificateWeakKey = None # (!) real value is ''
    CertificateWeakSignatureAlgorithm = None # (!) real value is ''
    Error = None # (!) real value is ''
    SslPinnedKeyNotInCertificateChain = None # (!) real value is ''


class QWebEngineContextMenuData(__Shiboken.Object):
    # no doc
    def editFlags(self, *args, **kwargs): # real signature unknown
        pass

    def isContentEditable(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def linkText(self, *args, **kwargs): # real signature unknown
        pass

    def linkUrl(self, *args, **kwargs): # real signature unknown
        pass

    def mediaFlags(self, *args, **kwargs): # real signature unknown
        pass

    def mediaType(self, *args, **kwargs): # real signature unknown
        pass

    def mediaUrl(self, *args, **kwargs): # real signature unknown
        pass

    def misspelledWord(self, *args, **kwargs): # real signature unknown
        pass

    def position(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self, *args, **kwargs): # real signature unknown
        pass

    def spellCheckerSuggestions(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CanCopy = None # (!) real value is ''
    CanCut = None # (!) real value is ''
    CanDelete = None # (!) real value is ''
    CanEditRichly = None # (!) real value is ''
    CanPaste = None # (!) real value is ''
    CanRedo = None # (!) real value is ''
    CanSelectAll = None # (!) real value is ''
    CanTranslate = None # (!) real value is ''
    CanUndo = None # (!) real value is ''
    EditFlag = None # (!) real value is ''
    EditFlags = None # (!) real value is ''
    MediaCanPrint = None # (!) real value is ''
    MediaCanRotate = None # (!) real value is ''
    MediaCanSave = None # (!) real value is ''
    MediaCanToggleControls = None # (!) real value is ''
    MediaControls = None # (!) real value is ''
    MediaFlag = None # (!) real value is ''
    MediaFlags = None # (!) real value is ''
    MediaHasAudio = None # (!) real value is ''
    MediaInError = None # (!) real value is ''
    MediaLoop = None # (!) real value is ''
    MediaMuted = None # (!) real value is ''
    MediaPaused = None # (!) real value is ''
    MediaType = None # (!) real value is ''
    MediaTypeAudio = None # (!) real value is ''
    MediaTypeCanvas = None # (!) real value is ''
    MediaTypeFile = None # (!) real value is ''
    MediaTypeImage = None # (!) real value is ''
    MediaTypeNone = None # (!) real value is ''
    MediaTypePlugin = None # (!) real value is ''
    MediaTypeVideo = None # (!) real value is ''


class QWebEngineDownloadItem(__PySide2_QtCore.QObject):
    # no doc
    def accept(self, *args, **kwargs): # real signature unknown
        pass

    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def downloadProgress(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def id(self, *args, **kwargs): # real signature unknown
        pass

    def interruptReason(self, *args, **kwargs): # real signature unknown
        pass

    def interruptReasonString(self, *args, **kwargs): # real signature unknown
        pass

    def isFinished(self, *args, **kwargs): # real signature unknown
        pass

    def isPaused(self, *args, **kwargs): # real signature unknown
        pass

    def isPausedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isSavePageDownload(self, *args, **kwargs): # real signature unknown
        pass

    def mimeType(self, *args, **kwargs): # real signature unknown
        pass

    def path(self, *args, **kwargs): # real signature unknown
        pass

    def pause(self, *args, **kwargs): # real signature unknown
        pass

    def receivedBytes(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def savePageFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setPath(self, *args, **kwargs): # real signature unknown
        pass

    def setSavePageFormat(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def totalBytes(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    CompleteHtmlSaveFormat = None # (!) real value is ''
    DownloadCancelled = None # (!) real value is ''
    DownloadCompleted = None # (!) real value is ''
    DownloadInProgress = None # (!) real value is ''
    DownloadInterrupted = None # (!) real value is ''
    DownloadInterruptReason = None # (!) real value is ''
    DownloadRequested = None # (!) real value is ''
    DownloadState = None # (!) real value is ''
    FileAccessDenied = None # (!) real value is ''
    FileBlocked = None # (!) real value is ''
    FileFailed = None # (!) real value is ''
    FileHashMismatch = None # (!) real value is ''
    FileNameTooLong = None # (!) real value is ''
    FileNoSpace = None # (!) real value is ''
    FileSecurityCheckFailed = None # (!) real value is ''
    FileTooLarge = None # (!) real value is ''
    FileTooShort = None # (!) real value is ''
    FileTransientError = None # (!) real value is ''
    FileVirusInfected = None # (!) real value is ''
    MimeHtmlSaveFormat = None # (!) real value is ''
    NetworkDisconnected = None # (!) real value is ''
    NetworkFailed = None # (!) real value is ''
    NetworkInvalidRequest = None # (!) real value is ''
    NetworkServerDown = None # (!) real value is ''
    NetworkTimeout = None # (!) real value is ''
    NoReason = None # (!) real value is ''
    SavePageFormat = None # (!) real value is ''
    ServerBadContent = None # (!) real value is ''
    ServerCertProblem = None # (!) real value is ''
    ServerFailed = None # (!) real value is ''
    ServerForbidden = None # (!) real value is ''
    ServerUnauthorized = None # (!) real value is ''
    ServerUnreachable = None # (!) real value is ''
    SingleHtmlSaveFormat = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    UnknownSaveFormat = None # (!) real value is ''
    UserCanceled = None # (!) real value is ''


class QWebEngineFullScreenRequest(__Shiboken.Object):
    # no doc
    def accept(self, *args, **kwargs): # real signature unknown
        pass

    def origin(self, *args, **kwargs): # real signature unknown
        pass

    def reject(self, *args, **kwargs): # real signature unknown
        pass

    def toggleOn(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWebEngineHistoryItem(__Shiboken.Object):
    # no doc
    def iconUrl(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def lastVisited(self, *args, **kwargs): # real signature unknown
        pass

    def originalUrl(self, *args, **kwargs): # real signature unknown
        pass

    def swap(self, *args, **kwargs): # real signature unknown
        pass

    def title(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWebEnginePage(__PySide2_QtCore.QObject):
    # no doc
    def acceptNavigationRequest(self, *args, **kwargs): # real signature unknown
        pass

    def action(self, *args, **kwargs): # real signature unknown
        pass

    def audioMutedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def backgroundColor(self, *args, **kwargs): # real signature unknown
        pass

    def certificateError(self, *args, **kwargs): # real signature unknown
        pass

    def chooseFiles(self, *args, **kwargs): # real signature unknown
        pass

    def contentsSize(self, *args, **kwargs): # real signature unknown
        pass

    def contentsSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuData(self, *args, **kwargs): # real signature unknown
        pass

    def createStandardContextMenu(self, *args, **kwargs): # real signature unknown
        pass

    def createWindow(self, *args, **kwargs): # real signature unknown
        pass

    def devToolsPage(self, *args, **kwargs): # real signature unknown
        pass

    def download(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def featurePermissionRequestCanceled(self, *args, **kwargs): # real signature unknown
        pass

    def featurePermissionRequested(self, *args, **kwargs): # real signature unknown
        pass

    def findText(self, *args, **kwargs): # real signature unknown
        pass

    def fullScreenRequested(self, *args, **kwargs): # real signature unknown
        pass

    def geometryChangeRequested(self, *args, **kwargs): # real signature unknown
        pass

    def hasSelection(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self, *args, **kwargs): # real signature unknown
        pass

    def iconChanged(self, *args, **kwargs): # real signature unknown
        pass

    def iconUrl(self, *args, **kwargs): # real signature unknown
        pass

    def iconUrlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def inspectedPage(self, *args, **kwargs): # real signature unknown
        pass

    def isAudioMuted(self, *args, **kwargs): # real signature unknown
        pass

    def javaScriptAlert(self, *args, **kwargs): # real signature unknown
        pass

    def javaScriptConfirm(self, *args, **kwargs): # real signature unknown
        pass

    def javaScriptConsoleMessage(self, *args, **kwargs): # real signature unknown
        pass

    def javaScriptPrompt(self, *args, **kwargs): # real signature unknown
        pass

    def linkHovered(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def loadFinished(self, *args, **kwargs): # real signature unknown
        pass

    def loadProgress(self, *args, **kwargs): # real signature unknown
        pass

    def loadStarted(self, *args, **kwargs): # real signature unknown
        pass

    def pdfPrintingFinished(self, *args, **kwargs): # real signature unknown
        pass

    def printToPdf(self, *args, **kwargs): # real signature unknown
        pass

    def profile(self, *args, **kwargs): # real signature unknown
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def quotaRequested(self, *args, **kwargs): # real signature unknown
        pass

    def recentlyAudible(self, *args, **kwargs): # real signature unknown
        pass

    def recentlyAudibleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def registerProtocolHandlerRequested(self, *args, **kwargs): # real signature unknown
        pass

    def renderProcessTerminated(self, *args, **kwargs): # real signature unknown
        pass

    def replaceMisspelledWord(self, *args, **kwargs): # real signature unknown
        pass

    def requestedUrl(self, *args, **kwargs): # real signature unknown
        pass

    def runJavaScript(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def scripts(self, *args, **kwargs): # real signature unknown
        pass

    def scrollPosition(self, *args, **kwargs): # real signature unknown
        pass

    def scrollPositionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self, *args, **kwargs): # real signature unknown
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setAudioMuted(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundColor(self, *args, **kwargs): # real signature unknown
        pass

    def setContent(self, *args, **kwargs): # real signature unknown
        pass

    def setDevToolsPage(self, *args, **kwargs): # real signature unknown
        pass

    def setFeaturePermission(self, *args, **kwargs): # real signature unknown
        pass

    def setHtml(self, *args, **kwargs): # real signature unknown
        pass

    def setInspectedPage(self, *args, **kwargs): # real signature unknown
        pass

    def settings(self, *args, **kwargs): # real signature unknown
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        pass

    def setView(self, *args, **kwargs): # real signature unknown
        pass

    def setWebChannel(self, *args, **kwargs): # real signature unknown
        pass

    def setZoomFactor(self, *args, **kwargs): # real signature unknown
        pass

    def title(self, *args, **kwargs): # real signature unknown
        pass

    def titleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def triggerAction(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def urlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def view(self, *args, **kwargs): # real signature unknown
        pass

    def webChannel(self, *args, **kwargs): # real signature unknown
        pass

    def windowCloseRequested(self, *args, **kwargs): # real signature unknown
        pass

    def zoomFactor(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AbnormalTerminationStatus = None # (!) real value is ''
    AlignCenter = None # (!) real value is ''
    AlignJustified = None # (!) real value is ''
    AlignLeft = None # (!) real value is ''
    AlignRight = None # (!) real value is ''
    Back = None # (!) real value is ''
    Copy = None # (!) real value is ''
    CopyImageToClipboard = None # (!) real value is ''
    CopyImageUrlToClipboard = None # (!) real value is ''
    CopyLinkToClipboard = None # (!) real value is ''
    CopyMediaUrlToClipboard = None # (!) real value is ''
    CrashedTerminationStatus = None # (!) real value is ''
    Cut = None # (!) real value is ''
    DesktopAudioVideoCapture = None # (!) real value is ''
    DesktopVideoCapture = None # (!) real value is ''
    DownloadImageToDisk = None # (!) real value is ''
    DownloadLinkToDisk = None # (!) real value is ''
    DownloadMediaToDisk = None # (!) real value is ''
    ErrorMessageLevel = None # (!) real value is ''
    ExitFullScreen = None # (!) real value is ''
    Feature = None # (!) real value is ''
    FileSelectionMode = None # (!) real value is ''
    FileSelectOpen = None # (!) real value is ''
    FileSelectOpenMultiple = None # (!) real value is ''
    FindBackward = None # (!) real value is ''
    FindCaseSensitively = None # (!) real value is ''
    FindFlag = None # (!) real value is ''
    FindFlags = None # (!) real value is ''
    Forward = None # (!) real value is ''
    Geolocation = None # (!) real value is ''
    Indent = None # (!) real value is ''
    InfoMessageLevel = None # (!) real value is ''
    InsertOrderedList = None # (!) real value is ''
    InsertUnorderedList = None # (!) real value is ''
    InspectElement = None # (!) real value is ''
    JavaScriptConsoleMessageLevel = None # (!) real value is ''
    KilledTerminationStatus = None # (!) real value is ''
    MediaAudioCapture = None # (!) real value is ''
    MediaAudioVideoCapture = None # (!) real value is ''
    MediaVideoCapture = None # (!) real value is ''
    MouseLock = None # (!) real value is ''
    NavigationType = None # (!) real value is ''
    NavigationTypeBackForward = None # (!) real value is ''
    NavigationTypeFormSubmitted = None # (!) real value is ''
    NavigationTypeLinkClicked = None # (!) real value is ''
    NavigationTypeOther = None # (!) real value is ''
    NavigationTypeReload = None # (!) real value is ''
    NavigationTypeTyped = None # (!) real value is ''
    NormalTerminationStatus = None # (!) real value is ''
    Notifications = None # (!) real value is ''
    NoWebAction = None # (!) real value is ''
    OpenLinkInNewBackgroundTab = None # (!) real value is ''
    OpenLinkInNewTab = None # (!) real value is ''
    OpenLinkInNewWindow = None # (!) real value is ''
    OpenLinkInThisWindow = None # (!) real value is ''
    Outdent = None # (!) real value is ''
    Paste = None # (!) real value is ''
    PasteAndMatchStyle = None # (!) real value is ''
    PermissionDeniedByUser = None # (!) real value is ''
    PermissionGrantedByUser = None # (!) real value is ''
    PermissionPolicy = None # (!) real value is ''
    PermissionUnknown = None # (!) real value is ''
    Redo = None # (!) real value is ''
    Reload = None # (!) real value is ''
    ReloadAndBypassCache = None # (!) real value is ''
    RenderProcessTerminationStatus = None # (!) real value is ''
    RequestClose = None # (!) real value is ''
    SavePage = None # (!) real value is ''
    SelectAll = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    Stop = None # (!) real value is ''
    ToggleBold = None # (!) real value is ''
    ToggleItalic = None # (!) real value is ''
    ToggleMediaControls = None # (!) real value is ''
    ToggleMediaLoop = None # (!) real value is ''
    ToggleMediaMute = None # (!) real value is ''
    ToggleMediaPlayPause = None # (!) real value is ''
    ToggleStrikethrough = None # (!) real value is ''
    ToggleUnderline = None # (!) real value is ''
    Undo = None # (!) real value is ''
    Unselect = None # (!) real value is ''
    ViewSource = None # (!) real value is ''
    WarningMessageLevel = None # (!) real value is ''
    WebAction = None # (!) real value is ''
    WebActionCount = None # (!) real value is ''
    WebBrowserBackgroundTab = None # (!) real value is ''
    WebBrowserTab = None # (!) real value is ''
    WebBrowserWindow = None # (!) real value is ''
    WebDialog = None # (!) real value is ''
    WebWindowType = None # (!) real value is ''


class QWebEngineProfile(__PySide2_QtCore.QObject):
    # no doc
    def cachePath(self, *args, **kwargs): # real signature unknown
        pass

    def clearAllVisitedLinks(self, *args, **kwargs): # real signature unknown
        pass

    def clearHttpCache(self, *args, **kwargs): # real signature unknown
        pass

    def clearVisitedLinks(self, *args, **kwargs): # real signature unknown
        pass

    def cookieStore(self, *args, **kwargs): # real signature unknown
        pass

    def defaultProfile(self, *args, **kwargs): # real signature unknown
        pass

    def downloadRequested(self, *args, **kwargs): # real signature unknown
        pass

    def httpAcceptLanguage(self, *args, **kwargs): # real signature unknown
        pass

    def httpCacheMaximumSize(self, *args, **kwargs): # real signature unknown
        pass

    def httpCacheType(self, *args, **kwargs): # real signature unknown
        pass

    def httpUserAgent(self, *args, **kwargs): # real signature unknown
        pass

    def installUrlSchemeHandler(self, *args, **kwargs): # real signature unknown
        pass

    def isOffTheRecord(self, *args, **kwargs): # real signature unknown
        pass

    def isSpellCheckEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def persistentCookiesPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def persistentStoragePath(self, *args, **kwargs): # real signature unknown
        pass

    def removeAllUrlSchemeHandlers(self, *args, **kwargs): # real signature unknown
        pass

    def removeUrlScheme(self, *args, **kwargs): # real signature unknown
        pass

    def removeUrlSchemeHandler(self, *args, **kwargs): # real signature unknown
        pass

    def scripts(self, *args, **kwargs): # real signature unknown
        pass

    def setCachePath(self, *args, **kwargs): # real signature unknown
        pass

    def setHttpAcceptLanguage(self, *args, **kwargs): # real signature unknown
        pass

    def setHttpCacheMaximumSize(self, *args, **kwargs): # real signature unknown
        pass

    def setHttpCacheType(self, *args, **kwargs): # real signature unknown
        pass

    def setHttpUserAgent(self, *args, **kwargs): # real signature unknown
        pass

    def setPersistentCookiesPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setPersistentStoragePath(self, *args, **kwargs): # real signature unknown
        pass

    def setRequestInterceptor(self, *args, **kwargs): # real signature unknown
        pass

    def setSpellCheckEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def setSpellCheckLanguages(self, *args, **kwargs): # real signature unknown
        pass

    def settings(self, *args, **kwargs): # real signature unknown
        pass

    def spellCheckLanguages(self, *args, **kwargs): # real signature unknown
        pass

    def storageName(self, *args, **kwargs): # real signature unknown
        pass

    def urlSchemeHandler(self, *args, **kwargs): # real signature unknown
        pass

    def visitedLinksContainsUrl(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AllowPersistentCookies = None # (!) real value is ''
    DiskHttpCache = None # (!) real value is ''
    ForcePersistentCookies = None # (!) real value is ''
    HttpCacheType = None # (!) real value is ''
    MemoryHttpCache = None # (!) real value is ''
    NoCache = None # (!) real value is ''
    NoPersistentCookies = None # (!) real value is ''
    PersistentCookiesPolicy = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''


class QWebEngineScript(__Shiboken.Object):
    # no doc
    def injectionPoint(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def runsOnSubFrames(self, *args, **kwargs): # real signature unknown
        pass

    def setInjectionPoint(self, *args, **kwargs): # real signature unknown
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        pass

    def setRunsOnSubFrames(self, *args, **kwargs): # real signature unknown
        pass

    def setSourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def setWorldId(self, *args, **kwargs): # real signature unknown
        pass

    def sourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def swap(self, *args, **kwargs): # real signature unknown
        pass

    def worldId(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    ApplicationWorld = None # (!) real value is ''
    Deferred = None # (!) real value is ''
    DocumentCreation = None # (!) real value is ''
    DocumentReady = None # (!) real value is ''
    InjectionPoint = None # (!) real value is ''
    MainWorld = None # (!) real value is ''
    ScriptWorldId = None # (!) real value is ''
    UserWorld = None # (!) real value is ''
    __hash__ = None


class QWebEngineScriptCollection(__Shiboken.Object):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def findScript(self, *args, **kwargs): # real signature unknown
        pass

    def findScripts(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def toList(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QWebEngineSettings(__Shiboken.Object):
    # no doc
    def defaultSettings(self, *args, **kwargs): # real signature unknown
        pass

    def defaultTextEncoding(self, *args, **kwargs): # real signature unknown
        pass

    def fontFamily(self, *args, **kwargs): # real signature unknown
        pass

    def fontSize(self, *args, **kwargs): # real signature unknown
        pass

    def globalSettings(self, *args, **kwargs): # real signature unknown
        pass

    def resetAttribute(self, *args, **kwargs): # real signature unknown
        pass

    def resetFontFamily(self, *args, **kwargs): # real signature unknown
        pass

    def resetFontSize(self, *args, **kwargs): # real signature unknown
        pass

    def resetUnknownUrlSchemePolicy(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultTextEncoding(self, *args, **kwargs): # real signature unknown
        pass

    def setFontFamily(self, *args, **kwargs): # real signature unknown
        pass

    def setFontSize(self, *args, **kwargs): # real signature unknown
        pass

    def setUnknownUrlSchemePolicy(self, *args, **kwargs): # real signature unknown
        pass

    def testAttribute(self, *args, **kwargs): # real signature unknown
        pass

    def unknownUrlSchemePolicy(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Accelerated2dCanvasEnabled = None # (!) real value is ''
    AllowAllUnknownUrlSchemes = None # (!) real value is ''
    AllowGeolocationOnInsecureOrigins = None # (!) real value is ''
    AllowRunningInsecureContent = None # (!) real value is ''
    AllowUnknownUrlSchemesFromUserInteraction = None # (!) real value is ''
    AllowWindowActivationFromJavaScript = None # (!) real value is ''
    AutoLoadIconsForPage = None # (!) real value is ''
    AutoLoadImages = None # (!) real value is ''
    CursiveFont = None # (!) real value is ''
    DefaultFixedFontSize = None # (!) real value is ''
    DefaultFontSize = None # (!) real value is ''
    DisallowUnknownUrlSchemes = None # (!) real value is ''
    ErrorPageEnabled = None # (!) real value is ''
    FantasyFont = None # (!) real value is ''
    FixedFont = None # (!) real value is ''
    FocusOnNavigationEnabled = None # (!) real value is ''
    FontFamily = None # (!) real value is ''
    FontSize = None # (!) real value is ''
    FullScreenSupportEnabled = None # (!) real value is ''
    HyperlinkAuditingEnabled = None # (!) real value is ''
    JavascriptCanAccessClipboard = None # (!) real value is ''
    JavascriptCanOpenWindows = None # (!) real value is ''
    JavascriptCanPaste = None # (!) real value is ''
    JavascriptEnabled = None # (!) real value is ''
    LinksIncludedInFocusChain = None # (!) real value is ''
    LocalContentCanAccessFileUrls = None # (!) real value is ''
    LocalContentCanAccessRemoteUrls = None # (!) real value is ''
    LocalStorageEnabled = None # (!) real value is ''
    MinimumFontSize = None # (!) real value is ''
    MinimumLogicalFontSize = None # (!) real value is ''
    PictographFont = None # (!) real value is ''
    PlaybackRequiresUserGesture = None # (!) real value is ''
    PluginsEnabled = None # (!) real value is ''
    PrintElementBackgrounds = None # (!) real value is ''
    SansSerifFont = None # (!) real value is ''
    ScreenCaptureEnabled = None # (!) real value is ''
    ScrollAnimatorEnabled = None # (!) real value is ''
    SerifFont = None # (!) real value is ''
    ShowScrollBars = None # (!) real value is ''
    SpatialNavigationEnabled = None # (!) real value is ''
    StandardFont = None # (!) real value is ''
    TouchIconsEnabled = None # (!) real value is ''
    UnknownUrlSchemePolicy = None # (!) real value is ''
    WebAttribute = None # (!) real value is ''
    WebGLEnabled = None # (!) real value is ''
    WebRTCPublicInterfacesOnly = None # (!) real value is ''
    XSSAuditingEnabled = None # (!) real value is ''


class QWebEngineView(__PySide2_QtWidgets.QWidget):
    # no doc
    def back(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def createWindow(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def findText(self, *args, **kwargs): # real signature unknown
        pass

    def forward(self, *args, **kwargs): # real signature unknown
        pass

    def hasSelection(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self, *args, **kwargs): # real signature unknown
        pass

    def iconChanged(self, *args, **kwargs): # real signature unknown
        pass

    def iconUrl(self, *args, **kwargs): # real signature unknown
        pass

    def iconUrlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def loadFinished(self, *args, **kwargs): # real signature unknown
        pass

    def loadProgress(self, *args, **kwargs): # real signature unknown
        pass

    def loadStarted(self, *args, **kwargs): # real signature unknown
        pass

    def page(self, *args, **kwargs): # real signature unknown
        pass

    def pageAction(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self, *args, **kwargs): # real signature unknown
        pass

    def renderProcessTerminated(self, *args, **kwargs): # real signature unknown
        pass

    def selectedText(self, *args, **kwargs): # real signature unknown
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setContent(self, *args, **kwargs): # real signature unknown
        pass

    def setHtml(self, *args, **kwargs): # real signature unknown
        pass

    def setPage(self, *args, **kwargs): # real signature unknown
        pass

    def settings(self, *args, **kwargs): # real signature unknown
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        pass

    def setZoomFactor(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def title(self, *args, **kwargs): # real signature unknown
        pass

    def titleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def triggerPageAction(self, *args, **kwargs): # real signature unknown
        pass

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def urlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def zoomFactor(self, *args, **kwargs): # real signature unknown
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

