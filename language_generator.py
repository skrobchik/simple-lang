from syntax_tree_types import *
from typing import Dict, List
from simpletron_instruction_types import Instruction, InstructionType

def load_number(variables, constants, number, instruction_type=InstructionType.LOAD) -> List[Instruction]:
    output = []
    if type(number) == VariableRead:
        if number.variable_name not in variables:
            print(f'Variable {number.variable_name} used before declaration!')
            exit()
        output.append(Instruction(
            instruction_type=instruction_type,
            target_address=variables[number.variable_name]
        ))
    elif type(number) == Constant:
        if number.value not in constants:
            constants[number.value] = len(constants)
        output.append(Instruction(
            instruction_type=instruction_type,
            target_address=constants[number.value]
        ))
    else:
        print("Error! Number type not supported.")
        exit()
    return output

def evaluate_expression(variables: Dict[str, int], constants: Dict[int, int], expression: Expression) -> List[Instruction]:
    output = []
    if type(expression) == Number:
        output.extend(load_number(variables, constants, expression))
    elif type(expression) == BinaryOperation:
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
            if statement.vairable_name not in variables:
                variables[statement.variable_name] = len(variables)
            instructions.append(Instruction(
                    instruction_type=InstructionType.SAVE,
                    target_address=variables[statement.variable_name]
            ))
        if type(statement) == Print:
            instructions.extend(evaluate_expression(variables, constants, statement.expression))
            instructions.append(Instruction(
                instruction_type=InstructionType.SAVE,
                target_address=variables['PRINT_BUFFER']
            ))
            instructions.append(Instruction(
                instruction_type=InstructionType.PRINT,
                target_address=variables['PRINT_BUFFER']
            ))
        if type(statement) == Read:
            instructions.append(Instruction(
                instruction_type=InstructionType.INPUT,
                target_address=variables[statement.variable_name]
            ))

    output = []
    variable_address_shift = len(instructions)+1
    for instruction in instructions:
        output.append(int(f'{instruction.instruction_type.value}{instruction.target_address+variable_address_shift}'))
    return output
