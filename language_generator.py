from enum import Enum
from syntax_tree_types import *
from typing import Dict, List, get_args
from simpletron_instruction_types import InstructionType

@dataclass
class MemoryAddress:
    memory_space_name: str
    index: int

@dataclass
class Instruction:
    instruction_type: InstructionType
    target_address: MemoryAddress


def load_number(variables, constants, number, instruction_type=InstructionType.LOAD) -> List[Instruction]:
    output = []
    if type(number) == VariableRead:
        if number.variable_name not in variables:
            print(f'Variable {number.variable_name} used before declaration!')
            exit()
        output.append(Instruction(
            instruction_type=instruction_type,
            target_address=MemoryAddress(
                'VARIABLES', variables[number.variable_name]
            )
        ))
    elif type(number) == Constant:
        if number.value not in constants:
            constants[number.value] = len(constants)
        output.append(Instruction(
            instruction_type=instruction_type,
            target_address=MemoryAddress(
                'CONSTANTS', constants[number.value]
            )
        ))
    else:
        print("Error! Number type not supported.")
        exit()
    return output

def evaluate_expression(variables: Dict[str, int], constants: Dict[int, int], expression: Expression) -> List[Instruction]:
    output = []
    if type(expression) in get_args(Number):
        output.extend(load_number(variables, constants, expression))
    elif type(expression) in get_args(BinaryOperation):
        output.extend(load_number(variables, constants, expression.left))
        operation_type_instructions = {
            Addition: InstructionType.ADDITION,
            Substraction: InstructionType.SUBSTRACTION,
            Multiplication: InstructionType.MULTIPLICATION,
            Division: InstructionType.DIVISION,
        }
        if type(expression) not in operation_type_instructions:
            print("Error! Operation type not supported.")
            exit()
        output.extend(load_number(variables, constants, expression.right, instruction_type=operation_type_instructions[type(expression)]))
    else:
        print("Error! Expression type not supported.")
        exit()
    return output

def compile_syntax_tree(program: Program) -> List[int]:
    variables = {}
    constants = {}
    instructions: List[Instruction] = []

    variables['PRINT_BUFFER'] = 0
    for statement in program:
        if type(statement) == VariableWrite:
            instructions.extend(evaluate_expression(variables, constants, statement.expression))
            if statement.variable_name not in variables:
                variables[statement.variable_name] = len(variables)
            instructions.append(Instruction(
                    instruction_type=InstructionType.SAVE,
                    target_address=MemoryAddress(
                        'VARIABLES', variables[statement.variable_name]
                    )
            ))
        elif type(statement) == Print:
            instructions.extend(evaluate_expression(variables, constants, statement.expression))
            instructions.append(Instruction(
                instruction_type=InstructionType.SAVE,
                target_address=MemoryAddress(
                    'VARIABLES', variables['PRINT_BUFFER']
                )
            ))
            instructions.append(Instruction(
                instruction_type=InstructionType.PRINT,
                target_address=MemoryAddress(
                    'VARIABLES', variables['PRINT_BUFFER']
                )
            ))
        elif type(statement) == Read:
            if statement.variable_name not in variables:
                variables[statement.variable_name] = len(variables)
            instructions.append(Instruction(
                instruction_type=InstructionType.INPUT,
                target_address=MemoryAddress(
                    'VARIABLES', variables[statement.variable_name]
                )
            ))
        else:
            print("Error! Statement type not supported")
            exit()
    instructions.append(Instruction(instruction_type=InstructionType.END_OF_PROGRAM, target_address=MemoryAddress('',0)))

    output = []
    variable_address_start = len(instructions)
    constants_address_start = variable_address_start+len(variables)
    for instruction in instructions:
        real_memory_address = instruction.target_address.index
        if instruction.target_address.memory_space_name == 'VARIABLES':
            real_memory_address += variable_address_start
        elif instruction.target_address.memory_space_name == 'CONSTANTS':
            real_memory_address += constants_address_start
        output.append(int(f'{instruction.instruction_type.value}{(real_memory_address+1):02}'))

    output.extend([0]*(len(variables)+len(constants)))
    
    for constant_value, index in constants.items():
        real_memory_address = index + constants_address_start
        output[real_memory_address] = constant_value

    return output
