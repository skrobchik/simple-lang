from compiler import compile

source_file_path = "sample_program.txt"
output_file_path = "test.m"
characters = None
with open(source_file_path, 'r') as source_file:
    characters = source_file.read()
output = compile(characters)
with open(output_file_path, 'w') as output_file:
    output_file.write(f"c={str(output)};\nsimpletron(c);")