i = 1
test = 1

# this is dodgey as we run the same test twice
while i<100:
    if (i % 3) != 0 and (i % 5) != 0:
        print(i),
    else:
        if (i % 3) == 0:
            print("fizz"),
            test = 0

        if (i % 5) == 0:
            print("buzz"),
            test = 0



    print("")
    i += 1
    test = 1
