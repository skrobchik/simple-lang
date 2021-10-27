from enum import Enum
from dataclasses import dataclass
from typing import Union

class KeywordToken(Enum):
    PRINT = 1
    READ = 2

@dataclass
class IdentifierToken:
    variable_name: str

class OperatorToken(Enum):
    ADDITION = 1
    SUBSTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4
    ASSIGNMENT = 5

@dataclass
class ConstantToken:
    value: int

Token = Union[KeywordToken, IdentifierToken, OperatorToken, ConstantToken]