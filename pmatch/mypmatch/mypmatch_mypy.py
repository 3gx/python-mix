from typing import Dict, List, Set, Tuple, Optional, Callable
from mypy.types import Type, Instance, CallableType, TypeList, UnboundType, ProperType
from typing_extensions import Final, Type as TypingType

from mypy.plugin import (
    Plugin, FunctionContext, MethodContext, MethodSigContext, AttributeContext, ClassDefContext,
    CheckerPluginInterface,
)
import sys

class MyPMatch(Plugin):
    def get_attribute_hook(self, fullname: str
            ) -> Optional[Callable[[AttributeContext], Type]]:
        print(f"--{self} -> {fullname}")
#        sys.stdout.flush()
#        assert(0)
        return None

def plugin(version: str) -> 'TypingType[Plugin]':
    return MyPMatch
