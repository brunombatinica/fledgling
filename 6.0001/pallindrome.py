#pallindrome using recursion

#Take string make all lowercase as strip unecessary charecter


def strip(phrase):
    lphrase = phrase.lower()
    a = ''
    for c in lphrase:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            a = a + c
    return a

#DONT FORGET HTE BASE CASE
def palindrome(x):
    if len(x) < 2:
        return 1
    elif x[0] == x[-1] and palindrome(x[1:-1]):
        return 1
    else:
        return 0
    
    
    
    
#phrase = input("What do you want to test? ")
#phrase = "Able was I Ere I  saw   ELBA"
phrase = "    Never ODD or    eve  n"

print(strip(phrase))
print(palindrome(strip(phrase)))




# for i,x in enumerate(lphrase):
#     if x == " ":
#         del(lphrase[i]) #ROOKIE MOVE
#     else:
#         lphrase[i] = lphrase[i].lower()

# output = "".join(lphrase)
# print(output)






    