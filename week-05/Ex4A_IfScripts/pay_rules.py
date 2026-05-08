# Test case 1: under 40 hours
pay_rate = 12.50
hours_worked = 20

if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = (40 * pay_rate) + overtime_pay

print("Gross pay is $" + format(gross_pay, ".2f"))

# Test Case 2: Exactly 40 hours
pay_rate = 25.50
hours_worked = 40

if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = (40 * pay_rate) + overtime_pay

print("Gross pay is $" + format(gross_pay, ".2f"))

# Test Case 3: Over 40 hours
pay_rate = 17.30
hours_worked = 45

if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = (40 * pay_rate) + overtime_pay

print("Gross pay is $" + format(gross_pay, ".2f"))