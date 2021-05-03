# Session2 - Basics: Example 7 - Advanced Bouncing Ball
# SCRP
# Daryl Dang
import time
# Globals
x_position = 25
y_position = 25
circle_diameter = 50
velocity_y = 0
velocity_x = 2
gravity = 10
bounce_direction = -1
bottom_of_screen = 500 - (circle_diameter / 2)

def setup():
    size(500, 500)
    smooth() # Removes anti_aliasing
    time.sleep(5)

def draw():
    background(0)
    
    # Draw ball.
    global x_position
    global y_position
    ellipse(x_position, y_position, circle_diameter, circle_diameter)
    
    # Have ball bounce up and down
    global velocity_y
    velocity_y += float(gravity) / 10
    y_position += velocity_y
    
    # Have ball move to the right
    x_position += velocity_x
    
    if y_position > bottom_of_screen:
        velocity_y *= bounce_direction
