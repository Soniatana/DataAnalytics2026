def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(city + ",", state, zip_code)

display_mailing_label(
    "Sonia Tana",
    "123 Main Street",
    "Charlotte",
    "NC",
    "28202"
)

print("\n")

display_mailing_label(
    "John Smith",
    "456 Oak Drive",
    "Atlanta",
    "GA",
    "30301"
)   

print("\n")

add_numbers(5)

add_numbers(3, 7)

add_numbers(1, 2, 3, 4, 5)

def display_receipt(total_due, amount_paid):

    print("Total Due: $", total_due)
    print("Amount Paid: $", amount_paid)

    if amount_paid > total_due:
        change = amount_paid - total_due
        print("Change Due: $", change)

    elif amount_paid == total_due:
        print("Change Due: $0")

    else:
        balance = total_due - amount_paid
        print("Remaining Balance: $", balance)

        print("\n")

# Overpay
display_receipt(20, 30)

print("\n")

# Exact payment
display_receipt(20, 20)

print("\n")

# Underpay
display_receipt(20, 10)