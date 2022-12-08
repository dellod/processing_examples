# Simon Ly 
# Billiards Game

def setup():
    global cue_ball_integer, game_over, game_win, diameter, pocket_diameter, mouse_to_ball_max_range, power_of_stick, max_power, border_width, pocket_condition, ball_list, win_counter, pocket_list, wood_border_list, cue_stick
    
    size(1920, 1080)
    #fullScreen()
    cue_ball_integer = 0
    game_over = 0
    game_win = 0
    diameter = 80
    pocket_diameter = 250
    stick_length = 250
    mouse_to_ball_max_range = diameter/2 + stick_length
    power_of_stick = 0
    max_power = 51
    border_width = 50 
    pocket_condition = (pocket_diameter/2)

    initializeballs()
    win_counter = 0
    win_condition = len(ball_list)
    
    pocket_topleft = Ball(Point(border_width, border_width), pocket_diameter, 0)
    pocket_topright = Ball(Point(width - border_width, border_width), pocket_diameter, 0)
    pocket_botright = Ball(Point(width - border_width, height - border_width), pocket_diameter, 0)
    pocket_botleft = Ball(Point(border_width, height - border_width), pocket_diameter, 0)
    
    pocket_list = [pocket_topleft, pocket_topright, pocket_botright, pocket_botleft]
    
    wood_border_top = wood_border(Point(0, 0), 1920, border_width, '#8B4513')
    wood_border_left = wood_border(Point(0, 50), border_width, 1030, '#8B4513')
    wood_border_right = wood_border(Point(1870, 50), border_width, 1030, '#8B4513')
    wood_border_bot = wood_border(Point(0, 1030), 1920, border_width, '#8B4513')
    
    wood_border_list = [wood_border_top, wood_border_left, wood_border_right, wood_border_bot]
    
    cue_stick = stick(stick_length)
             
def draw():
    draw_table()
    
    
class Point():
    def __init__ (self, x, y):
        self.x = x
        self.y = y;
        
    def measure_distance(self, other_point):
        self.x_difference = self.x - other_point.x
        self.y_difference = self.y - other_point.y
        return sqrt(pow(self.x_difference, 2) + pow(self.y_difference, 2))
    
    def measure_angle(self, other_point):
        self.x_difference = self.x - other_point.x
        self.y_difference = self.y - other_point.y
        return atan2(self.y_difference,self.x_difference)
    
class Ball():
    def __init__(self, coordinate, diameter, colour):
        self.coordinate = Point(coordinate.x, coordinate.y)
        self.x_velocity = 0
        self.y_velocity = 0
        self.diameter = diameter
        self.colour = colour
        self.still_in_play = 1
        
    def check_overlap(self, other_ball):
        self.overlap = self.diameter - self.coordinate.measure_distance(other_ball)
        return self.overlap

class wood_border():
    def __init__(self, coordinate, wide, high, colour):
        self.x = coordinate.x
        self.y = coordinate.y 
        self.wide = wide
        self.high = high
        self.colour = colour

class stick():
    def __init__(self, Length):
        self.start_point = Point(mouseX, mouseY)
        self.end_point = Point(0, 0)
        self.Length = Length
        self.colour = 0
def initializeballs():
    global diameter, ball_list
    cue_ball = Ball(Point(500, 543), diameter, 255)
    ball_1 = Ball(Point(1051, 543), diameter, '#FF0000')
    ball_2 = Ball(Point(1122, 502), diameter, '#00FF00')
    ball_3 = Ball(Point(1122, 584), diameter, '#0000FF')
    ball_4 = Ball(Point(1193, 543), diameter, 0)
    ball_5 = Ball(Point(1193, 625), diameter, '#FF00FF')
    ball_6 = Ball(Point(1193, 461), diameter, '#00FFFF')
    ball_7 = Ball(Point(1264, 666), diameter, '#FFFF00')
    ball_8 = Ball(Point(1264, 584), diameter, '#FF9600')
    ball_9 = Ball(Point(1264, 502), diameter, '#FF0096')
    ball_10 = Ball(Point(1264, 420), diameter, '#A260FA')
    
    ball_list = [cue_ball, ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, ball_7, ball_8, ball_9, ball_10]
    
def draw_stick(stick):
    global cue_ball
    stick.start_point.x = mouseX
    stick.start_point.y = mouseY
    angle = stick.start_point.measure_angle(ball_list[cue_ball_integer].coordinate)
    stick.end_point.x = stick.Length*cos(angle)
    stick.end_point.y = stick.Length*sin(angle)
    x_offset = abs(stick.Length*cos(angle))
    y_offset = abs(stick.Length*sin(angle))
    strokeWeight(30)
    stroke(cue_stick.colour, 0,0)
    strokeCap(SQUARE)
    if(stick.start_point.x <= ball_list[cue_ball_integer].coordinate.x and stick.start_point.y <= ball_list[cue_ball_integer].coordinate.y):
        line(stick.start_point.x - x_offset, stick.start_point.y - y_offset, stick.start_point.x - stick.end_point.x, stick.start_point.y - stick.end_point.y)
    if(stick.start_point.x <= ball_list[cue_ball_integer].coordinate.x and stick.start_point.y >= ball_list[cue_ball_integer].coordinate.y):
        line(stick.start_point.x - x_offset, stick.start_point.y + y_offset, stick.start_point.x - stick.end_point.x, stick.start_point.y - stick.end_point.y)
    if(stick.start_point.x >= ball_list[cue_ball_integer].coordinate.x and stick.start_point.y <= ball_list[cue_ball_integer].coordinate.y):
        line(stick.start_point.x + x_offset, stick.start_point.y - y_offset, stick.start_point.x - stick.end_point.x, stick.start_point.y - stick.end_point.y)
    if(stick.start_point.x >= ball_list[cue_ball_integer].coordinate.x and stick.start_point.y >= ball_list[cue_ball_integer].coordinate.y):
        line(stick.start_point.x + x_offset, stick.start_point.y + y_offset, stick.start_point.x - stick.end_point.x, stick.start_point.y - stick.end_point.y)
        
        
        
def draw_table():
    global cue_ball, game_over, game_win, ball_list, pocket_list, wood_border_list, cue_stick, win_counter
    strokeWeight(1)
    stroke(0)
    background('#006400')
    
    if (game_over == 1):
        game_over_screen()
        return
    if (game_win == 1):
        game_win_screen()
    
    i = 0
    while(i <= len(pocket_list)-1): ## This loop is to draw each pocket (black quarter-circles in each corner) by using the Ball object
        fill(pocket_list[i].colour)
        circle(pocket_list[i].coordinate.x, pocket_list[i].coordinate.y, pocket_list[i].diameter)
        i += 1
        
    i = 0
    while(i <= len(wood_border_list)-1): ## This loop is to draw the wooden borders around the screen by using the wooden_border object
        fill (wood_border_list[i].colour)
        rect(wood_border_list[i].x, wood_border_list[i].y, wood_border_list[i].wide, wood_border_list[i]. high)
        i += 1
    

    power_from_stick_to_cue_ball() ## This function continuously searches for user input to change the power_of_stick value. 
    draw_balls() ## This function draws the balls taking into account their initial positions and their velocities.
    draw_stick(cue_stick)## This function continuously draws the stick.
    collision_check()
    
def power_from_stick_to_cue_ball():
    global cue_ball_integer, power_of_stick
    mouse_point = Point(mouseX, mouseY)
    angle_between_cue_and_mouse = ball_list[cue_ball_integer].coordinate.measure_angle(mouse_point)
    
    if (mouseButton == LEFT and (ball_list[cue_ball_integer].coordinate.measure_distance(mouse_point) <= mouse_to_ball_max_range) and (ball_list[cue_ball_integer].x_velocity <= 1) and (ball_list[cue_ball_integer].y_velocity <= 1)):
        
        ball_list[cue_ball_integer].x_velocity = power_of_stick * cos(angle_between_cue_and_mouse)
        ball_list[cue_ball_integer].y_velocity = power_of_stick * sin(angle_between_cue_and_mouse)
        if (mouse_point.x == 0):
            ball_list[cue_ball_integer].x_velocity = 0
        if (mouse_point.y == 0):
            ball_list[cue_ball_integer].y_velocity = 0
        power_of_stick = 0
        cue_stick.colour = power_of_stick

    if (keyPressed and (key == ' ' and power_of_stick < max_power)):
        power_of_stick += 1
        cue_stick.colour = power_of_stick*5

    if (keyPressed and key == 'r'):
        power_of_stick = 0
        cue_stick.colour = power_of_stick

def draw_balls():
    global win_counter, game_over
    i = 0
    
    stroke(0)
    strokeWeight(1)
    
    while(i < len(ball_list)): ## This while loop works to displace the balls based on their velocities and will decrement the velocities to slow down as the balls move further. 
        if (ball_list[i].still_in_play == 1):
            ball_list[i].coordinate.x += ball_list[i].x_velocity
            ball_list[i].coordinate.y += ball_list[i].y_velocity
            fill(ball_list[i].colour)
            circle(ball_list[i].coordinate.x, ball_list[i].coordinate.y, ball_list[i].diameter)
            
            if (ball_list[i].x_velocity > 2 or ball_list[i].x_velocity < 2):
                ball_list[i].x_velocity /= 1.02
            else: 
                ball_list[i].x_velocity = 0
                
            if (ball_list[i].y_velocity > 2 or ball_list[i].y_velocity < 2):
                ball_list[i].y_velocity /= 1.02
            else: 
                ball_list[i].y_velocity = 0
        
            j = 0
            while (j < len(pocket_list)):  ## This while loop determines if a ball will fall into any of the four pockets. If so, the ball is moved off screen and the counter increases towards the win condition. 
                if (ball_list[i].coordinate.measure_distance(pocket_list[j].coordinate) < pocket_condition):
                    ball_list[i].coordinate.x = -2000
                    ball_list[i].coordinate.y = -2000
                    ball_list[i].x_velocity = 0
                    ball_list[i].y_velocity = 0
                    if (i == cue_ball_integer):
                        game_over = 1
                    if (i != cue_ball_integer):
                        win_counter += 1 
                        ball_list[i].still_in_play = 0
                j += 1
                    
            if (ball_list[i].coordinate.x > width - (ball_list[i].diameter/2 + border_width)):  ## These next few if statements work to determine each ball's collision with the wooden borders.
                ball_list[i].coordinate.x = width - (ball_list[i].diameter/2 + border_width)
                ball_list[i].x_velocity = -ball_list[i].x_velocity
            if (ball_list[i].coordinate.x < (ball_list[i].diameter/2 + border_width)):
                ball_list[i].coordinate.x = (ball_list[i].diameter/2 + border_width)
                ball_list[i].x_velocity = -ball_list[i].x_velocity
            if (ball_list[i].coordinate.y > height - (ball_list[i].diameter/2 + border_width)):
                ball_list[i].coordinate.y = height - (ball_list[i].diameter/2 + border_width)
                ball_list[i].y_velocity = -ball_list[i].y_velocity
            if (ball_list[i].coordinate.y < (ball_list[i].diameter/2 + border_width)):
                ball_list[i].coordinate.y = ball_list[i].diameter/2 + border_width
                ball_list[i].y_velocity = -ball_list[i].y_velocity            
        i += 1 

def game_over_screen():
    global game_over, win_counter
    background(0)
    fill(255)
    textSize(50)    
    text("Game Over", 830, 450)
    rect(760, 600, 400, 100)
    fill(0)
    textSize(30)
    text("Click here to play again", 795, 655)
    if(mouseButton == LEFT and (mouseX >= 760 and mouseX <= 1160) and (mouseY >= 600 and mouseY <= 700)):
        game_over = 0
        win_counter = 0
        initializeballs()


def game_win_screen(): 
    global game_win, win_counter
    background('#00FF00')
    fill(255)
    textSize(50)
    text("YOU WIN!!!", 850, 450)
    strokeWeight(1)
    rect(760, 600, 400, 100)
    fill(0)
    textSize(30)
    text("Click here to play again", 795, 655)
    if(mousePressed == LEFT and (mouseX >= 760 and mouseX <= 1160) and (mouseY >= 600 and mouseY <= 700)):
        game_win = 0
        win_counter = 0
        initializeballs()

def collision_check():
    i = 0
    while (i < (len(ball_list)-1)):
        j = i+1
        if (ball_list[i].still_in_play == 1):
            while (j < len(ball_list)):
    
                dx = ball_list[i].coordinate.x - ball_list[j].coordinate.x
                dy = ball_list[i].coordinate.y - ball_list[j].coordinate.y
                distance = sqrt(pow(dx, 2) + pow(dy, 2))
                    
                if (distance < (ball_list[i].diameter/2 + ball_list[j].diameter/2) and  distance != 0):
                    
                    normalX = dx / distance
                    normalY = dy / distance
                    
                    overlap = ball_list[i].check_overlap(ball_list[j].coordinate)/2
                                    
                    ball_list[i].coordinate.x += overlap * normalX 
                    ball_list[i].coordinate.y += overlap * normalY
                    ball_list[j].coordinate.x -= overlap * normalX
                    ball_list[j].coordinate.y -= overlap * normalY
                    
                    dVector = ((ball_list[i].x_velocity - ball_list[j].x_velocity) * normalX) + ((ball_list[i].y_velocity - ball_list[j].y_velocity)* normalY)
                    
                    dvx = dVector * normalX
                    dvy = dVector * normalY
                    
                    ball_list[i].x_velocity -= dvx
                    ball_list[i].y_velocity -= dvy
                    ball_list[j].x_velocity += dvx
                    ball_list[j].y_velocity += dvy
                j += 1
        i += 1

       
