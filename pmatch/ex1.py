##type: ignore

from __future__ import annotations
#import dataclasses as _dc
#from dataclasses import dataclass
import mypmatch as mpm
from mypmatch import TAny, TUnion, TLam

#@_dc.dataclass
#class S:
##    _1 : int


@mpm.dataclass(int)
class S: pass
@mpm.dataclass(float, str,int)
class T: pass

@mpm.dataclass(str)
class U: pass

@mpm.dataclass
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

