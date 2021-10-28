from dataclasses import dataclass
from typing import Union, List

@dataclass
class Constant:
    value: int

@dataclass
class VariableRead:
    variable_name: str

Number = Union[Constant, VariableRead]

@dataclass
class Addition:
    left: Number
    right: Number

@dataclass
class Substraction:
    left: Number
    right: Number

@dataclass
class Multiplication:
    left: Number
    right: Number

@dataclass
class Division:
    left: Number
    right: Number

BinaryOperation = Union[Addition, Substraction, Multiplication, Division]

Expression = Union[Number, BinaryOperation]

@dataclass
class VariableWrite:
    variable_name: str
    expression: Expression

@dataclass
class Print:
    expression: Expression

@dataclass
class Read:
    variable_name: str

Statement = Union[VariableWrite, Print, Read]

Program = List[Statement]