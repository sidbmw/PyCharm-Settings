# encoding: utf-8
# module lxml.etree
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37-32\lib\site-packages\lxml\etree.cp37-win32.pyd
# by generator 1.145
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .PIBase import PIBase

class _XSLTProcessingInstruction(PIBase):
    # no doc
    def parseXSL(self, parser=None): # real signature unknown; restored from __doc__
        """
        parseXSL(self, parser=None)
        
                Try to parse the stylesheet referenced by this PI and return
                an ElementTree for it.  If the stylesheet is embedded in the
                same document (referenced via xml:id), find and return an
                ElementTree for the stylesheet Element.
        
                The optional ``parser`` keyword argument can be passed to specify the
                parser used to read from external stylesheet URLs.
        """
        pass

    def set(self, key, value): # real signature unknown; restored from __doc__
        """
        set(self, key, value)
        
                Supports setting the 'href' pseudo-attribute in the text of
                the processing instruction.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


