#https://thispointer.com/python-capitalize-the-first-letter-of-each-word-in-a-string/#:~:text=Use%20title()%20to%20capitalize,of%20word%20to%20lower%20case.
input = raw_input("write the sentence you want to capitalize... ")
list = list(input)
len = len(list)

list[0] = input[0].upper()

#test through string
for x in range(1,len):
    if list[x-1] == " ":
        list[x] = input[x].upper()

#initize empty string
str = ""

# turn list to string
for x in list:
    str += x

#print output
print(str)
