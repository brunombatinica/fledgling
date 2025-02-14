#Functions and Variables

def cc(cheese,crackers):
    cheese += 10
    global a
    a = cheese
    print(f"you have {cheese} cheese")

    print(f"you have {crackers} crackers")

#can feed funciton numbers directly or feed it Variables
cc(10,20)
a = 10
print(a)

cheese = 100
crackers = 200

#notice how they are inputted backwards the function doesnt care
cc(crackers,cheese)
cc(cheese,crackers)

#notice how it is not affected by the function unless global is declared
# you can't global a parameter
print(cheese)

print(a)
