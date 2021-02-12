# Session3 - Lists, Operators, and Conditions: Example 1 - Moving Circle Improved
# SCRP
# Daryl Dang

# GLOBAL VARIABLES
radius = 50
x_pos = 25 # Starting x position
y_pos = 25 # Staring  y position

def setup():
    size(500, 500) # Set the display window size to 500 by 500 pixels.

def draw():
    global x_pos, y_pos, radius # Declare all of the global variables that we are going to be modifying
    
    background(0) # This improves the previous iteration of the moving circle
    # This is necessary as it replaces the previously drawn
    # circle. That way, we don't get a huge line of circles.
    
    circle(x_pos, y_pos, radius) # Draw the circle
    radius += 1 # Grow the size
    x_pos += 1 # Move the x position
    y_pos += 1 # Move the y position
