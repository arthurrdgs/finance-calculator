import math

#choosing which calculation the user wants
calculation = input("Choose either 'investment' or 'bond' from the menu below to proceed:\ninvestment  -   to calculate the amount of interest you'll earn on your invesment.\nbond        -   to calculate the amount you'll have to pay on a home loan.").lower()
while (calculation != "investment") and (calculation != "bond"):
    print("Please select either 'investment' or 'bond'")
    calculation = input("Choose either 'investment' or 'bond' from the menu below to proceed:\ninvestment   -   to calculate the amount of interest you'll earn on your invesment.\nbond       - to calculate the amount you'll have to pay on a home loan.").lower()

#if the users select investment
if calculation == "investment":
    deposit = float(input("What is the amount of money you want to deposit?"))
    interest_rate = float(input("What is your interest rate? (Only numbers should be entered, e.g. '8')"))
    investment_time = int(input("How many years do you plan on investing for?"))
    interest = input("Do you want 'simple' or 'compound' interest?").lower()

#calculating the total amount if the interest is 'simple'. Formula  is A = P*(1+r*t)
    if  interest == "simple":
        total_amount = deposit*(1+((interest_rate/100)*investment_time))
        total_amount = "{0:.2f}".format(total_amount)
        print(f"The total amount you will have back after {investment_time} years is: £{total_amount}") 

#calculating the total amount if the interest is 'compound'. Formula is A = P* math.pow((1+r),t)
    elif interest == "compound":
        total_amount = deposit * math.pow((1+(interest_rate/100)),investment_time)
        total_amount = "{0:.2f}".format(total_amount)
        print(f"The total amount you will have back after {investment_time} years is: £{total_amount}") 

#if the user select bond
elif calculation == "bond":
    house_value = float(input("Enter the value of the house (e.g. 100000):"))
    interest_rate = float(input("What is your interest rate? (Only numbers should be entered, e.g. '8')"))
    repaying_time = int(input("How many months do you plan to repay the bond? (e.g. 120)"))
    
    #calculating the monthly amount the user will need to pay using the formula x = (i.P) / (1 - (1+i)^(-n))
    month_interest = interest_rate / 100 / 12
    monthly_amount = (month_interest*house_value) / (1 - (1+month_interest)**(-repaying_time))
    monthly_amount = "{0:.2f}".format(monthly_amount)
    print(f"You will need to pay £{monthly_amount} for {repaying_time} months.")

    
    
