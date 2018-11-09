# encoding: utf-8
# module cx_Oracle
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37-32\lib\site-packages\cx_Oracle.cp37-win32.pyd
# by generator 1.145
# no doc

# imports
import datetime as __datetime


from .object import object

class Date(object):
    """ date(year, month, day) --> date object """
    def ctime(self): # real signature unknown; restored from __doc__
        """ Return ctime() style string. """
        pass

    @classmethod
    def fromisoformat(cls, *args, **kwargs): # real signature unknown
        """ str -> Construct a date from the output of date.isoformat() """
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown
        """ int -> date corresponding to a proleptic Gregorian ordinal. """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown
        """ timestamp -> local date from a POSIX timestamp (like time.time()). """
        pass

    def isocalendar(self, *args, **kwargs): # real signature unknown
        """ Return a 3-tuple containing ISO year, week number, and weekday. """
        pass

    def isoformat(self, *args, **kwargs): # real signature unknown
        """ Return string in ISO 8601 format, YYYY-MM-DD. """
        pass

    def isoweekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 1 ... Sunday == 7
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return date with new specified fields. """
        pass

    def strftime(self): # real signature unknown; restored from __doc__
        """ format -> strftime() style string. """
        pass

    def timetuple(self, *args, **kwargs): # real signature unknown
        """ Return time tuple, compatible with time.localtime(). """
        pass

    @classmethod
    def today(cls, *args, **kwargs): # real signature unknown
        """ Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). """
        pass

    def toordinal(self, *args, **kwargs): # real signature unknown
        """ Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. """
        pass

    def weekday(self, *args, **kwargs): # real signature unknown
        """
        Return the day of the week represented by the date.
        Monday == 0 ... Sunday == 6
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """ __reduce__() -> (cls, state) """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = None # (!) real value is ''
    min = None # (!) real value is ''
    resolution = None # (!) real value is ''


