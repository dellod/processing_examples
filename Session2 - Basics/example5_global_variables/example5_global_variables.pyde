# Session2 - Basics: Example 5 - Global Variables
# SCRP
# Daryl Dang

# GLOBAL VARIABLES
a = 1 # This variable is global since it is not defined in any function

def setup():
    print("This gets printed at the very start of the program")

def draw():
    global a # This keyword is necessary so we can access variable a
    
    # After using the global keyword, we can use the variable however we like
    a = a + 1
    print(a)
    
    
    
    
    
