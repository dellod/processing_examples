# solar_system.pyde
# SCRP
# Daryl Dang

# --- Globals ---
# Screen properties
width_of_screen = 1920
height_of_screen = 1080
center_of_screen = (width_of_screen / 2, height_of_screen / 2)
background_space_colour = 0

# Constants
RED = "0xFC0000"
GREEN = "#00FC2C"
PLAY = "PLAY"
PAUSE = "PAUSED"
PLANET_SCALE = 750
RADIUS_SCALE = 1900000
ORBITAL_SPEED_SCALE = 10
pi_factor = 0.0009

# Planets (use scale of ~1:1000 km)
# SUN
sun_diameter =  1392700 / 27000 # Have to use a separate scale for the sun.
sun_colour = (255, 247, 3)

# MERCURY
mercury_diameter = 4879 / PLANET_SCALE
mercury_orb_radius = 57900000 / RADIUS_SCALE
mercury_pi_factor = 0.01
mercury_orbital_speed = 47 / ORBITAL_SPEED_SCALE
mercury_colour = (196, 196, 196)

# VENUS
venus_diameter = 12104 / PLANET_SCALE
venus_orb_radius = 108250000 / RADIUS_SCALE
venus_pi_factor = 0.01
venus_orbital_speed = 35 / ORBITAL_SPEED_SCALE
venus_colour = (224, 224, 183)

# EARTH
earth_diameter = 12742 / PLANET_SCALE
earth_orb_radius = 147120000 / RADIUS_SCALE
earth_pi_factor = 0.01
earth_orbital_speed = 30 / ORBITAL_SPEED_SCALE
earth_colour = (19, 116, 232)

# MARS
mars_diameter = 6779 / PLANET_SCALE
mars_orb_radius = 226340000 / RADIUS_SCALE
mars_pi_factor = 0.01
mars_orbital_speed = 24 / ORBITAL_SPEED_SCALE
mars_colour = (216, 93, 15)

# JUPITER
jupiter_diameter = 139820 / 6000 # Have to use a separate scale for the Jupiter.
jupiter_orb_radius = 378500000 / RADIUS_SCALE
jupiter_pi_factor = 0.01
jupiter_orbital_speed = 13 / ORBITAL_SPEED_SCALE
jupiter_colour = (242, 185, 149)

# SATURN
saturn_diameter = 116460 / 6000 # Have to use a separate scale for the Saturn.
saturn_orb_radius = 1491400000 / 4000000 # Have to use a separate scale for the Saturn.
saturn_pi_factor = 0.01
saturn_orbital_speed = 10 / ORBITAL_SPEED_SCALE
saturn_colour = (252, 158, 99)

# URANUS
uranus_diameter = 50724 / 6000 # Have to use a separate scale for the Uranus.
uranus_orb_radius = 2957700000 / 5000000 # Have to use a separate scale for the Uranus.
uranus_pi_factor = 0.01
uranus_orbital_speed = 6.8 / ORBITAL_SPEED_SCALE
uranus_colour = (99, 241, 252)

# NEPTUNE
neptune_diameter = 49244 / 6000  # Have to use a separate scale for the Neptune.
neptune_orb_radius = 4476000000 / 6000000 # Have to use a separate scale for the Neptune.
neptune_pi_factor = 0.01
neptune_orbital_speed = 5.4 / ORBITAL_SPEED_SCALE
neptune_colour = (91, 137, 250)

# PLUTO
pluto_diameter = 2376 / PLANET_SCALE
pluto_orb_radius = 5900000000 / 6500000 # Have to use a separate scale for the Neptune
pluto_pi_factor = 0.01
pluto_orbital_speed = 4.7 / ORBITAL_SPEED_SCALE
pluto_colour = (144, 3, 31)

# Play/pause button
pp_button_colour = RED
pp_text = PLAY
time_value = 1

def setup():
    size(width_of_screen, height_of_screen)
    
def draw():    
    # Draw background.
    background(background_space_colour)
    
    # Play/pause button
    fill(255)
    textSize(32)
    text(pp_text, 50, 50)
    fill(pp_button_colour)
    circle(300, 40, 50)

    # Draw Sun.
    fill(sun_colour[0], sun_colour[1], sun_colour[2])
    circle(center_of_screen[0], center_of_screen[1], sun_diameter)
    
    # Draw Mercury.
    global mercury_pi_factor
    mercury_x = center_of_screen[0] + mercury_orb_radius * cos(mercury_pi_factor * PI)
    mercury_y = center_of_screen[1] + mercury_orb_radius * sin(mercury_pi_factor * PI)
    fill(mercury_colour[0], mercury_colour[1], mercury_colour[2])
    circle(mercury_x, mercury_y, mercury_diameter)
    mercury_pi_factor += mercury_orbital_speed * pi_factor * time_value
    
    # Draw Venus.
    global venus_pi_factor
    venus_x = center_of_screen[0] + venus_orb_radius * cos(venus_pi_factor * PI)
    venus_y = center_of_screen[1] + venus_orb_radius * sin(venus_pi_factor * PI)
    fill(venus_colour[0], venus_colour[1], venus_colour[2])
    circle(venus_x, venus_y, venus_diameter)
    venus_pi_factor += venus_orbital_speed * pi_factor * time_value

    # Draw Earth
    global earth_pi_factor
    earth_x = center_of_screen[0] + earth_orb_radius * cos(earth_pi_factor * PI)
    earth_y = center_of_screen[1] + earth_orb_radius * sin(earth_pi_factor * PI)
    fill(earth_colour[0], earth_colour[1], earth_colour[2])
    circle(earth_x, earth_y, earth_diameter)
    earth_pi_factor += earth_orbital_speed * pi_factor * time_value

    # Draw Mars.
    global mars_pi_factor
    mars_x = center_of_screen[0] + mars_orb_radius * cos(mars_pi_factor * PI)
    mars_y = center_of_screen[1] + mars_orb_radius * sin(mars_pi_factor * PI)
    fill(mars_colour[0], mars_colour[1], mars_colour[2])
    circle(mars_x, mars_y, mars_diameter)
    mars_pi_factor += mars_orbital_speed * pi_factor * time_value

    # Draw Jupiter.
    global jupiter_pi_factor
    jupiter_x = center_of_screen[0] + jupiter_orb_radius * cos(jupiter_pi_factor * PI)
    jupiter_y = center_of_screen[1] + jupiter_orb_radius * sin(jupiter_pi_factor * PI)
    fill(jupiter_colour[0], jupiter_colour[1], jupiter_colour[2])
    circle(jupiter_x, jupiter_y, jupiter_diameter)
    jupiter_pi_factor += jupiter_orbital_speed * pi_factor * time_value

    # Draw Saturn.
    global saturn_pi_factor
    saturn_x = center_of_screen[0] + saturn_orb_radius * cos(saturn_pi_factor * PI)
    saturn_y = center_of_screen[1] + saturn_orb_radius * sin(saturn_pi_factor * PI)
    fill(saturn_colour[0], saturn_colour[1], saturn_colour[2])
    circle(saturn_x, saturn_y, saturn_diameter)
    saturn_pi_factor += saturn_orbital_speed * pi_factor * time_value
    
    # Draw Uranus.
    global uranus_pi_factor
    uranus_x = center_of_screen[0] + uranus_orb_radius * cos(uranus_pi_factor * PI)
    uranus_y = center_of_screen[1] + uranus_orb_radius * sin(uranus_pi_factor * PI)
    fill(uranus_colour[0], uranus_colour[1], uranus_colour[2])
    circle(uranus_x, uranus_y, uranus_diameter)
    uranus_pi_factor += uranus_orbital_speed * pi_factor * time_value
    
    # Draw Neptune.
    global neptune_pi_factor
    neptune_x = center_of_screen[0] + neptune_orb_radius * cos(neptune_pi_factor * PI)
    neptune_y = center_of_screen[1] + neptune_orb_radius * sin(neptune_pi_factor * PI)
    fill(neptune_colour[0], neptune_colour[1], neptune_colour[2])
    circle(neptune_x, neptune_y, neptune_diameter)
    neptune_pi_factor += neptune_orbital_speed * pi_factor * time_value
    
    # Draw Pluto (not a planet).
    global pluto_pi_factor
    pluto_x = center_of_screen[0] + pluto_orb_radius * cos(pluto_pi_factor * PI)
    pluto_y = center_of_screen[1] + pluto_orb_radius * sin(pluto_pi_factor * PI)
    fill(pluto_colour[0], pluto_colour[1], pluto_colour[2])
    circle(pluto_x, pluto_y, pluto_diameter)
    pluto_pi_factor += pluto_orbital_speed * pi_factor * time_value
    
def mouseClicked():
    global pp_button_colour
    global pp_text
    global time_value
    if pp_button_colour == RED:
        pp_text = PAUSE
        pp_button_colour = GREEN
        time_value = 0
    else:
        pp_text = PLAY
        pp_button_colour = RED
        time_value = 1
    
