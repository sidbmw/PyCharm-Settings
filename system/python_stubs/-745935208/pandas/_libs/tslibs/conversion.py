# encoding: utf-8
# module pandas._libs.tslibs.conversion
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\_libs\tslibs\conversion.cp37-win_amd64.pyd
# by generator 1.146
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\__init__.py
import pytz as pytz # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pytz\__init__.py
from pandas._libs.tslibs.nattype import NaT

from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.parsing import parse_datetime_string


# functions

def datetime_to_datetime64(*args, **kwargs): # real signature unknown
    """
    Convert ndarray of datetime-like objects to int64 array representing
        nanosecond timestamps.
    
        Parameters
        ----------
        values : ndarray
    
        Returns
        -------
        result : ndarray with dtype int64
        inferred_tz : tzinfo or None
    """
    pass

def date_normalize(*args, **kwargs): # real signature unknown
    """
    Normalize each of the (nanosecond) timestamps in the given array by
        rounding down to the beginning of the day (i.e. midnight).  If `tz`
        is not None, then this is midnight for this timezone.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
    
        Returns
        -------
        result : int64 ndarray of converted of normalized nanosecond timestamps
    """
    pass

def ensure_datetime64ns(*args, **kwargs): # real signature unknown
    """
    Ensure a np.datetime64 array has dtype specifically 'datetime64[ns]'
    
        Parameters
        ----------
        arr : ndarray
        copy : boolean, default True
    
        Returns
        -------
        result : ndarray with dtype datetime64[ns]
    """
    pass

def ensure_timedelta64ns(*args, **kwargs): # real signature unknown
    """
    Ensure a np.timedelta64 array has dtype specifically 'timedelta64[ns]'
    
        Parameters
        ----------
        arr : ndarray
        copy : boolean, default True
    
        Returns
        -------
        result : ndarray with dtype timedelta64[ns]
    """
    pass

def is_date_array_normalized(*args, **kwargs): # real signature unknown
    """
    Check if all of the given (nanosecond) timestamps are normalized to
        midnight, i.e. hour == minute == second == 0.  If the optional timezone
        `tz` is not None, then this is midnight for this timezone.
    
        Parameters
        ----------
        stamps : int64 ndarray
        tz : tzinfo or None
    
        Returns
        -------
        is_normalized : bool True if all stamps are normalized
    """
    pass

def pydt_to_i8(*args, **kwargs): # real signature unknown
    """
    Convert to int64 representation compatible with numpy datetime64; converts
        to UTC
    
        Parameters
        ----------
        pydt : object
    
        Returns
        -------
        i8value : np.int64
    """
    pass

def tz_convert(*args, **kwargs): # real signature unknown
    """
    Convert the values (in i8) from timezone1 to timezone2
    
        Parameters
        ----------
        vals : int64 ndarray
        tz1 : string / timezone object
        tz2 : string / timezone object
    
        Returns
        -------
        int64 ndarray of converted
    """
    pass

def tz_convert_single(*args, **kwargs): # real signature unknown
    """
    Convert the val (in i8) from timezone1 to timezone2
    
        This is a single timezone version of tz_convert
    
        Parameters
        ----------
        val : int64
        tz1 : string / timezone object
        tz2 : string / timezone object
    
        Returns
        -------
        int64 converted
    """
    pass

def tz_localize_to_utc(*args, **kwargs): # real signature unknown
    """
    Localize tzinfo-naive i8 to given time zone (using pytz). If
        there are ambiguities in the values, raise AmbiguousTimeError.
    
        Returns
        -------
        localized : DatetimeIndex
    """
    pass

# classes

class datetime_time(object):
    """
    time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
    
    All arguments are optional. tzinfo may be None, or an instance of
    a tzinfo subclass. The remaining arguments may be ints.
    """
    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ string -> time from time.isoformat() output """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """
        Return string in ISO 8601 format, [HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].
        
        timespec specifies what components of the time to include.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return time with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Formats self with strftime. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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

    def __reduce_ex__(self, proto): # real signature unknown; restored from __doc__
        """ __reduce_ex__(proto) -> (cls, state) """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    resolution = None # (!) real value is ''


class _TSObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

nat_strings = None # (!) real value is ''

NS_DTYPE = None # (!) real value is ''

TD_DTYPE = None # (!) real value is ''

UTC = pytz.UTC

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'convert_datetime_to_tsobject': None, # (!) real value is ''
    'convert_to_tsobject': None, # (!) real value is ''
    'get_datetime64_nanos': None, # (!) real value is ''
    'maybe_datetimelike_to_i8': None, # (!) real value is ''
    'pydt_to_i8': None, # (!) real value is ''
    'tz_convert_single': None, # (!) real value is ''
    'tz_convert_utc_to_tzlocal': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

