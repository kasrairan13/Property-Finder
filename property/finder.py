from ast import AST, iter_child_nodes, walk, unparse, parse
from typing import List, Set, Iterable

from validation import AV


class ASTTools:
    @staticmethod
    def parse_file(file) -> AST:
        with open(file) as f:
            file = f.read()
        return parse(file)
    
    @staticmethod
    def set_parents(node: AST, parent: AST | None = None) -> None:
        node.parent = parent
        for child in iter_child_nodes(node):
            ASTTools.set_parents(child, node)

    @staticmethod
    def walk_in_root(root: AST):
        yield from walk(root)
    
    @staticmethod
    def extract_instance_names(node: AST) -> Set[str]:
        main_name = [node.targets[0].id]
        sub_names = [func.id for func in node.value.args]
        return set(main_name + sub_names)

    @staticmethod
    def unparse_node(root: AST, list_names: List[Set[str]]) -> List[Set[str]]:
        result = list()
        for names in list_names:
            items = set()
            for node in ASTTools.walk_in_root(root):
                if (
                    AV.is_classdef(node) or
                    (AV.is_assign(node) and node.targets[0].id in names) or
                    (AV.is_functiondef(node) and node.name in names)
                ):
                    items.add(unparse(node))
            result.append(items)
        return result

    @staticmethod
    def related_methods(list_node: List[str]) -> List[Set[str]]:
        properties_dict = dict()
        for node in list_node:
            unparse_node = unparse(node)
            key_state = properties_dict.setdefault(node.name, [])
            key_state.append(unparse_node)
        properties_set = [set(code_list) for code_list in properties_dict.values()]
        return properties_set
    

class PropertyAnalyzer:
    def __init__(self, file: str):
        self.root = ASTTools.parse_file(file)
        self.instance_list = list()
        self.method_list = list()

        # set parents
        ASTTools.set_parents(self.root)

    def property_instances(self) -> List[Set[str]]:
        for node in ASTTools.walk_in_root(self.root):
            if AV.is_property_assign(node):
                names = ASTTools.extract_instance_names(node)
                self.instance_list.append(names)
        return self.instance_list

    def property_methods(self) -> List[str]:
        for node in ASTTools.walk_in_root(self.root):
            if AV.has_decorator(node):
                decorator = node.decorator_list[0]
                if AV.is_property_decorator(decorator):
                    self.method_list.append(node)
        return self.method_list
    
    def use(self):
        instance_list = ASTTools.unparse_node(self.root, self.instance_list)
        method_list = ASTTools.related_methods(self.method_list)
        return [instance_list, method_list]

