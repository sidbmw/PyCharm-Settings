# encoding: utf-8
# module lxml.etree
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37-32\lib\site-packages\lxml\etree.cp37-win32.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._ElementMatchIterator import _ElementMatchIterator

class SiblingsIterator(_ElementMatchIterator):
    """
    SiblingsIterator(self, node, tag=None, preceding=False)
        Iterates over the siblings of an element.
    
        You can pass the boolean keyword ``preceding`` to specify the direction.
    """
    def __init__(self, node, tag=None, preceding=False): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


