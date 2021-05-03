# Session3 - Operators and Conditions: Example 7.5.1 - Circle Going to The Right
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

def setup():
    size(screen_width, screen_height)
    background(0)
    
def draw():
    global x_pos, y_pos, x_inc_value

    # Redraw background
    background(0) # Black

    # Draw the circle
    circle(x_pos, y_pos, diameter)

    # Increment the position of the circle
    x_pos += x_inc_value
