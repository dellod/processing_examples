# Session5 - Functions: Example 11 - key
# SCRP
# Daryl Dang

"""
This example will showcase the basic usage of Processing's
key keyword and how you can use it to perform specific actions
with keys.
"""

def setup():
    size(500, 500)
    
def draw():
    pass
    ### Uncommenting this section of code will also allow this code to work.
    ### However, you'll notice that there are much more print statements being
    ### written to console and that is due to the key keyword returning the last key
    ### pressed. Remember, keyPressed only is called when a key is actually pressed, 
    ### while draw is running the whole time your program is being run.
    # if key == 'w' or key == 'W':
    #     print("The 'W' key is being pressed.")
    # elif key == 'a' or key == 'A':
    #     print("The 'A' key is being pressed.")
    # elif key == 's' or key == 'S':
    #     print("The 'S' key is being pressed.")
    # elif key == 'd' or key == 'D':
    #     print("The 'D' key is being pressed.")
        
def keyPressed():
    if key == 'w' or key == 'W':
        print("The 'W' key is being pressed.")
    elif key == 'a' or key == 'A':
        print("The 'A' key is being pressed.")
    elif key == 's' or key == 'S':
        print("The 'S' key is being pressed.")
    elif key == 'd' or key == 'D':
        print("The 'D' key is being pressed.")
 
    
    
