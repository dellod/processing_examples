# Session4 - Lists and Loops: Example 7 - Drawing Multiple Shapes
# SCRP
# Daryl Dang

"""
This example will draw multiple shapes across the display window.
"""

# GLOBAL VARIABLES
circle_rad = 50
starting_x_pos = 50
initial_y_origin = 25
starting_y_pos = initial_y_origin
falling_speed = 3
screen_w = 500
screen_h = 500
circle_colour = [random(0, 255), random(0, 255), random(0, 255)]

def setup():
    size(screen_w, screen_h)
    smooth() # Creates anti-aliased edges
    
def draw():
    global starting_y_pos
    background(255)
    i = 1
    while i <= 9:
        fill(circle_colour[0], circle_colour[1], circle_colour[2])
        circle(starting_x_pos * i, starting_y_pos, circle_rad)
        i += 1
    
            
