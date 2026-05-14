f = open("about_me.txt", "a")

f.write("\nPerfect night out: Dinner and bowling with friends.")

f.close()

f = open("about_me.txt", "r")

print(f.read())

f.close()

f = open("about_me.txt", "r")

print(f.read(50))
print(f.read(50))

f.close()

f = open("about_me.txt", "r")

print(f.readline(10))
print(f.readline())

for i in range(1, 5):
    print(f.readline())

f.close()

f = open("about_me.txt", "r")

print(f.readlines(1))
print(f.readlines(1))
print(f.readlines(10))

f.close()

['Name: Sonia\n', 'Place of Birth: Cameroon\n']

f = open("about_me.txt", "r")

# First variable using .read(50)
first_part = f.read(50)

# Second variable using readline()
next_lines = []

for i in range(4):
    next_lines.append(f.readline())

# Third variable using readlines(100)
remaining_lines = f.readlines(100)

print("First 50 characters:")
print(first_part)

print("\nNext four lines, as list by line:")
print(next_lines)

print("\nNext 100 characters, as list by line:")
print(remaining_lines)

f.close()


