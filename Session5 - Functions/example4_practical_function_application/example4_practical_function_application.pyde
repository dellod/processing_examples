# Session5 - Functions: Example 4 - Practical Function Application
# SCRP
# Daryl Dang

"""
This example will show the practical application of functions and how
it helps with code reuse.
"""

def get_biggest_number(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    elif a == b:
        return "Both numbers are equal"
    
# If we were not using functions, we would have to
# program the same logic in the function EVERY single
# time for each set of numbers.
print(get_biggest_number(1234567, 402104))
print(get_biggest_number(1, 9999999))
print(get_biggest_number(24, 24))
