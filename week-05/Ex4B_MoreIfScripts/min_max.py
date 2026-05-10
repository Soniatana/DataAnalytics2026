a = 5
b = 12
c = 3

# Find smallest
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Find largest
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Smallest is", smallest)
print("Largest is", largest)