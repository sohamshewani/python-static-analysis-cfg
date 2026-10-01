from typing import Dict, List, Optional, Set, TypeVar, Union
from astroid import nodes, parse
from pyCFGParser import CFGParser

T = TypeVar('T')

class CFGNode:
    def __init__(self, node: nodes.NodeNG):
        self.node = node
        self.children: List[CFGNode] = []
        self.parents: List[CFGNode] = []

    def add_child(self, child: CFGNode):
        self.children.append(child)
        child.parents.append(self)

    def add_parent(self, parent: CFGNode):
        self.parents.append(parent)
        parent.children.append(self)

    def __str__(self):
        return f'{self.node.lineno}:{self.node.col_offset} - {self.node.name if hasattr(self.node, 