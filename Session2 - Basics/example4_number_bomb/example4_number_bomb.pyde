# Session2 - Basics: Example 4 - Number Bomb
# SCRP
# Daryl Dang

# GLOBAL VARIABLES
x = 1

def setup():
    size(500, 500)
    print("This will be printed at the very start of the program")
    delay(3000) # This waits 3 seconds (3000ms) before continuing the rest of the program.
    
def draw():
    global x # This declares that x is going to be used as a global variable.
    x = x * 2 # Multiply x by 2 every time and make it equal to that new value.
    print(x)
