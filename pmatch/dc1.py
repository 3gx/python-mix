from typing import Iterator as TIter, Tuple as TTuple, cast as _cast, \
                   TypeVar as TTypeVar, Union as TUnion
from dataclasses import dataclass


@dataclass
class S1:
    x : int
    y : str
    def __iter__(self) -> TIter[TUnion[int, str]]:
        yield self.x
        yield self.y
    def unpack(self) -> TTuple[int,str]:
        return (self.x, self.y)

s = S1(3,"4.0")
print(s)

def fun(x : int ,y : str) -> None:
    print("fun", x,y)

a,b = s.unpack()
print(a,b)
print(type(a),type(b))

fun(a,b)
