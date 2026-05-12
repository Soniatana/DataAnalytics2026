import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# Sample calculations
sample_sum = sum(vals_sample)
sample_average = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

# Choices calculations
choices_average = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)

# Circle calculations
area = pi * (radius ** 2)

rounded_up = math.ceil(area)
rounded_down = math.floor(area)

print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", sample_sum)
print("Average of 75 sample values:", sample_average)
print("Median of 75 sample values:", sample_median)

print('\n')

print("_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", choices_average)
print("Median of 200 values:", choices_median)
print("Mode of 200 values:", choices_mode)
print("Standard deviation of 200 values:", choices_stdev)

print('\n')

print("_Modeling a random circle:")
print("Radius =", radius, ", area =", rounded_up, "(rounded up)")
print("Radius =", radius, ", area =", rounded_down, "(rounded down)")