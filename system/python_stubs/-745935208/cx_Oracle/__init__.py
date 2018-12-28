# encoding: utf-8
# module cx_Oracle
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\cx_Oracle.cp37-win_amd64.pyd
# by generator 1.146
# no doc

# imports
import datetime as __datetime


# Variables with simple values

apilevel = '2.0'

ATTR_PURITY_DEFAULT = 0
ATTR_PURITY_NEW = 1
ATTR_PURITY_SELF = 2

buildtime = 'Sep 13 2018 14:27:29'

DBSHUTDOWN_ABORT = 4
DBSHUTDOWN_FINAL = 5
DBSHUTDOWN_IMMEDIATE = 3
DBSHUTDOWN_TRANSACTIONAL = 1

DBSHUTDOWN_TRANSACTIONAL_LOCAL = 2

DEQ_BROWSE = 1

DEQ_FIRST_MSG = 1

DEQ_IMMEDIATE = 1
DEQ_LOCKED = 2

DEQ_NEXT_MSG = 3
DEQ_NEXT_TRANSACTION = 2

DEQ_NO_WAIT = 0

DEQ_ON_COMMIT = 2

DEQ_REMOVE = 3

DEQ_REMOVE_NODATA = 4

DEQ_WAIT_FOREVER = -1

ENQ_IMMEDIATE = 1

ENQ_ON_COMMIT = 2

EVENT_AQ = 100
EVENT_DEREG = 5
EVENT_NONE = 0
EVENT_OBJCHANGE = 6
EVENT_QUERYCHANGE = 7
EVENT_SHUTDOWN = 2

EVENT_SHUTDOWN_ANY = 3

EVENT_STARTUP = 1

MSG_BUFFERED = 2
MSG_EXPIRED = 3

MSG_NO_DELAY = 0
MSG_NO_EXPIRATION = -1

MSG_PERSISTENT = 1

MSG_PERSISTENT_OR_BUFFERED = 3

MSG_PROCESSED = 2
MSG_READY = 0
MSG_WAITING = 1

OPCODE_ALLOPS = 0
OPCODE_ALLROWS = 1
OPCODE_ALTER = 16
OPCODE_DELETE = 8
OPCODE_DROP = 32
OPCODE_INSERT = 2
OPCODE_UPDATE = 4

paramstyle = 'named'

PRELIM_AUTH = 8

SPOOL_ATTRVAL_FORCEGET = 2
SPOOL_ATTRVAL_NOWAIT = 1
SPOOL_ATTRVAL_TIMEDWAIT = 3
SPOOL_ATTRVAL_WAIT = 0

SUBSCR_GROUPING_CLASS_TIME = 1

SUBSCR_GROUPING_TYPE_LAST = 2
SUBSCR_GROUPING_TYPE_SUMMARY = 1

SUBSCR_NAMESPACE_AQ = 1
SUBSCR_NAMESPACE_DBCHANGE = 2

SUBSCR_PROTO_HTTP = 3
SUBSCR_PROTO_MAIL = 1
SUBSCR_PROTO_OCI = 0
SUBSCR_PROTO_SERVER = 2

SUBSCR_QOS_BEST_EFFORT = 16

SUBSCR_QOS_DEREG_NFY = 2

SUBSCR_QOS_QUERY = 8
SUBSCR_QOS_RELIABLE = 1
SUBSCR_QOS_ROWIDS = 4

SYSASM = 32768
SYSBKP = 131072
SYSDBA = 2
SYSDGD = 262144
SYSKMT = 524288
SYSOPER = 4
SYSRAC = 1048576

threadsafety = 2

version = '7.0.0'

__version__ = '7.0.0'

# functions

def clientversion(*args, **kwargs): # real signature unknown
    pass

def DateFromTicks(*args, **kwargs): # real signature unknown
    pass

def makedsn(*args, **kwargs): # real signature unknown
    pass

def Time(*args, **kwargs): # real signature unknown
    pass

def TimeFromTicks(*args, **kwargs): # real signature unknown
    pass

def TimestampFromTicks(*args, **kwargs): # real signature unknown
    pass

def __future__(*args, **kwargs): # real signature unknown
    pass

# classes

from .BFILE import BFILE
from .Binary import Binary
from .BINARY import BINARY
from .BLOB import BLOB
from .BOOLEAN import BOOLEAN
from .CLOB import CLOB
from .Connection import Connection
from .connect import connect
from .Cursor import Cursor
from .CURSOR import CURSOR
from .Error import Error
from .DatabaseError import DatabaseError
from .DataError import DataError
from .Date import Date
from .DATETIME import DATETIME
from .DeqOptions import DeqOptions
from .EnqOptions import EnqOptions
from .FIXED_CHAR import FIXED_CHAR
from .FIXED_NCHAR import FIXED_NCHAR
from .IntegrityError import IntegrityError
from .InterfaceError import InterfaceError
from .InternalError import InternalError
from .INTERVAL import INTERVAL
from .LOB import LOB
from .LONG_BINARY import LONG_BINARY
from .LONG_STRING import LONG_STRING
from .MessageProperties import MessageProperties
from .NATIVE_FLOAT import NATIVE_FLOAT
from .NATIVE_INT import NATIVE_INT
from .NCHAR import NCHAR
from .NCLOB import NCLOB
from .NotSupportedError import NotSupportedError
from .NUMBER import NUMBER
from .Object import Object
from .OBJECT import OBJECT
from .ObjectType import ObjectType
from .OperationalError import OperationalError
from .ProgrammingError import ProgrammingError
from .ROWID import ROWID
from .SessionPool import SessionPool
from .SodaCollection import SodaCollection
from .SodaDatabase import SodaDatabase
from .SodaDoc import SodaDoc
from .SodaDocCursor import SodaDocCursor
from .SodaOperation import SodaOperation
from .STRING import STRING
from .Timestamp import Timestamp
from .TIMESTAMP import TIMESTAMP
from .Warning import Warning
from ._Error import _Error
# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

