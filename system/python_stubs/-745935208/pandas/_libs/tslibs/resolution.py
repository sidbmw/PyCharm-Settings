# encoding: utf-8
# module pandas._libs.tslibs.resolution
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\_libs\tslibs\resolution.cp37-win_amd64.pyd
# by generator 1.146
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\__init__.py
from pandas._libs.properties import cache_readonly

from pandas._libs.tslibs.conversion import tz_convert

from pandas._libs.tslibs.fields import build_field_sarray

from pandas._libs.tslibs.timestamps import Timestamp


# Variables with simple values

_ONE_DAY = 86400000000000
_ONE_HOUR = 3600000000000
_ONE_MICRO = 1000
_ONE_MILLI = 1000000
_ONE_MINUTE = 60000000000
_ONE_SECOND = 1000000000

# functions

def get_freq_group(W_MON): # real signature unknown; restored from __doc__
    """
    Return frequency code group of given frequency str or offset.
    
        Example
        -------
        >>> get_freq_group('W-MON')
        4000
    
        >>> get_freq_group('W-FRI')
        4000
    """
    pass

def resolution(*args, **kwargs): # real signature unknown
    pass

def unique(values): # reliably restored by inspect
    """
    Hash table-based unique. Uniques are returned in order
        of appearance. This does NOT sort.
    
        Significantly faster than numpy.unique. Includes NA values.
    
        Parameters
        ----------
        values : 1d array-like
    
        Returns
        -------
        unique values.
          - If the input is an Index, the return is an Index
          - If the input is a Categorical dtype, the return is a Categorical
          - If the input is a Series/ndarray, the return will be an ndarray
    
        Examples
        --------
        >>> pd.unique(pd.Series([2, 1, 3, 3]))
        array([2, 1, 3])
    
        >>> pd.unique(pd.Series([2] + [1] * 5))
        array([2, 1])
    
        >>> pd.unique(Series([pd.Timestamp('20160101'),
        ...                   pd.Timestamp('20160101')]))
        array(['2016-01-01T00:00:00.000000000'], dtype='datetime64[ns]')
    
        >>> pd.unique(pd.Series([pd.Timestamp('20160101', tz='US/Eastern'),
        ...                      pd.Timestamp('20160101', tz='US/Eastern')]))
        array([Timestamp('2016-01-01 00:00:00-0500', tz='US/Eastern')],
              dtype=object)
    
        >>> pd.unique(pd.Index([pd.Timestamp('20160101', tz='US/Eastern'),
        ...                     pd.Timestamp('20160101', tz='US/Eastern')]))
        DatetimeIndex(['2016-01-01 00:00:00-05:00'],
        ...           dtype='datetime64[ns, US/Eastern]', freq=None)
    
        >>> pd.unique(list('baabc'))
        array(['b', 'a', 'c'], dtype=object)
    
        An unordered Categorical will return categories in the
        order of appearance.
    
        >>> pd.unique(Series(pd.Categorical(list('baabc'))))
        [b, a, c]
        Categories (3, object): [b, a, c]
    
        >>> pd.unique(Series(pd.Categorical(list('baabc'),
        ...                                 categories=list('abc'))))
        [b, a, c]
        Categories (3, object): [b, a, c]
    
        An ordered Categorical preserves the category ordering.
    
        >>> pd.unique(Series(pd.Categorical(list('baabc'),
        ...                                 categories=list('abc'),
        ...                                 ordered=True)))
        [b, a, c]
        Categories (3, object): [a < b < c]
    
        An array of tuples
    
        >>> pd.unique([('a', 'b'), ('b', 'a'), ('a', 'c'), ('b', 'a')])
        array([('a', 'b'), ('b', 'a'), ('a', 'c')], dtype=object)
    
        See Also
        --------
        pandas.Index.unique
        pandas.Series.unique
    """
    pass

def _is_multiple(*args, **kwargs): # real signature unknown
    pass

def _maybe_add_count(*args, **kwargs): # real signature unknown
    pass

# classes

class Resolution(object):
    # no doc
    @classmethod
    def get_freq(cls, day): # real signature unknown; restored from __doc__
        """
        Return frequency str against resolution str.
        
                Example
                -------
                >>> f.Resolution.get_freq('day')
                'D'
        """
        pass

    @classmethod
    def get_freq_group(cls, day): # real signature unknown; restored from __doc__
        """
        Return frequency str against resolution str.
        
                Example
                -------
                >>> f.Resolution.get_freq_group('day')
                4000
        """
        pass

    @classmethod
    def get_reso(cls, second): # real signature unknown; restored from __doc__
        """
        Return resolution str against resolution code.
        
                Example
                -------
                >>> Resolution.get_reso('second')
                2
        
                >>> Resolution.get_reso('second') == Resolution.RESO_SEC
                True
        """
        pass

    @classmethod
    def get_reso_from_freq(cls, H): # real signature unknown; restored from __doc__
        """
        Return resolution code against frequency str.
        
                Example
                -------
                >>> Resolution.get_reso_from_freq('H')
                4
        
                >>> Resolution.get_reso_from_freq('H') == Resolution.RESO_HR
                True
        """
        pass

    @classmethod
    def get_str(cls, Resolution_RESO_SEC): # real signature unknown; restored from __doc__
        """
        Return resolution str against resolution code.
        
                Example
                -------
                >>> Resolution.get_str(Resolution.RESO_SEC)
                'second'
        """
        pass

    @classmethod
    def get_stride_from_decimal(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Convert freq with decimal stride into a higher freq with integer stride
        
                Parameters
                ----------
                value : integer or float
                freq : string
                    Frequency string
        
                Raises
                ------
                ValueError
                    If the float cannot be converted to an integer at any resolution.
        
                Example
                -------
                >>> Resolution.get_stride_from_decimal(1.5, 'T')
                (90, 'S')
        
                >>> Resolution.get_stride_from_decimal(1.04, 'H')
                (3744, 'S')
        
                >>> Resolution.get_stride_from_decimal(1, 'D')
                (1, 'D')
        """
        pass

    @classmethod
    def get_str_from_freq(cls, H): # real signature unknown; restored from __doc__
        """
        Return resolution str against frequency str.
        
                Example
                -------
                >>> Resolution.get_str_from_freq('H')
                'hour'
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    RESO_DAY = 6
    RESO_HR = 5
    RESO_MIN = 4
    RESO_MS = 2
    RESO_NS = 0
    RESO_SEC = 3
    RESO_US = 1
    _freq_reso_map = {
        'A': 'year',
        'D': 'day',
        'H': 'hour',
        'L': 'millisecond',
        'M': 'month',
        'N': 'nanosecond',
        'Q': 'quarter',
        'S': 'second',
        'T': 'minute',
        'U': 'microsecond',
    }
    _reso_freq_map = {
        'day': 'D',
        'hour': 'H',
        'microsecond': 'U',
        'millisecond': 'L',
        'minute': 'T',
        'month': 'M',
        'nanosecond': 'N',
        'quarter': 'Q',
        'second': 'S',
        'year': 'A',
    }
    _reso_mult_map = {
        0: None,
        1: 1000,
        2: 1000,
        3: 1000,
        4: 60,
        5: 60,
        6: 24,
    }
    _reso_str_bump_map = {
        'D': 'H',
        'H': 'T',
        'L': 'U',
        'N': None,
        'S': 'L',
        'T': 'S',
        'U': 'N',
    }
    _reso_str_map = {
        0: 'nanosecond',
        1: 'microsecond',
        2: 'millisecond',
        3: 'second',
        4: 'minute',
        5: 'hour',
        6: 'day',
    }
    _str_reso_map = {
        'day': 6,
        'hour': 5,
        'microsecond': 1,
        'millisecond': 2,
        'minute': 4,
        'nanosecond': 0,
        'second': 3,
    }
    __dict__ = None # (!) real value is ''


class _FrequencyInferer(object):
    """ Not sure if I can avoid the state machine here """
    def get_freq(self, *args, **kwargs): # real signature unknown
        pass

    def month_position_check(self, *args, **kwargs): # real signature unknown
        pass

    def _get_annual_rule(self, *args, **kwargs): # real signature unknown
        pass

    def _get_monthly_rule(self, *args, **kwargs): # real signature unknown
        pass

    def _get_quarterly_rule(self, *args, **kwargs): # real signature unknown
        pass

    def _get_wom_rule(self, *args, **kwargs): # real signature unknown
        pass

    def _infer_daily_rule(self, *args, **kwargs): # real signature unknown
        pass

    def _is_business_daily(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    day_deltas = None # (!) real value is ''
    deltas = None # (!) real value is ''
    deltas_asi8 = None # (!) real value is ''
    fields = None # (!) real value is ''
    hour_deltas = None # (!) real value is ''
    is_unique = None # (!) real value is ''
    is_unique_asi8 = None # (!) real value is ''
    mdiffs = None # (!) real value is ''
    rep_stamp = None # (!) real value is ''
    ydiffs = None # (!) real value is ''
    __dict__ = None # (!) real value is ''


class _TimedeltaFrequencyInferer(_FrequencyInferer):
    # no doc
    def _infer_daily_rule(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

int_to_weekday = {
    0: 'MON',
    1: 'TUE',
    2: 'WED',
    3: 'THU',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN',
}

MONTH_ALIASES = {
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC',
}

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {
    'Resolution.get_freq (line 267)': "\n        Return frequency str against resolution str.\n\n        Example\n        -------\n        >>> f.Resolution.get_freq('day')\n        'D'\n        ",
    'Resolution.get_freq_group (line 255)': "\n        Return frequency str against resolution str.\n\n        Example\n        -------\n        >>> f.Resolution.get_freq_group('day')\n        4000\n        ",
    'Resolution.get_reso (line 240)': "\n        Return resolution str against resolution code.\n\n        Example\n        -------\n        >>> Resolution.get_reso('second')\n        2\n\n        >>> Resolution.get_reso('second') == Resolution.RESO_SEC\n        True\n        ",
    'Resolution.get_reso_from_freq (line 291)': "\n        Return resolution code against frequency str.\n\n        Example\n        -------\n        >>> Resolution.get_reso_from_freq('H')\n        4\n\n        >>> Resolution.get_reso_from_freq('H') == Resolution.RESO_HR\n        True\n        ",
    'Resolution.get_str (line 228)': "\n        Return resolution str against resolution code.\n\n        Example\n        -------\n        >>> Resolution.get_str(Resolution.RESO_SEC)\n        'second'\n        ",
    'Resolution.get_str_from_freq (line 279)': "\n        Return resolution str against frequency str.\n\n        Example\n        -------\n        >>> Resolution.get_str_from_freq('H')\n        'hour'\n        ",
    'Resolution.get_stride_from_decimal (line 306)': "\n        Convert freq with decimal stride into a higher freq with integer stride\n\n        Parameters\n        ----------\n        value : integer or float\n        freq : string\n            Frequency string\n\n        Raises\n        ------\n        ValueError\n            If the float cannot be converted to an integer at any resolution.\n\n        Example\n        -------\n        >>> Resolution.get_stride_from_decimal(1.5, 'T')\n        (90, 'S')\n\n        >>> Resolution.get_stride_from_decimal(1.04, 'H')\n        (3744, 'S')\n\n        >>> Resolution.get_stride_from_decimal(1, 'D')\n        (1, 'D')\n        ",
    'get_freq_group (line 145)': "\n    Return frequency code group of given frequency str or offset.\n\n    Example\n    -------\n    >>> get_freq_group('W-MON')\n    4000\n\n    >>> get_freq_group('W-FRI')\n    4000\n    ",
}

