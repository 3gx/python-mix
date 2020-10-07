from typing import List, Union
from dataclasses import dataclass

Tree = Union["Leaf", "Node"]


@dataclass
class Leaf:
    pass


@dataclass
class Node:
    value: int
    left: Tree
    right: Tree


tree = Node(
    32,
    Node(34, Leaf(), Node(33, Leaf(), Leaf())),
    Node(44, Node(77, Leaf(), Leaf()), Leaf()),
)
print(tree)
