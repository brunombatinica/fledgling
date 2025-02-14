height_cm = False
input = raw_input("Enter a number in cm to convert it to inches ")

# try make this more elegant when you get better at python
while height_cm == False:
    try:
        height_cm = float(input)
    except:
        input = raw_input("please input a positive number ")

while height_cm < 0:
    input = raw_input("please input a positive number ")
    try:
        height_cm = float(input)
    except:
        input = raw_input("please input a positive number ")

height_inches = height_cm * 0.393701
height_feet = [height_inches / 12 , height_inches % 12]

print "%dcm is %f inches" % (height_cm,height_inches)
print "%f inches in feet is %d\' %f\"" % (height_inches, height_feet[0],height_feet[1])
