# Session5 - Functions: Example 2 - Addition function
# SCRP
# Daryl Dang

"""
This example will showcase a basic addition function using
parameters and return value.
"""

def addition(num1, num2):
    """
    num1 - (int/float)
    num2 - (int/float)
    """
    return num1 + num2

x = 521431
y = 192423
sum = x + y
print("We expect this value: " + str(sum))

function_sum = addition(x, y)
print("We get this from our function: " + str(function_sum))
