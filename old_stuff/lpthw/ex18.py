#Names, Variables, Code, Functions

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#*args is pointless can do
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("i got nothin")

print_two("bruno","batinica")
print_two_again("bruno","batinica")
print_one("one")
print_none()
