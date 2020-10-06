##type: ignore

from __future__ import annotations
import dataclasses as _dc
#from dataclasses import dataclass
from typing import Union as TUnion, Callable as TLam, Any as TAny

@_dc.dataclass
class S:
    _1 : int


def dataclass(*types : TAny) -> TAny:
    def wrapper(cls : TAny) -> TAny:
        fields = [(f"_{i}",ty) for i, ty in enumerate(types)]
        string = f"{cls.__name__}("
        keys = [f"_{i}" for i,_ in enumerate(types)]
        for k in keys[:-1]:
            string += f"{{self.{k}}},"
        string += f"{{self.{keys[-1]}}})"
        def get_names(self : TAny) -> str:
            string = f"{cls.__name__}("
            for i, k in enumerate(keys):
                value = getattr(self,k)
                if isinstance(value, str):
                    string += f"'{value}'"
                else:
                    string += f"{value}"
                string += ")" if (i == len(keys)-1) else ","
            return string
        return _dc.make_dataclass(cls.__name__, fields=fields,
                namespace={'__repr__': lambda self: get_names(self)})
    return wrapper


@dataclass(float, str,int)
class T: pass

@dataclass(str)
class U: pass

@dataclass
class V: pass

t = T(1,2,3)
print(t)
u = U("fun")
print(u)

ST = TUnion[S,T]
UV = TUnion[U,V]

def claim(f):
    return f
def define(f):
    return f

@claim
def fun(_ : TLam[[ST,UV],float]): pass


@define
def fun(_1 : S(x), _2 : V(_,_)):
    return 44

@define
def fun(_1 : [S(x), x > 0],  _2 : V(_,_)):
    return 44

@define
def fun(_1 : T(_,x,_), _2 : V(y,_)):
    return 45

@claim
def factorial(_ : TLam[[int],int]): pass

@define
def factorial(_1 : [n, n == 0]): return 1
@define
def factorial(_1 : [n, n > 0]): return n*factorial(n-1)

