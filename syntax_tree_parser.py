from syntax_tree_types import *
from token_types import *
from collections import deque

def parse_number(token: Union[ConstantToken, IdentifierToken]) -> Number:
    if type(token) == IdentifierToken:
        return VariableRead(token.variable_name)
    if type(token) == ConstantToken:
        return Constant(token.value)

def parse_expression(tokens: List[Token], line_num=None) -> Expression:
    line_error_string = f'Line {line_num+1}' if line_num is not None else ''
    for token in tokens:
        if type(token) == KeywordToken:
            print("Unexpected Keyword!", line_error_string)
            exit()
    if len(tokens) == 1:
        if type(tokens[0]) != IdentifierToken and type(tokens[0]) != ConstantToken:
            print("Invalid expression!", line_error_string)
            exit()
        return parse_number(tokens[0])
    if len(tokens) == 3:
        if type(tokens[0]) not in {ConstantToken, IdentifierToken} or type(tokens[1]) != OperatorToken or type(tokens[2]) not in {ConstantToken, IdentifierToken}:
            print("Invalid expression!", line_error_string)
            exit()
        if tokens[1] == OperatorToken.ADDITION:
            return Addition(left=parse_number(tokens[0]), right=parse_number(tokens[2]))
        if tokens[1] == OperatorToken.SUBSTRACTION:
            return Substraction(left=parse_number(tokens[0]), right=parse_number(tokens[2]))
        if tokens[1] == OperatorToken.MULTIPLICATION:
            return Multiplication(left=parse_number(tokens[0]), right=parse_number(tokens[2]))
        if tokens[1] == OperatorToken.DIVISION:
            return Division(left=parse_number(tokens[0]), right=parse_number(tokens[2]))
        
    pass

def parse_program(token_lines: 'deque[List[Token]]', start_line=1) -> List[Statement]:
    p = list()
    line_number = start_line
    while len(token_lines) > 0:
        tokens = token_lines.popleft()
        if tokens[0] == KeywordToken.END:
            break
        elif tokens[0] == KeywordToken.WHILE:
            p.append(While(
                expression=parse_expression(tokens[1:], line_number),
                body=parse_program(token_lines, start_line)
            ))
        elif tokens[0] == KeywordToken.IF:
            p.append(If(
                expression=parse_expression(tokens[1:], line_number),
                body=parse_program(token_lines, start_line)
            ))
        elif tokens[0] == KeywordToken.PRINT:
            p.append(Print(parse_expression(
                tokens[1:], line_num=line_number
            )))
        elif tokens[0] == KeywordToken.READ:
            if type(tokens[1]) != IdentifierToken:
                print("Error! Expected identifier. Line", line_number)
                exit()
            p.append(Read(tokens[1].variable_name))
        elif type(tokens[0]) == IdentifierToken:
            if tokens[1] != OperatorToken.ASSIGNMENT:
                print("Error! Expected assignment. Line", line_number)
                exit()
            p.append(VariableWrite(
                variable_name=tokens[0].variable_name,
                expression=parse_expression(tokens[2:], line_num=line_number)
            ))
        else:
            print("Unexprected token!")
            exit()
        line_number += 1
    return p