# encoding: utf-8
# module pandas._libs.tslibs.nattype
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\_libs\tslibs\nattype.cp37-win_amd64.pyd
# by generator 1.146
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\__init__.py
import datetime as __datetime


# Variables with simple values

iNaT = -9223372036854775808

# functions

def _make_error_func(*args, **kwargs): # real signature unknown
    pass

def _make_nan_func(*args, **kwargs): # real signature unknown
    pass

def _make_nat_func(*args, **kwargs): # real signature unknown
    pass

def __nat_unpickle(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__NaT(*args, **kwargs): # real signature unknown
    pass

# classes

class _NaT(__datetime.datetime):
    # no doc
    def to_datetime64(self, *args, **kwargs): # real signature unknown
        """ Returns a numpy.datetime64 object with 'ns' precision """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
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

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class NaTType(_NaT):
    """ (N)ot-(A)-(T)ime, the time equivalent of NaN """
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

    def combine(self, date, time): # real signature unknown; restored from __doc__
        """
        Timsetamp.combine(date, time)
        
                date, time -> datetime with same date and time fields
        """
        pass

    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    def date(self, *args, **kwargs): # real signature unknown
        """ Return date object with same year, month and day. """
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

    def dst(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.dst(self). """
        pass

    def floor(self, *args, **kwargs): # real signature unknown
        """
        return a new Timestamp floored to this resolution
        
                Parameters
                ----------
                freq : a freq string indicating the flooring resolution
        """
        pass

    def fromordinal(self, ordinal, freq=None, tz=None): # real signature unknown; restored from __doc__
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

    def fromtimestamp(self, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.fromtimestamp(ts)
        
                timestamp[, tz] -> tz's local time from POSIX timestamp.
        """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a 3-tuple containing ISO year, week number, and weekday. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
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

    def now(self, tz=None): # real signature unknown; restored from __doc__
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

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def strptime(self): # real signature unknown; restored from __doc__
        """ string, format -> new datetime parsed from a string (like time.strptime()). """
        pass

    def time(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time but with tzinfo=None. """
        pass

    def timestamp(self, *args, **kwargs): # real signature unknown
        """ Return POSIX timestamp as float. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    def timetz(self, *args, **kwargs): # real signature unknown
        """ Return time object with same time and tzinfo. """
        pass

    def today(self, cls, tz=None): # real signature unknown; restored from __doc__
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

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total duration of timedelta in seconds (to ns precision) """
        pass

    def to_pydatetime(self, *args, **kwargs): # real signature unknown
        """
        Convert a Timestamp object to a native Python datetime object.
        
                If warn=True, issue a warning if nanoseconds is nonzero.
        """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.tzname(self). """
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

    def utcfromtimestamp(self, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.utcfromtimestamp(ts)
        
                Construct a naive UTC datetime from a POSIX timestamp.
        """
        pass

    def utcnow(self): # real signature unknown; restored from __doc__
        """
        Timestamp.utcnow()
        
                Return a new Timestamp representing UTC day and time.
        """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """ Return self.tzinfo.utcoffset(self). """
        pass

    def utctimetuple(self, *args, **kwargs): # real signature unknown
        """ Return UTC time tuple, compatible with time.localtime(). """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        pass

    def __long__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __rdiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

NaT = None # (!) real value is ''

nat_strings = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'NPY_NAT': None, # (!) real value is ''
    '_nat_scalar_rules': None, # (!) real value is ''
    'checknull_with_nat': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {}

