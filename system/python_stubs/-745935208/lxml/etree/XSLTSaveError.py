# encoding: utf-8
# module lxml.etree
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.146
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .XSLTError import XSLTError

from .SerialisationError import SerialisationError

class XSLTSaveError(XSLTError, SerialisationError):
    """ Error serialising an XSLT result. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



