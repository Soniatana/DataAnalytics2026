sales = [
    ("Marcus Webb", "East", 4250.00),
    ("Priya Sharma", "West", 5875.50),
    ("DeShawn Carter", "East", 3100.75),
    ("LaTonya Rivers", "South", 6420.00),
    ("Bob Nguyen", "West", 4980.25)
]

total_sales = 0

for name, region, amount in sales:
    print(name + " (" + region + "): $" + format(amount, ".2f"))

    if amount > 5000:
        print("^ Top performer!")

    total_sales += amount

print("Total sales: $" + format(total_sales, ".2f"))