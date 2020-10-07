from typing import Iterator as TIter, Tuple as TTuple, cast as _cast, \
                   TypeVar as TTypeVar, Union as TUnion, Any as TAny

import dataclasses as _dc
from dataclasses import dataclass


class Unpack:
    def __iter__(self) -> TIter[TAny]:
        yield from [getattr(self, field.name) for field in _dc.fields(self)]
    def __repr__(self) -> str:
        string = f"{self.__class__.__name__}("
        keys = [field.name for field in _dc.fields(self)]
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



@dataclass(repr=False)
class S1(Unpack):
    x : int
    y : str

s = S1(3,"4.0")
print(s)

def fun(x : int ,y : str) -> None:
    print("fun", x,y)

a,b = s
print(a,b)
print(type(a),type(b))

fun(a,b)
