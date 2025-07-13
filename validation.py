import os
from ast import (
    AST,
    Assign,
    Attribute,
    ClassDef,
    FunctionDef,
    Name,
    Call,
)
from typing_extensions import Any


class Validation:
    @staticmethod
    def file_exists(path: str) -> bool:
        return os.path.isfile(path)
    
    @staticmethod
    def is_empty(value: Any) -> bool:
        return value
    

class AstValidation:
    @staticmethod
    def is_assign(node: AST) -> bool:
        return isinstance(node, Assign)
    
    @staticmethod
    def is_attribute(node: AST) -> bool:
        return isinstance(node, Attribute)
    
    @staticmethod
    def is_classdef(node: AST) -> bool:
        return isinstance(node.parent, ClassDef)
    
    @staticmethod
    def is_functiondef(node: AST) -> bool:
        return isinstance(node, FunctionDef)
    
    @staticmethod
    def is_name(node: AST) -> bool:
        return isinstance(node.func, Name)
    
    @staticmethod
    def is_call(node: AST) -> bool:
        return isinstance(node.value, Call)
    
    @staticmethod
    def is_property(node: str) -> bool:
        valid = AstValidation.is_name(node)
        return valid and node.id == "property"
    
    @staticmethod
    def is_setter(node) -> bool:
        valid = AstValidation.is_attribute(node)
        return valid and node.attr == "setter"
    
    @staticmethod
    def is_deleter(node: str) -> bool:
        valid = AstValidation.is_attribute(node)
        return valid and node.attr == "deleter"

