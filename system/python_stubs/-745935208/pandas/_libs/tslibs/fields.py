# encoding: utf-8
# module pandas._libs.tslibs.fields
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\_libs\tslibs\fields.cp37-win_amd64.pyd
# by generator 1.146
"""
Functions for accessing attributes of Timestamp/datetime64/datetime-like
objects and arrays
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.ccalendar import get_locale_names


# functions

def build_field_sarray(*args, **kwargs): # real signature unknown
    """ Datetime as int64 representation to a structured array of fields """
    pass

def get_date_field(*args, **kwargs): # real signature unknown
    """
    Given a int64-based datetime index, extract the year, month, etc.,
        field and return an array of these values.
    """
    pass

def get_date_name_field(*args, **kwargs): # real signature unknown
    """
    Given a int64-based datetime index, return array of strings of date
        name based on requested field (e.g. weekday_name)
    """
    pass

def get_start_end_field(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index return array of indicators
        of whether timestamps are at the start/end of the month/quarter/year
        (defined by frequency).
    """
    pass

def get_timedelta_field(*args, **kwargs): # real signature unknown
    """
    Given a int64-based timedelta index, extract the days, hrs, sec.,
        field and return an array of these values.
    """
    pass

def get_time_micros(*args, **kwargs): # real signature unknown
    """
    Return the number of microseconds in the time component of a
        nanosecond timestamp.
    
        Parameters
        ----------
        dtindex : ndarray[int64_t]
    
        Returns
        -------
        micros : ndarray[int64_t]
    """
    pass

def isleapyear_arr(*args, **kwargs): # real signature unknown
    """ vectorized version of isleapyear; NaT evaluates as False """
    pass

# no classes
# variables with complex values

DAYS_FULL = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

MONTHS_FULL = [
    '',
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

