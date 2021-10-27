from token_types import *
from typing import List

def tokenize_line(line: str) -> List[Token]:
    words: List[str] = [word.strip() for word in line.split()]
    tokens: List[Token] = []
    for word in words:
        if word == 'print':
            tokens.append(KeywordToken.PRINT)
            continue
        if word == 'read':
            tokens.append(KeywordToken.READ)
            continue

        var_name = []
        constant_digits = []
        for c in word:
            if c in {'+', '-', '*', '/', '='}:
                
                if len(var_name) > 0:
                    tokens.append(IdentifierToken(''.join(var_name)))
                    var_name = []
                if len(constant_digits) > 0:
                    tokens.append(ConstantToken(int(''.join(constant_digits))))
                    constant_digits = []
                
                if c == '+':
                    tokens.append(OperatorToken.ADDITION)
                if c == '-':
                    tokens.append(OperatorToken.SUBSTRACTION)
                if c == '*':
                    tokens.append(OperatorToken.MULTIPLICATION)
                if c == '/':
                    tokens.append(OperatorToken.DIVISION)
                if c == '=':
                    tokens.append(OperatorToken.ASSIGNMENT)
            else:
                if len(var_name) == 0:
                    if c in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                        constant_digits.append(c)
                    else:
                        if len(constant_digits) > 0:
                            print("Parsing error! Character in number.")
                            exit()
                        else:
                            var_name.append(c)
                else:
                    var_name.append(c)
                    
        if len(var_name) > 0:
            tokens.append(IdentifierToken(''.join(var_name)))
            var_name = []
        if len(constant_digits) > 0:
            tokens.append(ConstantToken(int(''.join(constant_digits))))
            constant_digits = []

    return tokens   

