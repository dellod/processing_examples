#Tessa Arnett
#Drawing Program

#GLOBAL VARIABLES
m = 12 #number of colours for mouse wheel
colours = ['#FF0000', '#FE03FF', '#FF9600', '#FFFF00', '#00FF00', '#00FFFF', '#0000FF', '#9600FF', '#7C5632', '#000000', '#808080', '#FFFFFF']
pen_colour = '#FFFFFF'
X = 1450 #canvas width(x)
Y = 900 #canvas height(y)
Z = 790 #top of colour boxes
A = 100 #length of colour boxes
B = 100 #width of colour boxes
D = 110 #starting x position of colour boxes
C = 1 #for colour boxes

#background
def setup():
    background(255)
    size(X, Y)
    noStroke()
    
def draw():
    global pen_colour, i, Lx, Rx, m, Z, A, B, colours, D, C
    
#square under mouse size (part of HUD)
    fill('#434343')
    rect(1330, 780, 1330, 120)
    
#HUD
    fill('#434343')
    rect(0, 780, 1330, 120)
    
#colour square options
    C = 0 #x coordinate of colour boxes
    while C <= 11:
        fill(colours[C]) #cannot call 12 different colours, needs to be C
        rect(D*C+10, Z, A, B)
        C += 1

#What I had before I made the loop             
    # fill('#FF0000')         #red
    # rect(10, 790, 100, 100)
    # fill('#FE03FF')         #pink
    # rect(120, 790, 100, 100)
    # fill('#FF9600')         #orange
    # rect(230, 790, 100, 100)
    # fill('#FFFF00')         #yellow
    # rect(340, 790, 100, 100)
    # fill('#00FF00')         #green
    # rect(450, 790, 100, 100)
    # fill('#00FFFF')         #cyan
    # rect(560, 790, 100, 100)
    # fill('#0000FF')         #dark blue
    # rect(670, 790, 100, 100)
    # fill('#9600FF')         #purple
    # rect(780, 790, 100, 100)
    # fill('#7C5632')         #brown
    # rect(890, 790, 100, 100)
    # fill('#000000')         #black
    # rect(1000, 790, 100, 100)
    # fill('#808080')         #grey
    # rect(1110, 790, 100, 100)
    # fill('#FFFFFF')         #white
    # rect(1220, 790, 100, 100)
    
#colour selecting variables
    Lx = 10 #left bound
    Rx = 110 #right bound
    
    i = 0
    while i <= 11:
        if mouseX > Lx and mouseX < Rx and mouseY > 790 and mouseY < 890 and mouseButton == LEFT:
            pen_colour = colours[i]
            break
        Rx += 110
        Lx += 110
        i += 1
    
#mouse movement and size
    fill(pen_colour)
    if mouseButton == LEFT:
        circle(mouseX, mouseY, m)
        
#square under mouse size
    circle(1390, 840, m)
    
#change mouse size
def mouseWheel (event):
    e = event.getCount()
    global m
    m += event.getCount()
    m = m % 100
    if m < 12:
        m = 12
    if m >= 97:
        m = 97
