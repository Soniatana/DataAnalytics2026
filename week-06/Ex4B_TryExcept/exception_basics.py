try:
    age = int("hello")

except ValueError:
    print("ValueError: You entered text instead of a number.")

else:
    print(age)

finally:
    print("Let's try another one...\n")

    print("Let's try another one...")

try:
    print(username)

except NameError:
    print("NameError: Variable does not exist.")

else:
    print(username)

finally:
    print("Let's try another one...\n") 

try:
    result = "5" + 5

except TypeError:
    print("TypeError: Cannot add text and numbers together.")

else:
    print(result)

finally:
    print("Let's try another one...\n")
    