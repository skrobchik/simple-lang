from collections import deque
from typing import List
from tokenizer import tokenize_line
from syntax_tree_parser import parse_program
from language_generator import compile_syntax_tree
import sys
            
def compile(characters: str) -> List[int]:
    token_lines = deque(tokenize_line(line) for line in characters.splitlines())
    abstract_syntax_tree = parse_program(token_lines)
    return compile_syntax_tree(abstract_syntax_tree)

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Usage: python compiler.py <source_file_path> [output_file_path]")
    else:
        source_file_path = sys.argv[1]
        output_file_path = 'out.m'
        if(len(sys.argv) >= 3):
            output_file_path = sys.argv[2]
        characters = None
        with open(source_file_path, 'r') as source_file:
            characters = source_file.read()
        output = compile(characters)
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"clear; clc;\nc={str(output)};\nsimpletron(c);")
