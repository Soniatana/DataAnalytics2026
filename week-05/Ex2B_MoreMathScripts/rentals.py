import math

people = 38
van_capacity = 15
cost_per_van = 250

vans_needed = math.ceil(people / van_capacity)
total_cost = vans_needed * cost_per_van
cost_per_person = total_cost / people

print("Vans needed: " + str(vans_needed))
print("Total cost: $" + str(total_cost))
print("Cost per person: $" + format(cost_per_person, ".2f"))