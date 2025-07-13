from ast import AST, iter_child_nodes, walk
from validation import Validation as V, AstValidation as AV
from typing_extensions import List, Set


class PropertyAnalyzer:
    def __init__(self, file: str):
        self.file = file

    @staticmethod
    def set_parents(node: AST, parent: AST | None = None) -> None:
        node.parent = parent
        for child in iter_child_nodes(node):
            PropertyAnalyzer.set_parents(child, node)

    def property_instances(root: AST) -> List[Set[str]]:
        result = list()
        for node in walk(root):
            if (
                AV.is_classdef(node) and
                AV.is_assign(node) and
                AV.is_call(node) and
                AV.is_property(node)
            ):
                main_name = [node.targets[0].id]
                sub_names = [func.id for func in node.value.args]
                names = set(main_name + sub_names)
                result.append(names)
        return result
