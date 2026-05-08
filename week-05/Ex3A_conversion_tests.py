# Description: This script tests various numeric
# conversion techniques
# Author: Sonia Tana

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# a conversions
a_int_fail = None
# int(a)  # ValueError: cannot convert decimal string directly to int

a_float = float(a)
a_int_from_float = int(float(a))

# b conversions
b_int = int(b)
b_float = float(b)

# c conversions
# int(c)  # ValueError: contains text
# float(c)  # ValueError: contains text

c_number = c[:3]  # slicing "402"
c_int = int(c_number)

# d conversions
# int(d)  # ValueError: contains text

d_number = d[-2:]  # gets "5 "
d_clean = d_number.strip()
d_int = int(d_clean)

