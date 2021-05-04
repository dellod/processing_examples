# pong.pyde
# Pong game
# SCRP
# Daryl Dang

# CONSTANTS
game_modes = ("EASY", "MEDI", "HARD")
X_POS_LEFT_SIDE = 0
X_POS_RIGHT_SIDE = 775
PADDLE_RECT_SIZE = (25, 100)

# GLOBALS
# Screen size
s_width, s_height = 800, 500

# Game states
in_menu_screen = True
in_cpu_selection_screen = False
give_instructions = False
in_game = False
in_game_over = False
has_game_value_been_adjusted = False

# Game mode difficulty (selected by user)
game_mode_difficulty = game_modes[1] # Set to MEDIUM by default

# Paddles
user_paddle_y_pos = cpu_paddle_y_pos = s_height / 2 - PADDLE_RECT_SIZE[1] / 2 # STARTING POSITIONS
user_paddle_speed = 40 # DEFAULT
cpu_paddle_speed = 0 # DEFAULT

# Game ball
initial_x = 400
initial_y = 250
sq_x_pos = initial_x
sq_y_pos = initial_y
sq_side = 10
sq_x_speed = 0 # DEFAULT
sq_y_speed = 0 # DEFAULT

# Scores
user_score = 0
cpu_score = 0

def settings():
    size(s_width, s_height)
    
def draw():
    # Draw starting menu
    if not(starting_menu()):
        pass
    elif not(run_game()):
        pass
    
def starting_menu():
    # State globals being used.
    global in_menu_screen, in_cpu_selection_screen, in_game
    
    # Set return value of function.
    return_exit_value = False
    if in_game:
        # If true, means the game is ready to be started.
        # Make sure game difficulty has been adjusted (only one time).
        if not(has_game_value_been_adjusted):
            adjust_game_to_difficulty()
        
        # Return value.
        return_exit_value = True
        return return_exit_value
    
    # Default background
    background("#15B1CB")
    
    # Write game title to top of screen.
    welcome_message = "PONG"
    textSize(64)
    fill(0)
    stroke(0)
    text(welcome_message, s_width/2 - 90, 70)

    if not(in_cpu_selection_screen) and not(give_instructions):
        # Draw play button.
        fill(125)
        stroke(125)
        rect(300, 250, 200, 100)
        textSize(48)
        fill(0)
        stroke(0)
        text("PLAY", s_width/2 - 57, 315)
    elif in_cpu_selection_screen and not(give_instructions):
        # User has selected play and is now in CPU selection.
        cpu_selection_message = "Please select a difficulty of CPU to play against."
        textSize(16)
        fill(0)
        stroke(0)
        text(cpu_selection_message, s_width/2 - 175, 100)

        # Draw EASY button.
        fill(125)
        stroke(125)
        rect(300, 105, 200, 100)
        textSize(48)
        fill(0)
        stroke(0)
        text("EASY", s_width/2 - 57, 170)
        
        # Draw MEDIUM button.
        fill(125)
        stroke(125)
        rect(300, 210, 200, 100)
        textSize(48)
        fill(0)
        stroke(0)
        text("MEDI", s_width/2 - 57, 275)
        
        # Draw MEDIUM button.
        fill(125)
        stroke(125)
        rect(300, 315, 200, 100)
        textSize(48)
        fill(0)
        stroke(0)
        text("HARD", s_width/2 - 57, 380)
    else:
        # Give instructions.
        textSize(15)
        fill(0)
        stroke(0)
        instruction_message = "Use UP and DOWN arrow keys to control the left side box to go up and down. First to 5 wins the game. Press any key when ready to continue..."
        text(instruction_message, 210, 200, 400, 100)

    return return_exit_value

def adjust_game_to_difficulty():
    global has_game_value_been_adjusted, sq_x_speed, sq_y_speed
    has_game_value_been_adjusted = True
    
    # Randomize positive or negative direciton of game ball
    random_pos_or_neg = random(-1, 1)
    if random_pos_or_neg < 0:
        random_pos_or_neg = -1
    else:
        random_pos_or_neg = 1
    
    # Check if on EASY
    if game_mode_difficulty == game_modes[0]:
        sq_x_speed = -2
        sq_y_speed = random_pos_or_neg * 2
        
    # Check if on MEDI
    elif game_mode_difficulty == game_modes[1]:
        sq_x_speed = -4
        sq_y_speed = random_pos_or_neg * 3

    # Check if on HARD
    elif game_mode_difficulty == game_modes[2]:
        sq_x_speed = -6
        sq_y_speed = random_pos_or_neg * 4

def run_game():
    # Define globals
    global user_paddle_y_pos

    # Draw background
    background(0)
    
    # Draw field (line and scores)
    draw_field()
    
    # Draw user paddle
    draw_paddle_rect(True, user_paddle_y_pos)
    
    # Draw CPU paddle
    cpu_logic()
    draw_paddle_rect(False, cpu_paddle_y_pos)

    # Draw square (ball)    
    draw_square()
    
    # Return logic
    if not(in_game_over):
        # Not in game over state, return False to keep running this function.
        return False
    else:
        # In game over state, return True ot exit this function.
        return True

def cpu_logic():
    # TODO
    # Define globals
    global cpu_paddle_y_pos, cpu_paddle_speed
    
    # Check if on EASY
    if game_mode_difficulty == game_modes[0]:
        cpu_paddle_speed = 20

    # Check if on MEDI
    elif game_mode_difficulty == game_modes[1]:
        cpu_paddle_speed = 40

    # Check if on HARD
    elif game_mode_difficulty == game_modes[2]:
        cpu_paddle_speed = 50

    # Update CPU paddle
    # # Check if about to hit the bottom of screen
    # if (cpu_paddle_y_pos + PADDLE_RECT_SIZE[1]) >= s_height:
    #     cpu_paddle_y_pos += 0
    # elif cpu_paddle_y_pos <= 0:
    #     cpu_paddle_y_pos += 0
    # else:
    #     cpu_paddle_y_pos += cpu_paddle_speed

def draw_square():
    # Define globals
    global sq_x_pos, sq_y_pos, sq_x_speed, sq_y_speed, cpu_score, user_score

    # Draw square
    fill(255)
    fill(255)
    square(sq_x_pos, sq_y_pos, sq_side)
    
    # Update position of square
    sq_x_pos += sq_x_speed
    sq_y_pos += sq_y_speed

    # Check if hitting top or bottom
    if (sq_y_pos + sq_side) >= s_height or sq_y_pos <= 0:
        sq_y_speed *= -1
    
    # Check if hitting user paddle
    if sq_x_pos <= (X_POS_LEFT_SIDE + PADDLE_RECT_SIZE[0]):
        if sq_y_pos >= user_paddle_y_pos and (sq_y_pos + sq_side) <= (user_paddle_y_pos + PADDLE_RECT_SIZE[1]):
            sq_x_speed *= -1
    
    # Check if hitting CPU paddle
    if (sq_x_pos + sq_side) >= X_POS_RIGHT_SIDE:
        if sq_y_pos >= cpu_paddle_y_pos and (sq_y_pos + sq_side) <= (cpu_paddle_y_pos + PADDLE_RECT_SIZE[1]):
            sq_x_speed *= -1

    # Check if pass user side
    if sq_x_pos < 0:
        # Update CPU score
        cpu_score += 1
        
        # Reset square
        sq_x_pos, sq_y_pos = initial_x, initial_y
    
    # Check if pass CPU side
    if (sq_x_pos + sq_side) > s_width:
        # Update user score
        user_score += 1
        
        # Reset square
        sq_x_pos, sq_y_pos = initial_x, initial_y

def draw_field():    
    # Colour of center line
    fill(255)
    stroke(255)
    
    # Draw center line
    center_line_width = 2
    center_line_height = s_height
    center_line_x = s_width / 2 - center_line_width / 2
    center_line_y = 0

    rect(center_line_x, center_line_y, center_line_width, center_line_height)
    
    # Draw scores
    score_y_pos = 50
    user_x_pos = 350
    cpu_x_pos = 410

    textSize(64)
    fill(255)
    stroke(0)
    _user_score = str(user_score)
    text(_user_score, user_x_pos, score_y_pos)
    _cpu_score = str(cpu_score)
    text(_cpu_score, cpu_x_pos, score_y_pos)

def draw_paddle_rect(is_user, y_pos):
    # Colour of paddles
    fill(255)
    stroke(0)

    # If it is a user, we draw on the box on the left side.
    if is_user:
        rect(X_POS_LEFT_SIDE, y_pos, PADDLE_RECT_SIZE[0], PADDLE_RECT_SIZE[1])
    # Else, we draw the CPU paddle
    else:
        rect(X_POS_RIGHT_SIDE, y_pos, PADDLE_RECT_SIZE[0], PADDLE_RECT_SIZE[1])        

def mouseClicked():
    # Define globals that are going to be used.
    global in_cpu_selection_screen, game_mode_difficulty, give_instructions
    
    if in_menu_screen:
        if not(in_cpu_selection_screen):
            # Check if user has clicked the PLAY button.
            if (mouseX >= 300 and mouseX <= 500) and (mouseY >= 250 and mouseY <= 350):
                in_cpu_selection_screen = True
        else:
            # Check if user has clicked the EASY button.
            if (mouseX >= 300 and mouseX <= 500) and (mouseY >= 105 and mouseY <= 205):
                game_mode_difficulty = game_modes[0]
                give_instructions = True
            # Check if user has clicked the MEDI button.
            elif (mouseX >= 300 and mouseX <= 500) and (mouseY >= 210 and mouseY <= 310):
                game_mode_difficulty = game_modes[1]
                give_instructions = True
            # Check if user has clicked the HARD button.
            elif (mouseX >= 300 and mouseX <= 500) and (mouseY >= 315 and mouseY <= 415):
                game_mode_difficulty = game_modes[2]
                give_instructions = True
                
def keyPressed():
    global in_menu_screen, give_instructions, in_game
    if in_menu_screen and give_instructions:
        in_menu_screen = give_instructions = False
        in_game = True
    elif in_game and not(in_game_over):
        # Define globals
        global user_paddle_y_pos
        if keyCode == UP:
            # Move user paddle up
            temp = user_paddle_y_pos - user_paddle_speed
            if temp >= 0:
                user_paddle_y_pos -= user_paddle_speed
        elif keyCode == DOWN:
            # Move user paddle down
            temp = (user_paddle_y_pos + PADDLE_RECT_SIZE[1]) + user_paddle_speed
            if temp <= s_height:
                user_paddle_y_pos += user_paddle_speed
