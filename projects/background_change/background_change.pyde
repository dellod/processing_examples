# background.pyde
# Cycles through background colours.
# SCRP
# Daryl Dang

# GLOBALS
# Initial colour setup.
RED = 255
GREEN = 0
BLUE = 0

def setup():
    size(500, 500)
    
def draw():
    global RED, GREEN, BLUE # Have to use keyword global here because we want to update global variables.
    background(RED, GREEN, BLUE) # Only have to call background one time using global variables.
    
    delay(500) # This delays the program by half a second ie. "pauses" the program. 
               # Makes much it easier to see colour changes.
    
    # If-else logic that we will discuss in session 3.
    if RED == 255:
        # Checks to see if the screen is red, if true, then we change it so GREEN will be the next background.
        RED = 0
        GREEN = 255
        BLUE = 0
    elif GREEN == 255:
        # Checks to see if the screen is green, if true, then we change it so BLUE will be the next background.
        RED = 0
        GREEN = 0
        BLUE = 255
    elif BLUE == 255:
        # Checks to see if the screen is blue, if true, then we change it so RED will be the next background.
        RED = 255
        GREEN = 0
        BLUE = 0
