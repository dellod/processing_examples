# Session2 - Basics: Example 4 - Number Bomb
# SCRP
# Daryl Dang

import time # Need this library so your program can be paused.

# GLOBAL VARIABLES
x = 1

def setup():
    size(500, 500)
    print("This will be printed at the very start of the program")
    time.sleep(5) # This waits 5 seconds before continuing the rest of the program.
    
def draw():
    global x # This declares that x is going to be used as a global variable.
    x = x * 2 # Multiply x by 2 every time and make it equal to that new value.
    print(x)
