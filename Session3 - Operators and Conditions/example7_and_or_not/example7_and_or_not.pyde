# Session3 - Operators and Conditions: Example 7 - and, or, not
# SCRP
# Daryl Dang

"""
Showcase the basic usage of and, or, not operators.
Comment/uncomment when going through each example.

Which statements get printed to the console?
"""
print("Start of program...")
# and example 1
a = 5
b = 10

if a > b and b > 1:
    print("and example 1")
    
# and example 2
x = 50
y = 25

if (x / y) == 2 and (x + y) >= 20:
    print("and example 2")
    
# and example 3
bool_value = True
w = 7
s = "test"

if s == "test" and bool_value and ((w + 15) / 2) == 11:
    print("and example 3")
    
# or example 1
a = 71
b = 24

if a <= 51 or (b / 1) == 24:
    print("or example 1")

# or example 2
x = 101
y = 481

# This is the first time seeing the modulus operator.
# It instead returns the remainder of division.
if (x * 3) >= 313 or (y % 2) == 0:
    print("or example 2")

# or example 3
val1 = False
val2 = True
val3 = (((101.0 + 202.0 + 481.0) / 3.0) * (6.0 / (3.0 * 101.0))) > 5

if val1 or val2 or val3:
    print("or example 3")
    
# not example 1
a = 1
b = 6

if not(a == b):
    print("not example 1")
    
# not example 2
x = 21
y = 42
z = 63

if (not(z == 3) and not(x > y)) or not(z == 63):
    print("not example 2")
    
    
