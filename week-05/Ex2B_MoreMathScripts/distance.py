# formula distance = √((x2 - x1)^2 + (y2 - y1)^2)

import math

x1 = 1
y1 = 2
x2 = 4
y2 = 6

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance is " + format(distance, ".2f"))