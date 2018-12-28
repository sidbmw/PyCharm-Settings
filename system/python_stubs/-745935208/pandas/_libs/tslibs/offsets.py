# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\_libs\tslibs\offsets.cp37-win_amd64.pyd
# by generator 1.146
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import time as time # <module 'time' (built-in)>
import numpy as np # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\__init__.py

# Variables with simple values

key = 'BAS-DEC'

_alias = 'Q-DEC'

_d = 'SUN'

_m = 'DEC'

__prefix = 'Q'

# functions

def apply_index_wraps(*args, **kwargs): # real signature unknown
    pass

def as_datetime(*args, **kwargs): # real signature unknown
    pass

def get_day_of_month(other, start): # real signature unknown; restored from __doc__
    """
    Find the day in `other`'s month that satisfies a DateOffset's onOffset
        policy, as described by the `day_opt` argument.
    
        Parameters
        ----------
        other : datetime or Timestamp
        day_opt : 'start', 'end'
            'start': returns 1
            'end': returns last day of the month
    
        Returns
        -------
        day_of_month : int
    
        Examples
        -------
        >>> other = datetime(2017, 11, 14)
        >>> get_day_of_month(other, 'start')
        1
        >>> get_day_of_month(other, 'end')
        30
    """
    pass

def get_firstbday(*args, **kwargs): # real signature unknown
    """
    Find the first day of the month that is a business day.
    
        Parameters
        ----------
        year : int
        month : int
    
        Returns
        -------
        first_bday : int
    """
    pass

def get_lastbday(*args, **kwargs): # real signature unknown
    """
    Find the last day of the month that is a business day.
    
        Parameters
        ----------
        year : int
        month : int
    
        Returns
        -------
        last_bday : int
    """
    pass

def roll_convention(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : int, generally the day component of a datetime
        n : number of periods to increment, before adjusting for rolling
        compare : int, generally the day component of a datetime, in the same
                  month as the datetime form which `other` was taken.
    
        Returns
        -------
        n : int number of periods to increment
    """
    pass

def roll_qtrday(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : datetime or Timestamp
        n : number of periods to increment, before adjusting for rolling
        month : int reference month giving the first month of the year
        day_opt : 'start', 'end', 'business_start', 'business_end'
            The convention to use in finding the day in a given month against
            which to compare for rollforward/rollbackward decisions.
        modby : int 3 for quarters, 12 for years
    
        Returns
        -------
        n : int number of periods to increment
    """
    pass

def roll_yearday(other, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : datetime or Timestamp
        n : number of periods to increment, before adjusting for rolling
        month : reference month giving the first month of the year
        day_opt : 'start', 'end'
            'start': returns 1
            'end': returns last day of the month
    
        Returns
        -------
        n : int number of periods to increment
    
        Notes
        -----
        * Mirrors `roll_check` in shift_months
    
        Examples
        -------
        >>> month = 3
        >>> day_opt = 'start'              # `other` will be compared to March 1
        >>> other = datetime(2017, 2, 10)  # before March 1
        >>> roll_yearday(other, 2, month, day_opt)
        1
        >>> roll_yearday(other, -7, month, day_opt)
        -7
        >>>
        >>> other = Timestamp('2014-03-15', tz='US/Eastern')  # after March 1
        >>> roll_yearday(other, 2, month, day_opt)
        2
        >>> roll_yearday(other, -7, month, day_opt)
        -6
    
        >>> month = 6
        >>> day_opt = 'end'                # `other` will be compared to June 30
        >>> other = datetime(1999, 6, 29)  # before June 30
        >>> roll_yearday(other, 5, month, day_opt)
        4
        >>> roll_yearday(other, -7, month, day_opt)
        -7
        >>>
        >>> other = Timestamp(2072, 8, 24, 6, 17, 18)  # after June 30
        >>> roll_yearday(other, 5, month, day_opt)
        5
        >>> roll_yearday(other, -7, month, day_opt)
        -6
    """
    pass

def shift_month(*args, **kwargs): # real signature unknown
    """
    Given a datetime (or Timestamp) `stamp`, an integer `months` and an
        option `day_opt`, return a new datetimelike that many months later,
        with day determined by `day_opt` using relativedelta semantics.
    
        Scalar analogue of shift_months
    
        Parameters
        ----------
        stamp : datetime or Timestamp
        months : int
        day_opt : None, 'start', 'end', or an integer
            None: returned datetimelike has the same day as the input, or the
                  last day of the month if the new month is too short
            'start': returned datetimelike has day=1
            'end': returned datetimelike has day on the last day of the month
            int: returned datetimelike has day equal to day_opt
    
        Returns
        -------
        shifted : datetime or Timestamp (same as input `stamp`)
    """
    pass

def shift_months(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index, shift all elements
        specified number of months using DateOffset semantics
    
        day: {None, 'start', 'end'}
           * None: day of month
           * 'start' 1st day of month
           * 'end' last day of month
    """
    pass

def shift_quarters(*args, **kwargs): # real signature unknown
    """
    Given an int64 array representing nanosecond timestamps, shift all elements
        by the specified number of quarters using DateOffset semantics.
    
        Parameters
        ----------
        dtindex : int64_t[:] timestamps for input dates
        quarters : int number of quarters to shift
        q1start_month : int month in which Q1 begins by convention
        day : {'start', 'end', 'business_start', 'business_end'}
        modby : int (3 for quarters, 12 for years)
    
        Returns
        -------
        out : ndarray[int64_t]
    """
    pass

def _determine_offset(*args, **kwargs): # real signature unknown
    pass

def _get_calendar(*args, **kwargs): # real signature unknown
    """ Generate busdaycalendar """
    pass

def _is_normalized(*args, **kwargs): # real signature unknown
    pass

def _to_dt64(*args, **kwargs): # real signature unknown
    pass

def _validate_business_time(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class ApplyTypeError(TypeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class _BaseOffset(object):
    """
    Base class for DateOffset methods that are not overridden by subclasses
        and will (after pickle errors are resolved) go into a cdef class.
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        pass

    def _should_cache(self, *args, **kwargs): # real signature unknown
        pass

    def _validate_n(self, *args, **kwargs): # real signature unknown
        """
        Require that `n` be a nonzero integer.
        
                Parameters
                ----------
                n : int
        
                Returns
                -------
                nint : int
        
                Raises
                ------
                TypeError if `int(n)` raises
                ValueError if n != int(n)
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        pass

    kwds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _attributes = None # (!) real value is ''
    _cacheable = False
    _day_opt = None
    _normalize_cache = True
    _typ = 'dateoffset'
    __dict__ = None # (!) real value is ''


class BaseOffset(_BaseOffset):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass


class CacheableOffset(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _cacheable = True
    __dict__ = None # (!) real value is ''


class relativedelta(object):
    """
    The relativedelta type is based on the specification of the excellent
        work done by M.-A. Lemburg in his
        `mx.DateTime <https://www.egenix.com/products/python/mxBase/mxDateTime/>`_ extension.
        However, notice that this type does *NOT* implement the same algorithm as
        his work. Do *NOT* expect it to behave like mx.DateTime's counterpart.
    
        There are two different ways to build a relativedelta instance. The
        first one is passing it two date/datetime classes::
    
            relativedelta(datetime1, datetime2)
    
        The second one is passing it any number of the following keyword arguments::
    
            relativedelta(arg1=x,arg2=y,arg3=z...)
    
            year, month, day, hour, minute, second, microsecond:
                Absolute information (argument is singular); adding or subtracting a
                relativedelta with absolute information does not perform an arithmetic
                operation, but rather REPLACES the corresponding value in the
                original datetime with the value(s) in relativedelta.
    
            years, months, weeks, days, hours, minutes, seconds, microseconds:
                Relative information, may be negative (argument is plural); adding
                or subtracting a relativedelta with relative information performs
                the corresponding aritmetic operation on the original datetime value
                with the information in the relativedelta.
    
            weekday: 
                One of the weekday instances (MO, TU, etc). These
                instances may receive a parameter N, specifying the Nth
                weekday, which could be positive or negative (like MO(+1)
                or MO(-2). Not specifying it is the same as specifying
                +1. You can also use an integer, where 0=MO. Notice that
                if the calculated date is already Monday, for example,
                using MO(1) or MO(-1) won't change the day.
    
            leapdays:
                Will add given days to the date found, if year is a leap
                year, and the date found is post 28 of february.
    
            yearday, nlyearday:
                Set the yearday or the non-leap year day (jump leap days).
                These are converted to day/month/leapdays information.
    
        There are relative and absolute forms of the keyword
        arguments. The plural is relative, and the singular is
        absolute. For each argument in the order below, the absolute form
        is applied first (by setting each attribute to that value) and
        then the relative form (by adding the value to the attribute).
    
        The order of attributes considered when this relativedelta is
        added to a datetime is:
    
        1. Year
        2. Month
        3. Day
        4. Hours
        5. Minutes
        6. Seconds
        7. Microseconds
    
        Finally, weekday is applied, using the rule described above.
    
        For example
    
        >>> dt = datetime(2018, 4, 9, 13, 37, 0)
        >>> delta = relativedelta(hours=25, day=1, weekday=MO(1))
        datetime(2018, 4, 2, 14, 37, 0)
    
        First, the day is set to 1 (the first of the month), then 25 hours
        are added, to get to the 2nd day and 14th hour, finally the
        weekday is applied, but since the 2nd is already a Monday there is
        no effect.
    """
    def normalized(self): # reliably restored by inspect
        """
        Return a version of this object represented entirely using integer
                values for the relative attributes.
        
                >>> relativedelta(days=1.5, hours=2).normalized()
                relativedelta(days=1, hours=14)
        
                :return:
                    Returns a :class:`dateutil.relativedelta.relativedelta` object.
        """
        pass

    def _fix(self): # reliably restored by inspect
        # no doc
        pass

    def _set_months(self, months): # reliably restored by inspect
        # no doc
        pass

    def __abs__(self): # reliably restored by inspect
        # no doc
        pass

    def __add__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __div__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __hash__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, dt1=None, dt2=None, years=0, months=0, days=0, leapdays=0, weeks=0, hours=0, minutes=0, seconds=0, microseconds=0, year=None, month=None, day=None, weekday=None, yearday=None, nlyearday=None, hour=None, minute=None, second=None, microsecond=None): # reliably restored by inspect
        # no doc
        pass

    def __mul__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __neg__(self): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __nonzero__(self): # reliably restored by inspect
        # no doc
        pass

    def __radd__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __rmul__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rsub__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __sub__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __truediv__(self, other): # reliably restored by inspect
        # no doc
        pass

    weeks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class WeekDay(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FRI = 4
    MON = 0
    SAT = 5
    SUN = 6
    THU = 3
    TUE = 1
    WED = 2
    __dict__ = None # (!) real value is ''


# variables with complex values

DAYS = [
    'MON',
    'TUE',
    'WED',
    'THU',
    'FRI',
    'SAT',
    'SUN',
]

MONTHS = [
    'JAN',
    'FEB',
    'MAR',
    'APR',
    'MAY',
    'JUN',
    'JUL',
    'AUG',
    'SEP',
    'OCT',
    'NOV',
    'DEC',
]

need_suffix = [
    'QS',
    'BQ',
    'BQS',
    'YS',
    'AS',
    'BY',
    'BA',
    'BYS',
    'BAS',
]

relativedelta_kwds = None # (!) real value is ''

_offset_to_period_map = {
    'A': 'A',
    'A-APR': 'A-APR',
    'A-AUG': 'A-AUG',
    'A-DEC': 'A-DEC',
    'A-FEB': 'A-FEB',
    'A-JAN': 'A-JAN',
    'A-JUL': 'A-JUL',
    'A-JUN': 'A-JUN',
    'A-MAR': 'A-MAR',
    'A-MAY': 'A-MAY',
    'A-NOV': 'A-NOV',
    'A-OCT': 'A-OCT',
    'A-SEP': 'A-SEP',
    'AS': 'A',
    'AS-APR': 'A',
    'AS-AUG': 'A',
    'AS-DEC': 'A',
    'AS-FEB': 'A',
    'AS-JAN': 'A',
    'AS-JUL': 'A',
    'AS-JUN': 'A',
    'AS-MAR': 'A',
    'AS-MAY': 'A',
    'AS-NOV': 'A',
    'AS-OCT': 'A',
    'AS-SEP': 'A',
    'B': 'B',
    'BA': 'A',
    'BA-APR': 'A',
    'BA-AUG': 'A',
    'BA-DEC': 'A',
    'BA-FEB': 'A',
    'BA-JAN': 'A',
    'BA-JUL': 'A',
    'BA-JUN': 'A',
    'BA-MAR': 'A',
    'BA-MAY': 'A',
    'BA-NOV': 'A',
    'BA-OCT': 'A',
    'BA-SEP': 'A',
    'BAS': 'A',
    'BAS-APR': 'A',
    'BAS-AUG': 'A',
    'BAS-DEC': 'A',
    'BAS-FEB': 'A',
    'BAS-JAN': 'A',
    'BAS-JUL': 'A',
    'BAS-JUN': 'A',
    'BAS-MAR': 'A',
    'BAS-MAY': 'A',
    'BAS-NOV': 'A',
    'BAS-OCT': 'A',
    'BAS-SEP': 'A',
    'BM': 'M',
    'BQ': 'Q',
    'BQ-APR': 'Q',
    'BQ-AUG': 'Q',
    'BQ-DEC': 'Q',
    'BQ-FEB': 'Q',
    'BQ-JAN': 'Q',
    'BQ-JUL': 'Q',
    'BQ-JUN': 'Q',
    'BQ-MAR': 'Q',
    'BQ-MAY': 'Q',
    'BQ-NOV': 'Q',
    'BQ-OCT': 'Q',
    'BQ-SEP': 'Q',
    'BQS': 'Q',
    'BQS-APR': 'Q',
    'BQS-AUG': 'Q',
    'BQS-DEC': 'Q',
    'BQS-FEB': 'Q',
    'BQS-JAN': 'Q',
    'BQS-JUL': 'Q',
    'BQS-JUN': 'Q',
    'BQS-MAR': 'Q',
    'BQS-MAY': 'Q',
    'BQS-NOV': 'Q',
    'BQS-OCT': 'Q',
    'BQS-SEP': 'Q',
    'BY': 'A',
    'BY-APR': 'A',
    'BY-AUG': 'A',
    'BY-DEC': 'A',
    'BY-FEB': 'A',
    'BY-JAN': 'A',
    'BY-JUL': 'A',
    'BY-JUN': 'A',
    'BY-MAR': 'A',
    'BY-MAY': 'A',
    'BY-NOV': 'A',
    'BY-OCT': 'A',
    'BY-SEP': 'A',
    'BYS': 'A',
    'BYS-APR': 'A',
    'BYS-AUG': 'A',
    'BYS-DEC': 'A',
    'BYS-FEB': 'A',
    'BYS-JAN': 'A',
    'BYS-JUL': 'A',
    'BYS-JUN': 'A',
    'BYS-MAR': 'A',
    'BYS-MAY': 'A',
    'BYS-NOV': 'A',
    'BYS-OCT': 'A',
    'BYS-SEP': 'A',
    'C': 'C',
    'D': 'D',
    'EOM': 'M',
    'H': 'H',
    'L': 'L',
    'M': 'M',
    'MS': 'M',
    'N': 'N',
    'Q': 'Q',
    'Q-APR': 'Q-APR',
    'Q-AUG': 'Q-AUG',
    'Q-DEC': 'Q-DEC',
    'Q-FEB': 'Q-FEB',
    'Q-JAN': 'Q-JAN',
    'Q-JUL': 'Q-JUL',
    'Q-JUN': 'Q-JUN',
    'Q-MAR': 'Q-MAR',
    'Q-MAY': 'Q-MAY',
    'Q-NOV': 'Q-NOV',
    'Q-OCT': 'Q-OCT',
    'Q-SEP': 'Q-SEP',
    'QS': 'Q',
    'QS-APR': 'Q',
    'QS-AUG': 'Q',
    'QS-DEC': 'Q',
    'QS-FEB': 'Q',
    'QS-JAN': 'Q',
    'QS-JUL': 'Q',
    'QS-JUN': 'Q',
    'QS-MAR': 'Q',
    'QS-MAY': 'Q',
    'QS-NOV': 'Q',
    'QS-OCT': 'Q',
    'QS-SEP': 'Q',
    'S': 'S',
    'T': 'T',
    'U': 'U',
    'W': 'W',
    'W-FRI': 'W-FRI',
    'W-MON': 'W-MON',
    'W-SAT': 'W-SAT',
    'W-SUN': 'W-SUN',
    'W-THU': 'W-THU',
    'W-TUE': 'W-TUE',
    'W-WED': 'W-WED',
    'WEEKDAY': 'D',
    'Y': 'A',
    'YS': 'A',
    'YS-APR': 'A',
    'YS-AUG': 'A',
    'YS-DEC': 'A',
    'YS-FEB': 'A',
    'YS-JAN': 'A',
    'YS-JUL': 'A',
    'YS-JUN': 'A',
    'YS-MAR': 'A',
    'YS-MAY': 'A',
    'YS-NOV': 'A',
    'YS-OCT': 'A',
    'YS-SEP': 'A',
}

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {
    'get_day_of_month (line 757)': "\n    Find the day in `other`'s month that satisfies a DateOffset's onOffset\n    policy, as described by the `day_opt` argument.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    day_opt : 'start', 'end'\n        'start': returns 1\n        'end': returns last day of the month\n\n    Returns\n    -------\n    day_of_month : int\n\n    Examples\n    -------\n    >>> other = datetime(2017, 11, 14)\n    >>> get_day_of_month(other, 'start')\n    1\n    >>> get_day_of_month(other, 'end')\n    30\n\n    ",
    'roll_yearday (line 874)': "\n    Possibly increment or decrement the number of periods to shift\n    based on rollforward/rollbackward conventions.\n\n    Parameters\n    ----------\n    other : datetime or Timestamp\n    n : number of periods to increment, before adjusting for rolling\n    month : reference month giving the first month of the year\n    day_opt : 'start', 'end'\n        'start': returns 1\n        'end': returns last day of the month\n\n    Returns\n    -------\n    n : int number of periods to increment\n\n    Notes\n    -----\n    * Mirrors `roll_check` in shift_months\n\n    Examples\n    -------\n    >>> month = 3\n    >>> day_opt = 'start'              # `other` will be compared to March 1\n    >>> other = datetime(2017, 2, 10)  # before March 1\n    >>> roll_yearday(other, 2, month, day_opt)\n    1\n    >>> roll_yearday(other, -7, month, day_opt)\n    -7\n    >>>\n    >>> other = Timestamp('2014-03-15', tz='US/Eastern')  # after March 1\n    >>> roll_yearday(other, 2, month, day_opt)\n    2\n    >>> roll_yearday(other, -7, month, day_opt)\n    -6\n\n    >>> month = 6\n    >>> day_opt = 'end'                # `other` will be compared to June 30\n    >>> other = datetime(1999, 6, 29)  # before June 30\n    >>> roll_yearday(other, 5, month, day_opt)\n    4\n    >>> roll_yearday(other, -7, month, day_opt)\n    -7\n    >>>\n    >>> other = Timestamp(2072, 8, 24, 6, 17, 18)  # after June 30\n    >>> roll_yearday(other, 5, month, day_opt)\n    5\n    >>> roll_yearday(other, -7, month, day_opt)\n    -6\n\n    ",
}

