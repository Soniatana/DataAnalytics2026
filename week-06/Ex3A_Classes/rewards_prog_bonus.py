cust_list = []

class RewardsProgram:
    """This class represents a rewards program."""

class RewardsProgram:
    """This class represents a rewards program."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")
    def add_to_cust_list(self):
        cust_list.append(
            (self.cust_name, self.phone, self.email)

        )
customer1 = RewardsProgram(
    "Sonia",
    "704-123-4567",
    "sonia@email.com"
)

customer2 = RewardsProgram(
    "Mike",
    "980-111-2222",
    "mike@email.com"
)

customer3 = RewardsProgram(
    "Ashley",
    "980-333-4444",
    "ashley@email.com"
) 

customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

print()

customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

print()

customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()

print("\nCustomer List:")
print(cust_list)