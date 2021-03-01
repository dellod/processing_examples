# Session5 - Functions: Example 8 - mouseX and mouseY
# SCRP
# Daryl Dang

"""
This example will showcase how to use mouseX and mouseY.
"""

def setup():
    size(500, 500)
    
def draw():
    background(0)
    # The circle will be drawn wherever your mouse is located on the display window.
    circle(mouseX, mouseY, 50)
