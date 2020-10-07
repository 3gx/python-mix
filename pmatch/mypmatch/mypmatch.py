from typing import Union as TUnion, Callable as TLam, Any as TAny
import dataclasses as _dc

def dataclass(*types : TAny) -> TAny:
    def wrapper(cls : TAny) -> TAny:
        fields = [(f"_{i}",ty) for i, ty in enumerate(types)]
        string = f"{cls.__name__}("
        keys = [f"_{i}" for i,_ in enumerate(types)]
        def get_names(self : TAny) -> str:
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
        return _dc.make_dataclass(cls.__name__, fields=fields,
                namespace={'__repr__': lambda self: get_names(self)})
    return wrapper


