# Session1 - Introduction: Example 3
# SCRP
# Daryl Dang

size(500, 500) # Set display window to be 500x500 pixels.

# Draw background.
background(100, 0, 0) 

# Draw a head.
fill(0, 255, 0)
ellipse(250, 200, 50, 50) # Head.

fill(255)
ellipse(237, 200, 10, 10) # Left eye.
ellipse(263, 200, 10, 10) # Right eye.

fill(255, 255, 0)
ellipse(250, 215, 15, 15) # Mouth.

# Draw stick body.
line(250, 225, 250, 350) # Main torso.
line(225, 275, 275, 275) # Both arms.
line(250, 350, 225, 375) # Left leg.
line(250, 350, 275, 375) # Right leg.

# Draw hat.
fill(255, 0, 255)
rect(225, 160, 50, 25)
