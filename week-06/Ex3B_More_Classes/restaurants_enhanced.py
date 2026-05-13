class Restaurant:
    """This class represents a restaurant."""

class Restaurant:
    """This class represents a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type 

        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self, customers):
        self.number_served += customers 
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")
restaurant1 = Restaurant("Wendy's", "Fast Food")
restaurant2 = Restaurant("Olive Garden", "Italian")
restaurant3 = Restaurant("Chipotle", "Mexican")

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant2.describe_rest()
restaurant2.rest_open()

restaurant3.describe_rest()
restaurant3.rest_open()

def customer_rating(self, rating):

    if type(rating) == int and rating >= 1 and rating <= 5:

        self.customer_ratings.append(rating)

        average = sum(self.customer_ratings) / len(self.customer_ratings)

        print(f"Your rating was {rating}.")
        print(f"The average rating for this restaurant is {average}")

    else:
        print("Invalid rating. Please enter a whole number from 1-5.")

restaurant1 = Restaurant("Wendy's", "Fast Food")
restaurant2 = Restaurant("Olive Garden", "Italian")
restaurant3 = Restaurant("Chipotle", "Mexican")

restaurant1.describe_rest()
restaurant1.rest_open()

restaurant1.print_num_served()

restaurant1.add_num_served(15)
restaurant1.add_num_served(10)

restaurant1.print_num_served()

restaurant1.customer_rating(5)
restaurant1.customer_rating(4)
restaurant1.customer_rating(3)