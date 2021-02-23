# Session4 - Lists and Loops: Example 5 - Lists and Loops
# SCRP
# Daryl Dang

"""
This example will go over how to iterate through a list using a while loop.
"""

names = ["Alice", "Bob", "Carl"]
names_size = len(names) # This function will get the size of the list

print("Size of the name list is: " + str(names_size))

i = 0
while i < names_size:
    print("Name " + str(i) + ":" + names[i]) # How can we make this more simple?
    i += 1
