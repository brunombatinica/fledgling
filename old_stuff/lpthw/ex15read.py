#reading files

#argv syntax
from sys import argv as a # as a is not necessary

script, filename = a

txt = open(filename)

print("title:",filename)
print(txt.readline(15))

"""
#input syntax
print("what file do you want to read?")
txt2 = open(input(">"))
print(txt2.read())
"""
