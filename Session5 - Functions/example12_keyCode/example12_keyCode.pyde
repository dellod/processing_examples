# Session5 - Functions: Example 12 - keyCode
# SCRP
# Daryl Dang

"""
This example will showcase the basic usage of Processing's
keyCode keyword and how you can use it to perform specific 
actions with special keys.
"""

def setup():
    size(500, 500)
    
def draw():
    pass
    ### Uncommenting this section of code will also allow this code to work.
    ### However, you'll notice that there are much more print statements being
    ### written to console and that is due to the keyCode returning the last key
    ### pressed. Remember, keyPressed only is called when a key is actually pressed, 
    ### while draw is running the whole time your program is being run.
    # if keyCode == UP:
    #     print("The UP key is being pressed.")
    # elif keyCode == DOWN:
    #     print("The DOWN key is being pressed.")
    # elif keyCode == LEFT:
    #     print("The LEFT key is being pressed.")
    # elif keyCode == RIGHT:
    #     print("The RIGHT key is being pressed.")
        
def keyPressed():
    if keyCode == UP:
        print("The UP key is being pressed.")
    elif keyCode == DOWN:
        print("The DOWN key is being pressed.")
    elif keyCode == LEFT:
        print("The LEFT key is being pressed.")
    elif keyCode == RIGHT:
        print("The RIGHT key is being pressed.")
 
    
    
