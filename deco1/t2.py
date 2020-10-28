#type: ignore
import inspect
import ast
import astunparse as ast_

def remove_indent(lines):
    lines = lines.split('\n')
    to_remove = 0
    for i in range(len(lines[0])):
        if lines[0][i] == ' ':
            to_remove = i + 1
        else:
            break

    cleaned = []
    for l in lines:
        cleaned.append(l[to_remove:])
        if len(l) >= to_remove:
            for i in range(to_remove):
                assert l[i] == ' '

    return '\n'.join(cleaned)


def get_ast(func):
    source = remove_indent(inspect.getsource(func))
    tree = ast.parse(source)
    return tree

class Var:
    def __init__(self):
        self._value = None

    @property
    def assign(self):
        raise SyntaxError("don't use it")
    @assign.setter
    def assign(self, value):
        self.value = value

def add_context(fn, ctx):

    class Transform(ast.NodeTransformer):
        def __init__(self, ctx):
            self.ctx = ctx


        def visit_FunctionDef(self, node):
            node.decorator_list = []
            stmts = list()
            for k,v in self.ctx.items():
                stmt = ast.Assign(targets=[ast.Name(id=k, ctx=ast.Store())],
                        value=ast.Constant(value=v,kind=None),
                        type_comment=None)
                stmts.append(stmt)
            stmts += node.body
            node.body = stmts
            return node

    tree = get_ast(fn)
    Transform(ctx).visit(tree)
    ast.fix_missing_locations(tree)
#    print(ast_.dump(tree))
#    print(ast_.unparse(tree))
    code = compile(tree, "<string>", mode="exec")
    local_vars = {}
    global_vars = {}
    exec(code, global_vars, local_vars)
    modified_fn = local_vars[fn.__name__]
    return modified_fn

def deco1(fn):
    fn_args = inspect.getfullargspec(fn).args
    kw_args = {kw : Var() for kw in fn_args}
    fn(**kw_args)
    kw_args = {k : v.value for k,v in kw_args.items()}
    return kw_args

def deco2(ctx):
    assert(isinstance(ctx,dict))
    def wrapper(fn):
        return add_context(fn,ctx)
    return wrapper

########## example

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
try:
    print(globals()['x'])
except:
    print("x is not in global")
