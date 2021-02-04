# Session2 - Basics: Example 6 - Moving Circle
# SCRP
# Daryl Dang

# GLOBAL VARIABLES
radius = 50
x_pos = 25 # Starting x position of circle
y_pos = 25 # Starting y position of circle

def setup():
    size(500, 500) # Set the display window size to 500 by 500 pixels.
    
def draw():
    global x_pos, y_pos, radius # Declare all of the global variables that we are going to be modifying
    circle(x_pos, y_pos, radius) # Draw the circle
    
    radius += 1 # Grow the size
    x_pos += 1 # Move the x position
    y_pos += 1 # Move the y position
