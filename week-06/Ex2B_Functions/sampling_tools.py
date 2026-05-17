import random

products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]

product_day = random.choice(products)

print("Product of the Day:", product_day)

survey_products = random.sample(products, 3)

print("Survey Products:", survey_products)

import random

products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]

# Product of the Day
product_day = random.choice(products)
print("Product of the Day:", product_day)

# Select 3 products for survey
survey_products = random.sample(products, 3)
print("Survey Products:", survey_products)

# Shuffle products list
random.shuffle(products)
print("Shuffled Products:", products)

# Generate random transaction count
transaction_count = random.randint(50, 300)
print("Daily Transaction Count:", transaction_count)