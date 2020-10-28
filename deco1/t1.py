#type: ignore
import inspect

class Var:
    def __init__(self):
        self._value = None

    @property
    def assign(self):
        raise SyntaxError("don't use it")
    @assign.setter
    def assign(self, value):
        self.value = value

def deco1(fn):
    fn_args = inspect.getfullargspec(fn).args
    kw_args = {kw : Var() for kw in fn_args}
    fn(**kw_args)
    kw_args = {k : v.value for k,v in kw_args.items()}
    return kw_args

def deco2(ctx):
    assert(isinstance(ctx,dict))
    def wrapper(fn):
        fn.__globals__.update(ctx)
        return fn
    return wrapper



@deco1
def P(x,y):
    x.assign = 42
    y.assign = 44

@deco2(P)
def m1():
    print(x)
    print(y)
    try:
        print(z)
        print("OK")
    except:
        print("z doesn't exist")

m1()
print(globals()['x'])
