#reading and writing

from sys import argv

script,filename = argv

print(f"We're going to erase {filename}")
print("if you dont want that hit CTRL-C")
#gives you a chance to cancel the code
input("else hit that return button")

print("Opening the file...")
target = open(filename,'w')

target.truncate()

line1 = input("what do you to write in the file (line 1) ")
line2 = input("what do you to write in the file (line 2) ")

target.write(line1 + "\n" + line2)
target.close()
