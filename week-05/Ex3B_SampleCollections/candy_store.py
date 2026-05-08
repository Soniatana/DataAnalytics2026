# Tuples

candies = ("Gummy Bears", "Lollipop", "Chocolate")
flavors = ("Strawberry", "Mango", "Blueberry")

# Set for combinations
candy_combos = set()

# Add combinations
candy_combos.add(candies[0] + " - " + flavors[1])
candy_combos.add(candies[1] + " - " + flavors[2])
candy_combos.add(candies[2] + " - " + flavors[0])

print("Today's candy options include:")
print(candy_combos)

# Print multiple times (for the question)
print(candy_combos)
print(candy_combos)