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
    
    @classmethod
    def is_type(cls, obj: Any, type: Any) -> bool:
        return isinstance(obj, type)
    
    @classmethod
    def is_assign(cls, node: AST) -> bool:
        return cls.is_type(node, Assign)
    
    @classmethod
    def is_attribute(cls, node: AST) -> bool:
        return cls.is_type(node, Attribute)
    
    @classmethod
    def is_classdef(cls, node: AST) -> bool:
        return cls.is_type(node, ClassDef)
    
    @classmethod
    def is_functiondef(cls, node: AST) -> bool:
        return cls.is_type(node, FunctionDef)
    
    @classmethod
    def is_name(cls, node: AST) -> bool:
        return cls.is_type(node, Name)
    
    @classmethod
    def is_call(cls, node: AST) -> bool:
        return cls.is_type(node, Call)

    
