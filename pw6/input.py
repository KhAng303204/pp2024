import os

def get_input(prompt):
    return input(prompt)

def get_float_input(prompt):
    return float(input(prompt))

def get_int_input(prompt):
    return int(input(prompt))

def get_input(prompt):
    return input(prompt)

def get_float_input(prompt):
    return float(input(prompt))

def get_int_input(prompt):
    return int(input(prompt))

def write_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')

def check_file_exist(filename):
    return os.path.exists(filename)