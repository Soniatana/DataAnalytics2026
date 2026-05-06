# Years = 72 ÷ interest_rate 

savings = 1000
interest_rate = 6  # percent

years = 72 / interest_rate
double_amount = savings * 2

print("Your current savings is " + str(savings))
print("At a " + str(interest_rate) + "% interest rate, your savings account will be worth " + format(double_amount, ".2f") + " in " + format(years, ".1f") + " years")