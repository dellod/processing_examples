# Session5 - Functions: Example 10 - keyPressed
# SCRP
# Daryl Dang

"""
This example will showcase basic usage of Processing's 
keyPressed function.
"""

# GLOBAL VARIABLES
counter = 0

# NEED to have setup defined.
def setup():
    size(500, 500)

# NEED to have draw defined.
def draw():
    circle(250, 250, 50)

def keyPressed():
    global counter
    counter += 1
    print(counter)
