import math

length = 10
width = 12

area = length * width

extra = area * 1.10

boxes_needed = math.ceil(extra / 12)

print("Boxes needed: " + str(boxes_needed))