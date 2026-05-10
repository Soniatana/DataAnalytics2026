# Create a list of numbers (this is your "pool")
numbers = [3, 7, 12, 18, 25, 30, 42, 55]

# Pick a number from the list (pretend it's random)
secret_number = numbers[3]   # you can change index if needed

print("Guess the number! It's between 1 and 60.")

guesses = []   # to store guesses
count = 0      # number of tries

while True:
    user_input = input("Enter your guess: ")

    # Handle non-numeric input
    if not user_input.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(user_input)
    guesses.append(guess)
    count += 1

    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print("🎉 Correct!")
        break

# After game ends
print("You guessed in", count, "tries")
print("Your guesses were:", guesses)

# Bonus condition
if count < 5:
    print("🔥 You're awesome!")