# Session5 - Functions: Example 3 - Rectangle function
# SCRP
# Daryl Dang

"""
This example will show how a basic function that draws a
rectangle to screen.
"""
size(500, 500) # NOTE: ensure you are not calling the setup function here. 

def draw_rectangle(x, y, w, h):
    # 1. Draw the rectangle to screen
    rect(x, y, w, h)
    
    # 2. Print the coordinates of rectangle.
    print("Rectangle Coordinates: ({}, {})".format(x, y))
    
    # 3. Return the area of the rectangle.
    return w * h

# Call draw_rectangle and store the return value.
area = draw_rectangle(250, 250, 100, 50)
print("Area = {}".format(area))
    
