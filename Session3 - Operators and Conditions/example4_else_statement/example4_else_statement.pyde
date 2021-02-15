# Session3 - Operators and Conditions: Example 4 - else statement
# SCRP
# Daryl Dang

"""
Showcase the basic usage of if-else statements.
"""
# With booleans
is_it_cold_outside = False

if is_it_cold_outside:
    print("Put on a jacket")
else:
    print("Don't wear a jacket")
    
# With integers
a = 521
b = 300

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b") # This is not necessarily true, will demonstrate why in other examples.
