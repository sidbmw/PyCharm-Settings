# encoding: utf-8
# module _cython_0_28_5
# from C:\Users\siddh\AppData\Local\Programs\Python\Python37-32\lib\site-packages\lxml\objectify.cp37-win32.pyd
# by generator 1.145
# no doc
# no imports

# Variables with simple values

__loader__ = None

__spec__ = None

# no functions
# classes

class coroutine(object):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> raise GeneratorExit inside coroutine. """
        pass

    def send(self, arg): # real signature unknown; restored from __doc__
        """
        send(arg) -> send 'arg' into coroutine,
        return next iterated value or raise StopIteration.
        """
        pass

    def throw(self, typ, val=None, tb=None): # real signature unknown; restored from __doc__
        """
        throw(typ[,val[,tb]]) -> raise exception in coroutine,
        return next iterated value or raise StopIteration.
        """
        pass

    def __await__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator to be used in await expression. """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    cr_await = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being awaited, or None"""

    cr_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Frame of the coroutine"""

    cr_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'coroutine'
    __qualname__ = 'coroutine'


class coroutine_wrapper(object):
    """ A wrapper object implementing __await__ for coroutines. """
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> raise GeneratorExit inside coroutine. """
        pass

    def send(self, arg): # real signature unknown; restored from __doc__
        """
        send(arg) -> send 'arg' into coroutine,
        return next yielded value or raise StopIteration.
        """
        pass

    def throw(self, typ, val=None, tb=None): # real signature unknown; restored from __doc__
        """
        throw(typ[,val[,tb]]) -> raise exception in coroutine,
        return next yielded value or raise StopIteration.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


class cython_function_or_method(object):
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    func_closure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func_defaults = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func_dict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func_doc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func_globals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __annotations__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __closure__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __code__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __defaults__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __globals__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __kwdefaults__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __self__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''
    __name__ = 'cython_function_or_method'
    __qualname__ = 'cython_function_or_method'


class generator(object):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> raise GeneratorExit inside generator. """
        pass

    def send(self, arg): # real signature unknown; restored from __doc__
        """
        send(arg) -> send 'arg' into generator,
        return next yielded value or raise StopIteration.
        """
        pass

    def throw(self, typ, val=None, tb=None): # real signature unknown; restored from __doc__
        """
        throw(typ[,val[,tb]]) -> raise exception in generator,
        return next yielded value or raise StopIteration.
        """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    gi_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_yieldfrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being iterated by 'yield from', or None"""


    __name__ = 'generator'
    __qualname__ = 'generator'


