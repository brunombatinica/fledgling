#Functions and files

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline(),end = "")


current_file = open(input_file)

print("print whole file")
print_all(current_file)

rewind(current_file)

print("first 3 lines")
for i in range(1,4):
    print_a_line(i,current_file)
