from syntax_tree_types import *
from typing import Dict, List
from simpletron_instruction_types import Instruction

def generate_bytecode(instructions: List[Instruction]) -> List[int]:
    output = []
    for instruction in instructions:
        output.append(int(f'{instruction.instruction_type}{instruction.target_address}'))
    return output

def evaluate_expression(variable_addresses: Dict[str, int], expression: Expression, start_line: int) -> List[int]:
    curr_line = start_line
    if type(expression) == Number:
        if type(expression) == VariableRead:
            load_accumulator(variable_addresses[expression.variable_name])
            curr_line += 1
        if type(expression) == Constant:
            pass

def compile_syntax_tree(program: Program) -> List[int]:
    variables = {}
    constants = {}
    


    for statement in program:
        if type(statement) == VariableWrite:
            output.extend(evaluate_expression(variable_addresses, statement.expression))


    output.append(end_of_program())
