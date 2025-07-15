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
    def file_exists(path: str, /) -> bool:
        return os.path.isfile(path)
    
    @staticmethod
    def is_empty(value: Any, /) -> bool:
        return bool(value)
    

class AstValidation:
    @staticmethod
    def is_classdef(node: AST, /) -> bool:
        return hasattr(node, "parent") and isinstance(node.parent, ClassDef)

    @staticmethod
    def is_functiondef(node: AST, /) -> bool:
        return isinstance(node, FunctionDef)
    
    @staticmethod
    def is_assign(node: AST, /) -> bool:
        return isinstance(node, Assign)

    @staticmethod
    def is_call(node: AST, /) -> bool:
        return hasattr(node, "value") and isinstance(node.value, Call)
    
    @staticmethod
    def is_name_func(node: AST, /) -> bool:
        return isinstance(node.value.func, Name)
    
    @staticmethod
    def is_name_node(node: AST, /) -> bool:
        return isinstance(node, Name)
    
    @staticmethod
    def is_attribute(node: AST, /) -> bool:
        return isinstance(node, Attribute)
    
    @staticmethod
    def is_property_assign(node: AST, /) -> bool:
        return (
            AstValidation.is_classdef(node) and
            AstValidation.is_assign(node) and
            AstValidation.is_call(node) and
            AstValidation.is_name_func(node) and
            node.value.func.id == "property"
        )

    def is_property_name(node: AST, /) -> bool:
        return (
            AstValidation.is_name_node(node) and
            node.id == "property"
        )
    
    @staticmethod
    def is_setter(node: AST, /) -> bool:
        return (
            AstValidation.is_attribute(node) and
            node.attr == "setter"
        )
    
    @staticmethod
    def is_deleter(node: AST, /) -> bool:
        return (
            AstValidation.is_attribute(node) and
            node.attr == "deleter"
        )
    
    @staticmethod
    def has_decorator(node: AST, /) -> bool:
        return (
            AstValidation.is_classdef(node) and
            AstValidation.is_functiondef(node) and
            Validation.is_empty(node.decorator_list)
        )
    
    @staticmethod
    def is_property_decorator(node: AST,/):
        return (
            AstValidation.is_property_name(node) or
            AstValidation.is_setter(node) or 
            AstValidation.is_deleter(node)
        )
