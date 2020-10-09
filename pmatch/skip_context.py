from typing import TypeVar as TTypeVar, Any as TAny, Generic as TGeneric


class _skip_context:
    class _skip(Exception):
        pass

    def __init__(self, skip : bool):
        print("init")
        self.skip = skip

    def __enter__(self) -> TAny:
        print("enter")
        if self.skip:
            import sys

            sys.settrace(lambda *args, **keys: None)
            frame = sys._getframe(1)
            frame.f_trace = self.trace  # type: ignore
            return None 
        return (42,43,44)

    def trace(self, frame, event, arg):  # type: ignore
        print("abort")
        raise _skip_context._skip()

    def __exit__(self, type, value, traceback):  # type: ignore
        print("exit")
        if type is None:
            return  # No exception
        if issubclass(type, _skip_context._skip):
            return True  # Suppress special SkipWithBlock exception



with _skip_context(False) as (a,b,c), _skip_context(False) as g:
    print(a,b,c)
    with _skip_context(True):
        pass
    print(g)


from contextlib import suppress, contextmanager

class Pass(Exception): pass

@contextmanager
def skip(flag):
    if flag:
        raise Pass
    yield

suppress = suppress(Pass)

@contextmanager
def ctx():
    yield ("a","b","cc")

with suppress, ctx() as (a,b,c):
    print(a,b,c)
    with suppress, ctx() as g, skip(True):
        print(g)
    with suppress, ctx() as g, skip(False):
        print(g)
    print(c,b,a)


