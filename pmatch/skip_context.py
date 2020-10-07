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



with _skip_context(True) as (a,b,c), _skip_context(False) as g:
    print(a,b,c)
    print(g)

