#type: ignore

from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Callable

@dataclass
class S:
    _1 : int

@dataclass
class T:
    _1 : float
    _2 : str
    _3 : int


@dataclass
class U:
    _1 : float

@dataclass
class V:
    _1 : int
    _2 : int

ST = Union[S,T]
UV = Union[U,V]

def claim(f):
    return f
def match(f):
    return f

@claim
def fun(_ : Callable[[ST,UV],float]): pass


@match
def fun(_1 : S(x), _2 : V(_,_)):
    return 44

@match
def fun(_1 : T(_,x,_), _2 : V(y,_)):
    return 45
