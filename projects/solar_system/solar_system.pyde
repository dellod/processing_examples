# solar_system.pyde
# SCRP
# Daryl Dang

# --- Globals ---
# Screen properties
width_of_screen = 1200
height_of_screen = 1200
center_of_screen = (width_of_screen / 2, height_of_screen / 2)
background_space_colour = 0

# Constants
PLANET_SCALE = 10000

# Planets (use scale of ~1:1000 km)
sun_diameter =  1392700 / PLANET_SCALE
sun_colour =(255, 247, 3)


def setup():
    size(width_of_screen, height_of_screen)
    print("Hello World!")
    
def draw():
    # Draw background.
    background(background_space_colour)
    
    # Draw Sun.
    circle(center_of_screen[0], center_of_screen[1], sun_diameter)
    fill(sun_colour[0], sun_colour[1], sun_colour[2])
    
    # Draw Mercury.
    
    # Draw Venus.
    
    # Draw Earth
    
    # Draw Mars.
    
    # Draw Jupiter.
    
    # Draw Saturn.
    
    # Draw Uranus.
    
    # Draw Neptune.
    
    # Draw Pluto (not a planet).
