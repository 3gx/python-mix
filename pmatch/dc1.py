from dataclasses import dataclass
from typing import Iterable as TIter, Tuple as TTuple, cast as _cast, \
                   TypeVar as TTypeVar

_T = TTypeVar("_T")

@dataclass
class S:
    x : int
    y : str
    def unpack(self) -> TTuple[int,str]:
        return (self.x,self.y)

s = S(3,"4")
print(s)

a,b = s.unpack()
print(a,b)
print(type(a),type(b))
