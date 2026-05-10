balance = 100
goal = 500
weekly_savings = 75

while balance < goal:
    balance += weekly_savings
    print("This week my balance increased to", balance)

if balance > goal / 2:
        print("Almost there! This week my balance is up to", balance)

if balance >= goal * 0.75:
        balance -= 20  # treat yourself
        print("So close! After treating myself, my balance is up to", balance)

print("Goal met! My current balance is", balance)