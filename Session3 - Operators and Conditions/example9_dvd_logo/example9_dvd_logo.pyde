# Session3 - Operators and Conditions: Example 9 - DVD logo
# SCRP
# Daryl Dang

# GLOBAL VARIABLES
screen_width = 500
screen_height = 500
x_pos = 0
y_pos = 0
x_speed = 5
y_speed = 5
rect_width = 100
rect_height = 50

def setup():
    size(screen_width, screen_height)
    background(0)
    
def draw():
    global x_pos, y_pos, x_speed, y_speed

    # Redraw background
    background(0) # Black

    # Draw the rect
    rect(x_pos, y_pos, rect_width, rect_height)
    
    # Update the position of the rectangle
    x_pos += x_speed
    y_pos += y_speed
    
    # Check if hitting sides
    if (x_pos + rect_width) == screen_width or x_pos == 0:
        x_speed *= -1
        
    # Check if top or bottom side
    if (y_pos + rect_height) == screen_height or y_pos == 0:
        y_speed *= -1
        
    
