##type: ignore

from __future__ import annotations
import mypmatch as mpm
from mypmatch import data
from mypmatch import TAny
from mypmatch import TUnion, TLam

@data()
class SX:
    _1 : int

sx = SX()
print(sx)

@data(int)
class S: pass
@data(float, str,int)
class T: pass

@data(str)
class U: pass

@data
class V: pass

t = T(1,2,3)
print(t)
u = U("fun")
print(u)
m,n,k = t
print(m,n,k)

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

