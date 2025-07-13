from ast import AST, iter_child_nodes, walk, unparse, parse
from validation import AstValidation as AV
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
            if AV.is_property_assign(node):
                main_name = [node.targets[0].id]
                sub_names = [func.id for func in node.value.args]
                names = set(main_name + sub_names)
                result.append(names)
        return result


    def unparse_node(root: AST, list_names: List[Set[str]]) -> List[Set[str]]:
        result = list()
        for names in list_names:
            items = set()
            for node in walk(root):
                if AV.is_classdef(node):
                    if AV.is_assign(node) and node.targets[0].id in names:
                        items.add(unparse(node))
                    elif AV.is_functiondef(node) and node.name in names:
                        items.add(unparse(node))
            result.append(items)
        return result


    def property_methods(node: AST) -> List[str]:
        list_properties = list()
        for node in walk(node):
            if AV.has_decorator(node):
                decorator = node.decorator_list[0]
                if AV.is_property_decorator(decorator):
                    list_properties.append(node)
        return list_properties


    def related_properties(list_node: List[str]) -> List[Set[str]]:
        properties_dict = dict()
        for node in list_node:
            unparse_node = unparse(node)
            key_state = properties_dict.setdefault(node.name, [])
            key_state.append(unparse_node)
        properties_set = [set(code_list) for code_list in properties_dict.values()]
        return properties_set
