print "which file do you want to rewrite?"
i = raw_input(">")

print "opening the file..."
fileread = open(i)

print "this file currently contains:"
text = fileread.read()
print text

print "are you sure you want to clear this file?"
j = raw_input("type 1 to continue or 0 to stop:")
k = 1
while k:
    try:
        j = int(j)
        break
    except:
        print "please enter a 1 or 0"
        j = raw_input(">")


if j == 1:
    print "truncating the file..."
    filewrite = open(i,"w")
    filewrite.truncate()

    print "you can now write 2 lines in"

    line1 = raw_input("line 1:")
    line2 = raw_input("line 2:")

    filewrite.write(line1)
    filewrite.write("\n")
    filewrite.write(line2)
    filewrite.write("\n")

    print "closing file..."
    filewrite.close()

    print "the file now says"
    fileread = open(i)
    text = fileread.read()
    print text

else:
    print "okay"
