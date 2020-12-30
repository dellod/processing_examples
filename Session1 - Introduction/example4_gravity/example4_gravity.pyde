# Session1 - Introduction: Example 4
# SCRP
# Daryl Dang

# Globals
x_position = 250
y_position = 25
circle_diameter = 50
velocity_y = 0
gravity = 1
bounce_direction = -1
bottom_of_screen = 500 - (circle_diameter / 2)

def setup():
    size(500, 500)
    smooth() # Removes anti_aliasing

def draw():
    background(0)
    
    # Draw ball.
    global x_position
    global y_position
    ellipse(x_position, y_position, circle_diameter, circle_diameter)
    
    # Have ball bounce
    global velocity_y
    velocity_y += float(gravity) / 10
    y_position += velocity_y
    
    if y_position > bottom_of_screen:
        velocity_y *= bounce_direction
