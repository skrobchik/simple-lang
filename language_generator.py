from syntax_tree_types import *
from typing import Dict, List

@dataclass
class GoToInstruction:
    line: LineReference

def goto(line: int) -> int:
    return int(f'40{line}')

def end_of_program() -> int:
    return 43

def write_accumulator(line: int) -> int:
    return int(f'21{line}')

def load_accumulator(line: int) -> int:
    return int(f'20{line}')

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
    for statement in program:
        if type(statement) == VariableWrite:
            variables.add(statement.vairable_name)
    
    output: List[int] = [0]
    variable_addresses = {}
    for var in variables:
        output.append(0)
        variable_addresses[var] = len(output)
    output[0] = goto(len(output)+1)

    for statement in program:
        if type(statement) == VariableWrite:
            output.extend(evaluate_expression(variable_addresses, statement.expression))


    output.append(end_of_program())
