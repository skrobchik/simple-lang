from dataclasses import dataclass
from enum import Enum

class InstructionType(Enum):
    INPUT = 10 # Prompts CLI input. Writes to specified address.
    PRINT = 11 # Prints value in specified address to CLI.
    LOAD = 20 # Load value in specified address to acumulator.
    SAVE = 21 # Save value in acumulator to specified address.
    ADDITION = 30 # Adds value in specified address to acumulator.
    SUBSTRACTION = 31 # Substracts value in specified address from acumulator.
    DIVISION = 32 # Divides acumulator by value in specified address.
    MULTIPLICATION = 33 # Multiplies acumulator by value in specified address.
    GOTO = 40 # Changes instruction pointer to specified address.
    CONDITIONAL_NEGATIVE_GOTO = 41 # Changes instruction pointer to specified address if acumulator is negative.
    CONDITIONAL_ZERO_GOTO = 42 # Changes instruction pointer to specified address if acumulator is zero.
    END_OF_PROGRAM = 43 # Terminates execution.

@dataclass
class Instruction:
    instruction_type: InstructionType
    target_address: int
