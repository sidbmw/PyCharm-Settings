# encoding: utf-8
# module pandas._libs.tslibs.timedeltas
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\_libs\tslibs\timedeltas.cp37-win_amd64.pyd
# by generator 1.146
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import collections as collections # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\collections\__init__.py
import textwrap as textwrap # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\textwrap.py
import warnings as warnings # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\warnings.py
import sys as sys # <module 'sys' (built-in)>
import numpy as np # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.nattype import NaT

import datetime as __datetime


# functions

def array_to_timedelta64(*args, **kwargs): # real signature unknown
    """
    Convert an ndarray to an array of timedeltas. If errors == 'coerce',
        coerce non-convertible objects to NaT. Otherwise, raise.
    """
    pass

def cast_from_unit(*args, **kwargs): # real signature unknown
    """
    return a casting of the unit represented to nanoseconds
            round the fractional part of a float to our precision, p
    """
    pass

def convert_to_timedelta64(*args, **kwargs): # real signature unknown
    """
    Convert an incoming object to a timedelta64 if possible
    
        Handle these types of objects:
            - timedelta/Timedelta
            - timedelta64
            - an offset
            - np.int64 (with unit providing a possible modifier)
            - None/NaT
    
        Return an ns based int64
    
        # kludgy here until we have a timedelta scalar
        # handle the numpy < 1.7 case
    """
    pass

def delta_to_nanoseconds(*args, **kwargs): # real signature unknown
    pass

def _binary_op_method_timedeltalike(*args, **kwargs): # real signature unknown
    pass

def _op_unary_method(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__Timedelta(*args, **kwargs): # real signature unknown
    pass

# classes

class Components(tuple):
    """ Components(days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Components object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new Components object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds): # reliably restored by inspect
        """ Create new instance of Components(days, hours, minutes, seconds, milliseconds, microseconds, nanoseconds) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 5"""

    milliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 4"""

    minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 6"""

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""


    _fields = (
        'days',
        'hours',
        'minutes',
        'seconds',
        'milliseconds',
        'microseconds',
        'nanoseconds',
    )
    _fields_defaults = {}
    __slots__ = ()


class _Timedelta(__datetime.timedelta):
    # no doc
    def isoformat(self): # real signature unknown; restored from __doc__
        """
        Format Timedelta as ISO 8601 Duration like
                ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``, where the ``[n]`` s are replaced by the
                values. See https://en.wikipedia.org/wiki/ISO_8601#Durations
        
                .. versionadded:: 0.20.0
        
                Returns
                -------
                formatted : str
        
                Notes
                -----
                The longest component is days, whose value may be larger than
                365.
                Every component is always included, even if its value is 0.
                Pandas uses nanosecond precision, so up to 9 decimal places may
                be included in the seconds component.
                Trailing 0's are removed from the seconds component after the decimal.
                We do not 0 pad components, so it's `...T5H...`, not `...T05H...`
        
                Examples
                --------
                >>> td = pd.Timedelta(days=6, minutes=50, seconds=3,
                ...                   milliseconds=10, microseconds=10, nanoseconds=12)
                >>> td.isoformat()
                'P6DT0H50M3.010010012S'
                >>> pd.Timedelta(hours=1, seconds=10).isoformat()
                'P0DT0H0M10S'
                >>> pd.Timedelta(hours=1, seconds=10).isoformat()
                'P0DT0H0M10S'
                >>> pd.Timedelta(days=500.5).isoformat()
                'P500DT12H0MS'
        
                See Also
                --------
                Timestamp.isoformat
        """
        pass

    def total_seconds(self, *args, **kwargs): # real signature unknown
        """ Total duration of timedelta in seconds (to ns precision) """
        pass

    def to_pytimedelta(self, *args, **kwargs): # real signature unknown
        """
        return an actual datetime.timedelta object
                note: we lose nanosecond resolution if any
        """
        pass

    def to_timedelta64(self, *args, **kwargs): # real signature unknown
        """ Returns a numpy.timedelta64 object with 'ns' precision """
        pass

    def view(self, *args, **kwargs): # real signature unknown
        """ array view compat """
        pass

    def _ensure_components(self, *args, **kwargs): # real signature unknown
        """ compute the components """
        pass

    def _has_ns(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_base(self, *args, **kwargs): # real signature unknown
        """
        Parameters
                ----------
                format : None|all|sub_day|long
        
                Returns
                -------
                converted : string of a Timedelta
        """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
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

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ return a numpy timedelta64 array view of myself """

    components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ Return a Components NamedTuple-like """

    delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the timedelta in nanoseconds (ns), for internal compatibility.

        Returns
        -------
        int
            Timedelta in nanoseconds.

        Examples
        --------
        >>> td = pd.Timedelta('1 days 42 ns')
        >>> td.delta
        86400000000042

        >>> td = pd.Timedelta('3 s')
        >>> td.delta
        3000000000

        >>> td = pd.Timedelta('3 ms 5 us')
        >>> td.delta
        3005000

        >>> td = pd.Timedelta(42, unit='ns')
        >>> td.delta
        42
        """

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_populated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.
       
        Returns
        -------
        int
            Number of nanoseconds.

        See Also
        --------
        Timedelta.components : Return all attributes with assigned values
            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,
            nanoseconds).

        Examples
        --------
        **Using string input**

        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')
        >>> td.nanoseconds
        42

        **Using integer input**

        >>> td = pd.Timedelta(42, unit='ns')
        >>> td.nanoseconds
        42
        """

    resolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ return a string representing the lowest resolution that we have """

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _h = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _s = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _us = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __array_priority__ = 100
    __pyx_vtable__ = None # (!) real value is ''


class Timedelta(_Timedelta):
    """
    Represents a duration, the difference between two dates or times.
    
        Timedelta is the pandas equivalent of python's ``datetime.timedelta``
        and is interchangeable with it in most cases.
    
        Parameters
        ----------
        value : Timedelta, timedelta, np.timedelta64, string, or integer
        unit : string, {'ns', 'us', 'ms', 's', 'm', 'h', 'D'}, optional
            Denote the unit of the input, if input is an integer. Default 'ns'.
        days, seconds, microseconds,
        milliseconds, minutes, hours, weeks : numeric, optional
            Values for construction in compat with datetime.timedelta.
            np ints and floats will be coereced to python ints and floats.
    
        Notes
        -----
        The ``.value`` attribute is always in ns.
    """
    def ceil(self, *args, **kwargs): # real signature unknown
        """
        return a new Timedelta ceiled to this resolution
        
                Parameters
                ----------
                freq : a freq string indicating the ceiling resolution
        """
        pass

    def floor(self, *args, **kwargs): # real signature unknown
        """
        return a new Timedelta floored to this resolution
        
                Parameters
                ----------
                freq : a freq string indicating the flooring resolution
        """
        pass

    def round(self, *args, **kwargs): # real signature unknown
        """
        Round the Timedelta to the specified resolution
        
                Returns
                -------
                a new Timedelta rounded to the given resolution of `freq`
        
                Parameters
                ----------
                freq : a freq string indicating the rounding resolution
        
                Raises
                ------
                ValueError if the freq cannot be converted
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __inv__(self, *args, **kwargs): # real signature unknown
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    __dict__ = None # (!) real value is ''


# variables with complex values

nat_strings = None # (!) real value is ''

_no_input = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__pyx_capi__ = {
    'array_to_timedelta64': None, # (!) real value is ''
    'cast_from_unit': None, # (!) real value is ''
    'convert_to_timedelta64': None, # (!) real value is ''
    'delta_to_nanoseconds': None, # (!) real value is ''
    'parse_timedelta_string': None, # (!) real value is ''
}

__spec__ = None # (!) real value is ''

__test__ = {
    '_Timedelta.delta.__get__ (line 762)': "\n        Return the timedelta in nanoseconds (ns), for internal compatibility.\n\n        Returns\n        -------\n        int\n            Timedelta in nanoseconds.\n\n        Examples\n        --------\n        >>> td = pd.Timedelta('1 days 42 ns')\n        >>> td.delta\n        86400000000042\n\n        >>> td = pd.Timedelta('3 s')\n        >>> td.delta\n        3000000000\n\n        >>> td = pd.Timedelta('3 ms 5 us')\n        >>> td.delta\n        3005000\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.delta\n        42\n        ",
    '_Timedelta.isoformat (line 905)': "\n        Format Timedelta as ISO 8601 Duration like\n        ``P[n]Y[n]M[n]DT[n]H[n]M[n]S``, where the ``[n]`` s are replaced by the\n        values. See https://en.wikipedia.org/wiki/ISO_8601#Durations\n\n        .. versionadded:: 0.20.0\n\n        Returns\n        -------\n        formatted : str\n\n        Notes\n        -----\n        The longest component is days, whose value may be larger than\n        365.\n        Every component is always included, even if its value is 0.\n        Pandas uses nanosecond precision, so up to 9 decimal places may\n        be included in the seconds component.\n        Trailing 0's are removed from the seconds component after the decimal.\n        We do not 0 pad components, so it's `...T5H...`, not `...T05H...`\n\n        Examples\n        --------\n        >>> td = pd.Timedelta(days=6, minutes=50, seconds=3,\n        ...                   milliseconds=10, microseconds=10, nanoseconds=12)\n        >>> td.isoformat()\n        'P6DT0H50M3.010010012S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT0H0M10S'\n        >>> pd.Timedelta(hours=1, seconds=10).isoformat()\n        'P0DT0H0M10S'\n        >>> pd.Timedelta(days=500.5).isoformat()\n        'P500DT12H0MS'\n\n        See Also\n        --------\n        Timestamp.isoformat\n        ",
    '_Timedelta.nanoseconds.__get__ (line 817)': "\n        Return the number of nanoseconds (n), where 0 <= n < 1 microsecond.\n       \n        Returns\n        -------\n        int\n            Number of nanoseconds.\n\n        See Also\n        --------\n        Timedelta.components : Return all attributes with assigned values\n            (i.e. days, hours, minutes, seconds, milliseconds, microseconds,\n            nanoseconds).\n\n        Examples\n        --------\n        **Using string input**\n\n        >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns')\n        >>> td.nanoseconds\n        42\n\n        **Using integer input**\n\n        >>> td = pd.Timedelta(42, unit='ns')\n        >>> td.nanoseconds\n        42\n        ",
}

