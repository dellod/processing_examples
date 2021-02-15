# Session3 - Operators and Conditions: Example 5 - elif statement
# SCRP
# Daryl Dang

"""
Showcase the basic usage of an elif statement.
"""
# Temperature example
# Try to think of these if-else branches on a number spectrum...
temp_in_celsius = 0

if temp_in_celsius >= 20:
    print("Wear shorts")
elif temp_in_celsius >= 10:
    print("Wear normal clothes")
elif temp_in_celsius >= 0:
    print("Put on a sweater")
elif temp_in_celsius >= -10:
    print("Put on a jacket")
else:
    print("Stay inside...")

print("Reached the end of the temperature example.")

# Integers example
a = 10
b = 10

if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")
    
print("Reached the end of the integer example.")
