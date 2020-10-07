from typing import Union as TUnion, Callable as TLam, Any as TAny, \
                   Iterable as TIter
import dataclasses as _dc

def data(*types : TAny) -> TAny:
    def wrapper(cls : TAny) -> TAny:
        fields = [(f"_{i}",ty) for i, ty in enumerate(types)]
        string = f"{cls.__name__}("
        keys = [f"_{i}" for i,_ in enumerate(types)]
        def _repr(self : TAny) -> str:
            string = f"{cls.__name__}("
            for i, k in enumerate(keys):
                value = getattr(self,k)
                if isinstance(value, str):
                    string += f"'{value}'"
                else:
                    string += f"{value}"
                if i < len(keys)-1:
                    string += ","
            string += ")"
            return string
        def _iter(self: TAny) -> TIter[TAny]:
            yield from (getattr(self, k) for k in keys)
        return _dc.make_dataclass(cls.__name__, fields=fields,
                namespace={'__repr__': _repr,
                           '__iter__': _iter})
    return wrapper


