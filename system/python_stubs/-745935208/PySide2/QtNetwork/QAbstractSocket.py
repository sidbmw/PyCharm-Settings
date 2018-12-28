# encoding: utf-8
# module PySide2.QtNetwork
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\PySide2\QtNetwork.pyd
# by generator 1.146
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAbstractSocket(__PySide2_QtCore.QIODevice):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def connected(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHost(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectFromHost(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def hostFound(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def localAddress(self, *args, **kwargs): # real signature unknown
        pass

    def localPort(self, *args, **kwargs): # real signature unknown
        pass

    def pauseMode(self, *args, **kwargs): # real signature unknown
        pass

    def peerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def peerName(self, *args, **kwargs): # real signature unknown
        pass

    def peerPort(self, *args, **kwargs): # real signature unknown
        pass

    def proxy(self, *args, **kwargs): # real signature unknown
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def readBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalPort(self, *args, **kwargs): # real signature unknown
        pass

    def setPauseMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerName(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerPort(self, *args, **kwargs): # real signature unknown
        pass

    def setProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketDescriptor(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketError(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketOption(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketState(self, *args, **kwargs): # real signature unknown
        pass

    def socketDescriptor(self, *args, **kwargs): # real signature unknown
        pass

    def socketOption(self, *args, **kwargs): # real signature unknown
        pass

    def socketType(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForConnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForDisconnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForReadyRead(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AddressInUseError = None # (!) real value is ''
    AnyIPProtocol = None # (!) real value is ''
    BindFlag = None # (!) real value is ''
    BindMode = None # (!) real value is ''
    BoundState = None # (!) real value is ''
    ClosingState = None # (!) real value is ''
    ConnectedState = None # (!) real value is ''
    ConnectingState = None # (!) real value is ''
    ConnectionRefusedError = None # (!) real value is ''
    DatagramTooLargeError = None # (!) real value is ''
    DefaultForPlatform = None # (!) real value is ''
    DontShareAddress = None # (!) real value is ''
    HostLookupState = None # (!) real value is ''
    HostNotFoundError = None # (!) real value is ''
    IPv4Protocol = None # (!) real value is ''
    IPv6Protocol = None # (!) real value is ''
    KeepAliveOption = None # (!) real value is ''
    ListeningState = None # (!) real value is ''
    LowDelayOption = None # (!) real value is ''
    MulticastLoopbackOption = None # (!) real value is ''
    MulticastTtlOption = None # (!) real value is ''
    NetworkError = None # (!) real value is ''
    NetworkLayerProtocol = None # (!) real value is ''
    OperationError = None # (!) real value is ''
    PathMtuSocketOption = None # (!) real value is ''
    PauseMode = None # (!) real value is ''
    PauseModes = None # (!) real value is ''
    PauseNever = None # (!) real value is ''
    PauseOnSslErrors = None # (!) real value is ''
    ProxyAuthenticationRequiredError = None # (!) real value is ''
    ProxyConnectionClosedError = None # (!) real value is ''
    ProxyConnectionRefusedError = None # (!) real value is ''
    ProxyConnectionTimeoutError = None # (!) real value is ''
    ProxyNotFoundError = None # (!) real value is ''
    ProxyProtocolError = None # (!) real value is ''
    ReceiveBufferSizeSocketOption = None # (!) real value is ''
    RemoteHostClosedError = None # (!) real value is ''
    ReuseAddressHint = None # (!) real value is ''
    SctpSocket = None # (!) real value is ''
    SendBufferSizeSocketOption = None # (!) real value is ''
    ShareAddress = None # (!) real value is ''
    SocketAccessError = None # (!) real value is ''
    SocketAddressNotAvailableError = None # (!) real value is ''
    SocketError = None # (!) real value is ''
    SocketOption = None # (!) real value is ''
    SocketResourceError = None # (!) real value is ''
    SocketState = None # (!) real value is ''
    SocketTimeoutError = None # (!) real value is ''
    SocketType = None # (!) real value is ''
    SslHandshakeFailedError = None # (!) real value is ''
    SslInternalError = None # (!) real value is ''
    SslInvalidUserDataError = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    TcpSocket = None # (!) real value is ''
    TemporaryError = None # (!) real value is ''
    TypeOfServiceOption = None # (!) real value is ''
    UdpSocket = None # (!) real value is ''
    UnconnectedState = None # (!) real value is ''
    UnfinishedSocketOperationError = None # (!) real value is ''
    UnknownNetworkLayerProtocol = None # (!) real value is ''
    UnknownSocketError = None # (!) real value is ''
    UnknownSocketType = None # (!) real value is ''
    UnsupportedSocketOperationError = None # (!) real value is ''


