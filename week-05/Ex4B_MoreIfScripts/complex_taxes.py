pay_rate = 20
hours_worked = 40
filing_status = "single"

if hours_worked <= 40:
    weekly_pay = pay_rate * hours_worked
else:
    overtime_hours = hours_worked - 40
    weekly_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)

    annual_income = weekly_pay * 52

annual_income = weekly_pay * 52

# determine tax rate first
if filing_status == "single":
    if annual_income < 12000:
        tax_rate = 0.05
    elif annual_income < 25000:
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == "joint":
    if annual_income < 12000:
        tax_rate = 0.00
    elif annual_income < 25000:
        tax_rate = 0.06
    elif annual_income < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

tax_withheld = weekly_pay * tax_rate
net_pay = weekly_pay - tax_withheld

print("You worked", hours_worked, "hours this period.")
print("Your gross weekly pay is $", format(weekly_pay, ".2f"))
print("Your filing status is", filing_status)
print("Your tax withholding is $", format(tax_withheld, ".2f"))
print("Your net pay is $", format(net_pay, ".2f"))

