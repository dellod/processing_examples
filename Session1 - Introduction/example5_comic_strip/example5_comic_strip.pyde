# Session1 - Introduction: Example 5 - Comic Strip
# SCRP
# Daryl Dang

# First define the size of the screen
size(1920, 480)

# Store the screen width and height so they can be used to evenly divide the screen.
# NOTE: We cannot use these variables directly in the size function without the
#       setup function. Will be discuseed in future sessions.
screen_width = 1920
screen_height = 480

# Define other useful variables.
segments = 1920 / 4
top_screen = 0
bot_screen = screen_height

# Create default background (white).
background(255)

# Create panel grids.
line(segments * 1, top_screen, segments * 1, bot_screen)
line(segments * 2, top_screen, segments * 2, bot_screen)
line(segments * 3, top_screen, segments * 3, bot_screen)

# 1. Create first comic panel.
# Draw computer
fill(0)
rect(80, 80, 340, 240) # Border
rect(100, 100, 300, 200) # Main screen
photo = loadImage("1.png")
image(photo, 101, 101, 299, 199)
ellipse(250, 390, 100, 30) # Base
fill(100)
rect(230, 320, 40, 70) # Neck

# Draw text bubble
fill(255)
rect(10, 350, 200, 100, 7) # The extra paramenter at the end curves the edges
first_panel_text = "*sigh* programming is SO boring..."
textSize(18)
fill(0)
text(first_panel_text, 20, 370, 190, 100)

# 2. Create second comic panel.
photo2 = loadImage("2.png")
image(photo2, 481, 0, 478, 479)
second_panel_text = "DP participants"
textSize(18)
fill(0)
text(second_panel_text, 550, 25)

# 3. Create third comic panel.
# Draw computer
fill(0)
rect(1040, 80, 340, 240) # Border
rect(1060, 100, 300, 200) # Main screen
photo3 = loadImage("3.png")
image(photo3, 1061, 101, 299, 199)
ellipse(1210, 390, 100, 30) # Base
fill(100)
rect(1190, 320, 40, 70) # Neck

# Draw text
third_panel_text = "*changes slide to draw figure assignment*"
textSize(18)
fill(0)
text(third_panel_text, 1025, 70)

# 4. Create fourth comic panel.
photo4 = loadImage("4.jpg")
image(photo4, 1441, 0, 478, 479)
