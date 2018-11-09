# encoding: utf-8
# module lxml.etree
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37-32\lib\site-packages\lxml\etree.cp37-win32.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class RelaxNGErrorTypes(object):
    """ Libxml2 RelaxNG error types """
    def _getName(self, *args, **kwargs): # real signature unknown
        """ Return the value for key if key is in the dictionary, else default. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    RELAXNG_ERR_ATTREXTRANS = 20
    RELAXNG_ERR_ATTRNAME = 14
    RELAXNG_ERR_ATTRNONS = 16
    RELAXNG_ERR_ATTRVALID = 24
    RELAXNG_ERR_ATTRWRONGNS = 18
    RELAXNG_ERR_CONTENTVALID = 25
    RELAXNG_ERR_DATAELEM = 28
    RELAXNG_ERR_DATATYPE = 31
    RELAXNG_ERR_DUPID = 4
    RELAXNG_ERR_ELEMEXTRANS = 19
    RELAXNG_ERR_ELEMNAME = 13
    RELAXNG_ERR_ELEMNONS = 15
    RELAXNG_ERR_ELEMNOTEMPTY = 21
    RELAXNG_ERR_ELEMWRONG = 38
    RELAXNG_ERR_ELEMWRONGNS = 17
    RELAXNG_ERR_EXTRACONTENT = 26
    RELAXNG_ERR_EXTRADATA = 35
    RELAXNG_ERR_INTEREXTRA = 12
    RELAXNG_ERR_INTERNAL = 37
    RELAXNG_ERR_INTERNODATA = 10
    RELAXNG_ERR_INTERSEQ = 11
    RELAXNG_ERR_INVALIDATTR = 27
    RELAXNG_ERR_LACKDATA = 36
    RELAXNG_ERR_LIST = 33
    RELAXNG_ERR_LISTELEM = 30
    RELAXNG_ERR_LISTEMPTY = 9
    RELAXNG_ERR_LISTEXTRA = 8
    RELAXNG_ERR_MEMORY = 1
    RELAXNG_ERR_NODEFINE = 7
    RELAXNG_ERR_NOELEM = 22
    RELAXNG_ERR_NOGRAMMAR = 34
    RELAXNG_ERR_NOSTATE = 6
    RELAXNG_ERR_NOTELEM = 23
    RELAXNG_ERR_TEXTWRONG = 39
    RELAXNG_ERR_TYPE = 2
    RELAXNG_ERR_TYPECMP = 5
    RELAXNG_ERR_TYPEVAL = 3
    RELAXNG_ERR_VALELEM = 29
    RELAXNG_ERR_VALUE = 32
    RELAXNG_OK = 0
    _names = {
        0: 'RELAXNG_OK',
        1: 'RELAXNG_ERR_MEMORY',
        2: 'RELAXNG_ERR_TYPE',
        3: 'RELAXNG_ERR_TYPEVAL',
        4: 'RELAXNG_ERR_DUPID',
        5: 'RELAXNG_ERR_TYPECMP',
        6: 'RELAXNG_ERR_NOSTATE',
        7: 'RELAXNG_ERR_NODEFINE',
        8: 'RELAXNG_ERR_LISTEXTRA',
        9: 'RELAXNG_ERR_LISTEMPTY',
        10: 'RELAXNG_ERR_INTERNODATA',
        11: 'RELAXNG_ERR_INTERSEQ',
        12: 'RELAXNG_ERR_INTEREXTRA',
        13: 'RELAXNG_ERR_ELEMNAME',
        14: 'RELAXNG_ERR_ATTRNAME',
        15: 'RELAXNG_ERR_ELEMNONS',
        16: 'RELAXNG_ERR_ATTRNONS',
        17: 'RELAXNG_ERR_ELEMWRONGNS',
        18: 'RELAXNG_ERR_ATTRWRONGNS',
        19: 'RELAXNG_ERR_ELEMEXTRANS',
        20: 'RELAXNG_ERR_ATTREXTRANS',
        21: 'RELAXNG_ERR_ELEMNOTEMPTY',
        22: 'RELAXNG_ERR_NOELEM',
        23: 'RELAXNG_ERR_NOTELEM',
        24: 'RELAXNG_ERR_ATTRVALID',
        25: 'RELAXNG_ERR_CONTENTVALID',
        26: 'RELAXNG_ERR_EXTRACONTENT',
        27: 'RELAXNG_ERR_INVALIDATTR',
        28: 'RELAXNG_ERR_DATAELEM',
        29: 'RELAXNG_ERR_VALELEM',
        30: 'RELAXNG_ERR_LISTELEM',
        31: 'RELAXNG_ERR_DATATYPE',
        32: 'RELAXNG_ERR_VALUE',
        33: 'RELAXNG_ERR_LIST',
        34: 'RELAXNG_ERR_NOGRAMMAR',
        35: 'RELAXNG_ERR_EXTRADATA',
        36: 'RELAXNG_ERR_LACKDATA',
        37: 'RELAXNG_ERR_INTERNAL',
        38: 'RELAXNG_ERR_ELEMWRONG',
        39: 'RELAXNG_ERR_TEXTWRONG',
    }
    __dict__ = None # (!) real value is ''

