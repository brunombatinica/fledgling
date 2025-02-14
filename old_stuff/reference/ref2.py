#VERSION 2 - attempted hyphen functionality
#allows basic editing of refence numbers - too broke to afford endnote
#want to add the integer value of all numbers within bracket to allow me to insert a refence

# future plans
#1. Take into acount changes in number length
#1. mek it read from a text filen
#2. make it read from a word file
#3. input speficic changes



#######################################################################################################
# check integer - python does it automatically but only to test class, here need to test if the string value is an integer
def isint(test):
    try:
        int(test)
        return True
    except ValueError:
        return False




#manually input text as a string
#text = raw_input("Copy the reference list now")

#read the test file
with open("text2.txt") as a:
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
        # condition find [ unique to references
        if templist[j] == "[":
            # j = index of "["
            # initialize k variable (from index "[" seaching for "]"
            print templist[j]
            k = j
            # test that not at the end "]" - using k varaible
            while not templist[k] == "]":
                #initialize num and p (seaching for int)
                num = ""
                p = 1

                #go through string from k and populate num
                while isint(templist[k+p]):
                    num += templist[k+p]
                    p+=1

                #increment num
                num2 = str(int(num)+1)

                #check if incrementation has changed "size"
                if len(num2) == len(num):
                    #change number
                    for l in range(0,len(num)):
                        templist[k+l+1] = num[l]
                else:
                    print ("you need to write more robust code")

                #increment k
                k += (len(num)+1)

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
