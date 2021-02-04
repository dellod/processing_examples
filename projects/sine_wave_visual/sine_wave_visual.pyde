# sine_wave_visual.pyde
# A visual representation of a sine wave.
# SCRP
# Daryl Dang

# CONSTANTS
X_SPACING = 16
WIDTH = 0

# GLOBAL VARIABLES
theta = 0 # Start angle
amp = 75 # Height of wave
period = 500 # Pixels before the wave repeats
dx = 0 # Value for incrementing x 
y_values = [] # Store height values for wave

def setup():
    global WIDTH, y_values, dx
    size(640, 360)
    WIDTH = width + X_SPACING
    dx = (TWO_PI / period) * X_SPACING
    y_values = [0] * (WIDTH / X_SPACING)
    smooth() # Removes anti_aliasing

def draw():
    background(0)
    print(dx)
    calc_wave()
    render_wave()
    
def calc_wave():
    global theta, y_values
    # Increment theta
    theta += 0.02
    
    # Every x value, calculate y value with sine function
    x = theta
    
    i = 0
    for i in range(len(y_values)):
        y_values[i] = sin(x) * amp
        x += dx
        i += 1
        
def render_wave():
    noStroke()
    x = 0
    for x in range(len(y_values)):
        fill(random(0, 255), random(0, 255), random(0, 255))
        ellipse(x * X_SPACING, (height / 2) + y_values[x], X_SPACING, X_SPACING)
        x += 1
    
