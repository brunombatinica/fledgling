#VERSION 1 - no hyphen functionality
#allows basic editing of refence numbers - too broke to afford endnote
#want to add the integer value of all numbers within bracket to allow me to insert a refence

# future plans
#1. Test for - hyphen
#1. mek it read from a text filen
#2. make it read from a word file
#3. input speficic changes


#for now semi manual changes

#manually input text as a string
#text = raw_input("Copy the reference list now")

#read the test file
with open("text.txt") as a:
    text_input = a.readlines()

#initiate textoutput array
text_output = []

#go through each line in the textinput
for i in range(0,len(text_input)):
    #create temporary list
    templist = list(text_input[i])

    #iterate through that list
    for j in range(0,len(templist)):
        print templist[j]
        # condition = between []
        if templist[j] == "[":
            #initialize num and k
            num = ""
            k = 1

            #run from "[" untill you reach "]" , and add every charecter to the num string
            while not templist[j+k] == "]":
                num += templist[j+k]
                k += 1

            #test num
            try:
                num = str(int(num)+1)

            except ValueError:
                print "number index " + num

            #increment num
            num = str(int(num))
            print "number index" + num

            #change number
            for l in range(0,len(num)):
                templist[j+1+l] = num[l]
                print num[l]
                print templist[l]


    #populate textoutput
    text_output.append("".join(templist))
    #clear templist - not necessary
    templist = []


    #other possible method
    #index = text[i].find("[")
    #print index

#writing ouput
with open("textoutput.txt","w") as textoutput:
        for line in text_output:
            textoutput.write(line)
