# Session4 - Lists and Loops: Example 6 - for loops
# SCRP
# Daryl Dang

"""
This example will go over the basic usage of a for loop.
"""

# Basic example.
# Print every name in the list.
print("Example 1")
names = ["Alice", "Bob", "Carl"]

for name in names:
    print(name)

print("----------------------------")
# More practical/advanced example.
# Check if a number is even first, if even, print it.
print("Example 2")
numbers = [16, 3, 1, 56, 902, 101]

for num in numbers:
    # First check if the number is even using modulus.
    if (num % 2) == 0:
        # If true, then print even number.
        print("{} is an even number".format(num))
        
