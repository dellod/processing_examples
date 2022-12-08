## Simon Ly
## Snake Game
## DIRECTIONS: 

## Setting up some values for the screen size/borders 
x_size = 700
x_max = x_size
x_min = 0
y_size = 700
y_max = y_size
y_min = 0

## Setting up some values for the snake head
square_size = 50
head_x_coord = x_size/2 - square_size
head_y_coord = y_size/2 - square_size
head_x_speed = 0
head_y_speed = 0
increment_amount = square_size

## Setting up the random variables for the random square the snake will be eating
food_x_coord = int(random(0,x_size/square_size))*square_size
food_y_coord = int(random(0,y_size/square_size))*square_size
delay_time = 500 ## Delay of 500 ms (half a second)
lose_check = 0
win_check = 0
win_counter = 1

class body():
    def __init__(self, x_coord, y_coord, x_speed, y_speed):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_speed = x_speed
        self.y_speed = y_speed
    
def setup():
    global snake_body
    background(0)
    size(x_size, y_size)
    head = body(head_x_coord, head_y_coord, head_x_speed, head_y_speed)
    snake_body = [head]
    
def keyPressed():
    global snake_body, lose_check
    if (key == 'w' and snake_body[0].y_speed !=1):
        snake_body[0].x_speed = 0
        snake_body[0].y_speed = -1
    if (key == 's' and snake_body[0].y_speed !=-1):
        snake_body[0].x_speed = 0
        snake_body[0].y_speed = 1
    if (key == 'd' and snake_body[0].x_speed !=-1):
        snake_body[0].x_speed = 1
        snake_body[0].y_speed = 0
    if (key == 'a' and snake_body[0].x_speed !=1):
        snake_body[0].x_speed = -1
        snake_body[0].y_speed = 0
        
def draw():
    global snake_body, food_x_coord, food_y_coord, lose_check, win_check
    if lose_check == 1 or win_check == 1:
        return
    
    if win_counter == x_size * y_size / square_size^2:
        win_screen()
        return
    
    background(0)
    if (snake_body[0].x_coord == x_max or snake_body[0].x_coord < x_min or snake_body[0].y_coord == y_max or snake_body[0].y_coord < y_min):
        lose_screen()
        return   
    delay(delay_time)
    
    ## Drawing the food square 
    fill(255,0,0)
    square(food_x_coord, food_y_coord, square_size)
   
     ## If statement to check if food has been eaten
    if (snake_body[0].x_coord == food_x_coord and snake_body[0].y_coord == food_y_coord):
        food_consumed()
        
   
    ## While loop to draw other parts of snake's body after consuming food    
    i = len(snake_body)
    fill(0,255,0)
    while i > 1:
        snake_body[i-1].x_coord = snake_body[i-2].x_coord
        snake_body[i-1].y_coord = snake_body[i-2].y_coord
        square(snake_body[i-1].x_coord, snake_body[i-1].y_coord, square_size)
        i -= 1
   
    ## Incrementing and drawing the snake head
    snake_body[0].x_coord = snake_body[0].x_coord + snake_body[0].x_speed*increment_amount
    snake_body[0].y_coord = snake_body[0].y_coord + snake_body[0].y_speed*increment_amount
    square(snake_body[0].x_coord, snake_body[0].y_coord, square_size)
    
    ## Checking for self collision
    j = len(snake_body)
    while j-1 > 0:
        if (snake_body[j-1].x_coord == snake_body[0].x_coord and snake_body[j-1].y_coord == snake_body[0].y_coord):
            lose_screen()
            return
        j -= 1 

def food_consumed():
    global food_x_coord, food_y_coord, snake_body, win_counter
    win_counter += 1
    new_square = body(food_x_coord, food_y_coord, snake_body[0].x_speed, snake_body[0].y_speed)
    snake_body.append(new_square)
    food_x_coord = int(random(0,x_size/square_size))*square_size
    food_y_coord = int(random(0,y_size/square_size))*square_size
    k = len(snake_body) - 1
    while k > 0:
        if food_x_coord == snake_body[k].x_coord and food_y_coord == snake_body[k].y_coord:
            food_x_coord = int(random(0,x_size/square_size))*square_size
            food_y_coord = int(random(0,y_size/square_size))*square_size
            k = len(snake_body) -1
        k -= 1
        
def lose_screen():
    global lose_check
    fill(255)
    textSize(50)
    text('Game Over', x_size/2 - 130, y_size/2)
    lose_check = 1
    
def win_screen():
    global win_check
    fill(0,255,0)
    textSize(50)
    text('You Win!', x_size/2 - 125, y_size/2)
    win_check = 1
