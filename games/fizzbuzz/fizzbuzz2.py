num = False
input = raw_input("What number do you want to fizzbuzz to? ")
i = 1

while bool(num) == False:
    try:
        num = int(input)
    except:
        input = raw_input("please write a number...")

while i <= num:
        print(i)

        i += 1
