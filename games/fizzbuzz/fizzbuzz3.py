#fizz buzz with user inputted condition

#inputs/conditions
trials = input("over what number do you want to fizz buzz? ") #ideally test this
tests = [3,5,10]
words = ["fizz","buzz","boing"]

#test if ararys are of equal size
if len(tests) != len(words):
    tests = raw_input("please try again")

#setting up the variables
i = 0
index = 0
output = ""

while i<=trials:
    for x in tests:
        if (i % x) == 0:
            output += words[index]
        index += 1
    if output == "":
        output = i

    print(output) #print output
    #reset variables
    output = ""
    i += 1
    index = 0
