from typing import Iterator as TIter, Tuple as TTuple, cast as _cast, \
                   TypeVar as TTypeVar, Union as TUnion, Any as TAny

import dataclasses as _dc
from dataclasses import dataclass


@dataclass
class S1:
    x : int
    y : str
    def __iter__(self) -> TIter[TAny]:
        yield from [self.x, self.y]

if False:
    X = _dc.make_dataclass("X", [("_1", str), ("_2", float)])

    x = X("3", 4)
    m,n = x
    print(m,n)

s = S1(3,"4.0")
print(s)

def fun(x : int ,y : str) -> None:
    print("fun", x,y)

a,b = s
print(a,b)
print(type(a),type(b))

fun(a,b)
