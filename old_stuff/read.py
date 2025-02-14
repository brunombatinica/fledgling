print "which file do you want to open"
filename = raw_input("> ")
print filename

text = open(filename)

print "how many times do you want it to print"
number = raw_input("> ")
n = int(number)

print (text.read()+"\n")*n
