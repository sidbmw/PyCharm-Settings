# encoding: utf-8
# module pandas._libs.tslibs.timestamps
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\_libs\tslibs\timestamps.cp37-win_amd64.pyd
# by generator 1.146
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\warnings.py
import numpy as np # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.conversion import (date_normalize, 
    tz_localize_to_utc)

from pandas._libs.tslibs.fields import (get_date_name_field, 
    get_start_end_field)

from pandas._libs.tslibs.nattype import NaT

from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.timedeltas import Timedelta

import datetime as __datetime


# functions

def round_ns(*args, **kwargs): # real signature unknown
    """
    Applies rounding function at given frequency
    
        Parameters
        ----------
        values : :obj:`ndarray`
        rounder : function, eg. 'ceil', 'floor', 'round'
        freq : str, obj
    
        Returns
        -------
        :obj:`ndarray`
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


class _Timestamp(__datetime.datetime):
    # no doc
    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def to_datetime64(self, *args, **kwargs): # real signature unknown
        """ Returns a numpy.datetime64 object with 'ns' precision """
        pass

    def to_pydatetime(self, *args, **kwargs): # real signature unknown
        """
        Convert a Timestamp object to a native Python datetime object.
        
                If warn=True, issue a warning if nanoseconds is nonzero.
        """
        pass

    def _get_date_name_field(self, *args, **kwargs): # real signature unknown
        pass

    def _get_start_end_field(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _repr_base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _short_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _time_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is ''


class Timestamp(_Timestamp):
    """
    Pandas replacement for datetime.datetime
    
        Timestamp is the pandas equivalent of python's Datetime
        and is interchangeable with it in most cases. It's the type used
        for the entries that make up a DatetimeIndex, and other timeseries
        oriented data structures in pandas.
    
        Parameters
        ----------
        ts_input : datetime-like, str, int, float
            Value to be converted to Timestamp
        freq : str, DateOffset
            Offset which Timestamp will have
        tz : str, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time which Timestamp will have.
        unit : str
            Unit used for conversion if ts_input is of type int or float. The
            valid values are 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For
            example, 's' means seconds and 'ms' means milliseconds.
        year, month, day : int
            .. versionadded:: 0.19.0
        hour, minute, second, microsecond : int, optional, default 0
            .. versionadded:: 0.19.0
        nanosecond : int, optional, default 0
            .. versionadded:: 0.23.0
        tzinfo : datetime.tzinfo, optional, default None
            .. versionadded:: 0.19.0
    
        Notes
        -----
        There are essentially three calling conventions for the constructor. The
        primary form accepts four parameters. They can be passed by position or
        keyword.
    
        The other two forms mimic the parameters from ``datetime.datetime``. They
        can be passed by either position or keyword, but not both mixed together.
    
        Examples
        --------
        Using the primary calling convention:
    
        This converts a datetime-like string
        >>> pd.Timestamp('2017-01-01T12')
        Timestamp('2017-01-01 12:00:00')
    
        This converts a float representing a Unix epoch in units of seconds
        >>> pd.Timestamp(1513393355.5, unit='s')
        Timestamp('2017-12-16 03:02:35.500000')
    
        This converts an int representing a Unix-epoch in units of seconds
        and for a particular timezone
        >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')
        Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')
    
        Using the other two forms that mimic the API for ``datetime.datetime``:
    
        >>> pd.Timestamp(2017, 1, 1, 12)
        Timestamp('2017-01-01 12:00:00')
    
        >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)
        Timestamp('2017-01-01 12:00:00')
    """
    def astimezone(self, *args, **kwargs): # real signature unknown
        """
        Convert tz-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        """
        pass

    def ceil(self, *args, **kwargs): # real signature unknown
        """
        return a new Timestamp ceiled to this resolution
        
                Parameters
                ----------
                freq : a freq string indicating the ceiling resolution
        """
        pass

    @classmethod
    def combine(cls, date, time): # real signature unknown; restored from __doc__
        """
        Timsetamp.combine(date, time)
        
                date, time -> datetime with same date and time fields
        """
        pass

    def day_name(self, *args, **kwargs): # real signature unknown
        """
        Return the day name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : string, default None (English locale)
                    locale determining the language in which to return the day name
        
                Returns
                -------
                day_name : string
        
                .. versionadded:: 0.23.0
        """
        pass

    def floor(self, *args, **kwargs): # real signature unknown
        """
        return a new Timestamp floored to this resolution
        
                Parameters
                ----------
                freq : a freq string indicating the flooring resolution
        """
        pass

    @classmethod
    def fromordinal(cls, ordinal, freq=None, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.fromordinal(ordinal, freq=None, tz=None)
        
                passed an ordinal, translate and convert to a ts
                note: by definition there cannot be any tz info on the ordinal itself
        
                Parameters
                ----------
                ordinal : int
                    date corresponding to a proleptic Gregorian ordinal
                freq : str, DateOffset
                    Offset which Timestamp will have
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will have.
        """
        pass

    @classmethod
    def fromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.fromtimestamp(ts)
        
                timestamp[, tz] -> tz's local time from POSIX timestamp.
        """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        pass

    def month_name(self, *args, **kwargs): # real signature unknown
        """
        Return the month name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : string, default None (English locale)
                    locale determining the language in which to return the month name
        
                Returns
                -------
                month_name : string
        
                .. versionadded:: 0.23.0
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Normalize Timestamp to midnight, preserving
                tz information.
        """
        pass

    @classmethod
    def now(cls, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.now(tz=None)
        
                Returns new Timestamp object representing current time local to
                tz.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        implements datetime.replace, handles nanoseconds
        
                Parameters
                ----------
                year : int, optional
                month : int, optional
                day : int, optional
                hour : int, optional
                minute : int, optional
                second : int, optional
                microsecond : int, optional
                nanosecond: int, optional
                tzinfo : tz-convertible, optional
                fold : int, optional, default is 0
                    added in 3.6, NotImplemented
        
                Returns
                -------
                Timestamp with fields replaced
        """
        pass

    def round(self, *args, **kwargs): # real signature unknown
        """
        Round the Timestamp to the specified resolution
        
                Returns
                -------
                a new Timestamp rounded to the given resolution of `freq`
        
                Parameters
                ----------
                freq : a freq string indicating the rounding resolution
        
                Raises
                ------
                ValueError if the freq cannot be converted
        """
        pass

    @classmethod
    def today(cls, cls_1, tz=None): # real signature unknown; restored from __doc__
        """
        Timestamp.today(cls, tz=None)
        
                Return the current time in the local timezone.  This differs
                from datetime.today() in that it can be localized to a
                passed timezone.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to
        """
        pass

    def to_julian_date(self, *args, **kwargs): # real signature unknown
        """
        Convert TimeStamp to a Julian Date.
                0 Julian date is noon January 1, 4713 BC.
        """
        pass

    def to_period(self, *args, **kwargs): # real signature unknown
        """ Return an period of which this timestamp is an observation. """
        pass

    def tz_convert(self, *args, **kwargs): # real signature unknown
        """
        Convert tz-aware Timestamp to another time zone.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        """
        pass

    def tz_localize(self, *args, **kwargs): # real signature unknown
        """
        Convert naive Timestamp to local time zone, or remove
                timezone from tz-aware Timestamp.
        
                Parameters
                ----------
                tz : str, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding local time.
        
                ambiguous : bool, 'NaT', default 'raise'
                    - bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates)
                    - 'NaT' will return NaT for an ambiguous time
                    - 'raise' will raise an AmbiguousTimeError for an ambiguous time
        
                errors : 'raise', 'coerce', default 'raise'
                    - 'raise' will raise a NonExistentTimeError if a timestamp is not
                       valid in the specified timezone (e.g. due to a transition from
                       or to DST time)
                    - 'coerce' will return NaT if the timestamp can not be converted
                      into the specified timezone
        
                      .. versionadded:: 0.19.0
        
                Returns
                -------
                localized : Timestamp
        
                Raises
                ------
                TypeError
                    If the Timestamp is tz-aware and tz is not None.
        """
        pass

    @classmethod
    def utcfromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.utcfromtimestamp(ts)
        
                Construct a naive UTC datetime from a POSIX timestamp.
        """
        pass

    @classmethod
    def utcnow(cls): # real signature unknown; restored from __doc__
        """
        Timestamp.utcnow()
        
                Return a new Timestamp representing UTC day and time.
        """
        pass

    def _has_time_component(self, *args, **kwargs): # real signature unknown
        """
        Returns if the Timestamp has a time component
                in addition to the date part
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freqstr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Alias for tzinfo
        """

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        .. deprecated:: 0.23.0
            Use ``Timestamp.day_name()`` instead
        """

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    __dict__ = None # (!) real value is ''


# variables with complex values

_no_input = None # (!) real value is ''

_zero_time = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    '_NS_LOWER_BOUND': None, # (!) real value is ''
    '_NS_UPPER_BOUND': None, # (!) real value is ''
    'create_timestamp_from_ts': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

