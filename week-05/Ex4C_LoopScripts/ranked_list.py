foods = ["pizza", "tacos", "ramen", "burger", "pasta"]

for i, food in enumerate(foods, start=1):
    if i == 1:
        print(str(i) + ". " + food + " < top pick!")
    else:
        print(str(i) + ". " + food)