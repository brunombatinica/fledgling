# #How long it will take you to save to buy a house

# #annual_salary = float(input("Enter your annual salary: "))
# #portion_saved = float(input("Enter the percent of your salary to save, as a decimal: " ))
# #total_cost = float(input("Enter the cost of your dream home: "))
# annual_salary = 1500000
# portion_saved = .05 
# total_cost = 1000000.0
# semi_annual_raise = .07

# current_savings = 0.0
# r = 0.04
# portion_down_payment = 0.25*total_cost
# months = 0


# while current_savings < portion_down_payment:
#     if months > 0 and months%6 == 0:
#         annual_salary += annual_salary * semi_annual_raise 
    
#     months += 1
#     current_savings += (current_savings * r / 12) + \
#         ((annual_salary / 12) * portion_saved)
        
#     print(current_savings)
    
    
# print("Number of months: {}".format(months))



#Best saving rate to get house in 36 months using bisection
#Within 100 of down payment

#annual_salary = float(input("Enter your annual salary: "))
#portion_saved = float(input("Enter the percent of your salary to save, as a decimal: " ))
#total_cost = float(input("Enter the cost of your dream home: "))

total_cost = 1000000.0
semi_annual_raise = .07

current_savings = 0.0
r = 0.04
portion_down_payment = 0.25*total_cost
solved = False
steps = 0


# use integer to limit float to 2 decimal places of accuracy
# out of 10000 so 0.5 = 5000
upper = 10000
lower = 0

while not solved and lower < 99990:  
    #reset variables
    current_savings = 0
    annual_salary = 3000000.0
    months = 0
    steps += 1
    
    saving_rate = round( (upper + lower) / 2 )

    
    for i in range(36):
        if months > 0 and months%6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        months += 1
        current_savings += (current_savings * r / 12) + \
            ((annual_salary / 12) * saving_rate/100000)

    print(lower)
    print(upper)
    print(saving_rate)
    print(current_savings - portion_down_payment) 
    if current_savings - portion_down_payment <= -100.0:
        lower = int(saving_rate)
        print("TOO LOW")
    elif current_savings - portion_down_payment >= 100.0:
        upper = int(saving_rate)
        print("TOO HIGH")
    else:
        solved = True
        print(current_savings- portion_down_payment)

    print("")
   
    
    
if solved:    
    print("best savings rate: {}".format(round(saving_rate)))
    print("steps in biseciton search {}".format(steps))
else:
    print("not possible given your salary")