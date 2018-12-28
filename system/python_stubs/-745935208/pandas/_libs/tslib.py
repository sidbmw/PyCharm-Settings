# encoding: utf-8
# module pandas._libs.tslib
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\_libs\tslib.cp37-win_amd64.pyd
# by generator 1.146
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\__init__.py
import pytz as pytz # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pytz\__init__.py
from pandas._libs.tslibs.conversion import tz_convert_single

from pandas._libs.tslibs.nattype import NaT

from pandas._libs.tslibs.np_datetime import OutOfBoundsDatetime

from pandas._libs.tslibs.parsing import parse_datetime_string

from pandas._libs.tslibs.timedeltas import Timedelta

from pandas._libs.tslibs.timestamps import Timestamp


# Variables with simple values

iNaT = -9223372036854775808

# functions

def array_to_datetime(*args, **kwargs): # real signature unknown
    pass

def array_with_unit_to_datetime(*args, **kwargs): # real signature unknown
    """
    convert the ndarray according to the unit
        if errors:
          - raise: return converted values or raise OutOfBoundsDatetime
              if out of range on the conversion or
              ValueError for other conversions (e.g. a string)
          - ignore: return non-convertible values as the same unit
          - coerce: NaT for non-convertibles
    """
    pass

def format_array_from_datetime(*args, **kwargs): # real signature unknown
    """
    return a np object array of the string formatted values
    
        Parameters
        ----------
        values : a 1-d i8 array
        tz : the timezone (or None)
        format : optional, default is None
              a strftime capable string
        na_rep : optional, default is None
              a nat format
    """
    pass

def ints_to_pydatetime(*args, **kwargs): # real signature unknown
    """
    Convert an i8 repr to an ndarray of datetimes, date, time or Timestamp
    
        Parameters
        ----------
        arr  : array of i8
        tz   : str, default None
             convert to this timezone
        freq : str/Offset, default None
             freq to convert
        box  : {'datetime', 'timestamp', 'date', 'time'}, default 'datetime'
             If datetime, convert to datetime.datetime
             If date, convert to datetime.date
             If time, convert to datetime.time
             If Timestamp, convert to pandas.Timestamp
    
        Returns
        -------
        result : array of dtype specified by box
    """
    pass

def ints_to_pytimedelta(*args, **kwargs): # real signature unknown
    pass

def monthrange(*args, **kwargs): # real signature unknown
    pass

def normalize_date(*args, **kwargs): # real signature unknown
    """
    Normalize datetime.datetime value to midnight. Returns datetime.date as a
        datetime.datetime at midnight
    
        Returns
        -------
        normalized : datetime.datetime or Timestamp
    """
    pass

def _localize_pydatetime(*args, **kwargs): # real signature unknown
    """ Take a datetime/Timestamp in UTC and localizes to timezone tz. """
    pass

def _test_parse_iso8601(*args, **kwargs): # real signature unknown
    """
    TESTING ONLY: Parse string into Timestamp using iso8601 parser. Used
        only for testing, actual construction uses `convert_str_to_tsobject`
    """
    pass

# no classes
# variables with complex values

nat_strings = None # (!) real value is ''

UTC = pytz.UTC

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

