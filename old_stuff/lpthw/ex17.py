#copy a file
from sys import argv
from os.path import exists

# format script old file new file
script, from_file, to_file = argv

indata = open(from_file).read()

print(f"The inpur is {len(indata)} bytes long")

print("does the output file exist?")
print(exists(to_file))

input("CTLR^C to abort")

open(to_file,'w').write(indata)

#out_file.close()
#in_file.close()
