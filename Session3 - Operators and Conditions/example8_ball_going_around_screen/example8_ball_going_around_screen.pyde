# Session3 - Operators and Conditions: Example 8 - Ball Going Around Screen
# SCRP
# Daryl Dang

# GLOBAL VARIABLES
screen_width = 500
screen_height = 500
diameter = 100

default_inc_value = 5 # Default increment value
initial_x = diameter / 2
initial_y = diameter / 2
x_pos = initial_x # Initial x position of circle
x_inc_value = default_inc_value # Initial x increment value
y_pos = initial_y # Initial y position of circle
y_inc_value = 0

def setup():
    size(screen_width, screen_height)
    background(0)
    
def draw():
    global x_pos, y_pos, x_inc_value, y_inc_value

    # Redraw background
    background(0) # Black

    # Draw the circle
    circle(x_pos, y_pos, diameter)
    
    # Check if we hit the top right side of the screen.
    if x_pos >= (screen_width - initial_x) and y_pos <= initial_y:
        x_inc_value = 0
        y_inc_value = default_inc_value
    # Check if we hit the bottom right of the screen.
    elif y_pos >= (screen_height - initial_y) and x_pos >= (screen_width - initial_x):
        x_inc_value = default_inc_value * -1 # Go backwards
        y_inc_value = 0
    # Check if we hit the bottom left of the screen.
    elif x_pos <= initial_x and y_pos >= (screen_height - initial_y):
        x_inc_value = 0
        y_inc_value = default_inc_value * -1 # Go back up
    # Check if we hit the top left of the screen (initial start).
    elif y_pos <= initial_y and x_pos <= initial_x:
        x_inc_value = default_inc_value
        y_inc_value = 0

    # Increment the position of the circle
    x_pos += x_inc_value
    y_pos += y_inc_value
