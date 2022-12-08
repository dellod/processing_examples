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
did_user_win = False

def settings():
    size(s_width, s_height)
    
def draw():
    # Draw starting menu
    if not(starting_menu()):
        pass
    elif not(run_game()):
        pass
    elif in_game_over:
        # End game with results
        background("#15B1CB")
        textSize(64)
        fill(0)
        stroke(0)
        if did_user_win:
            end_game_message = "YOU WON"
        else:
            end_game_message = "YOU LOSE"
        
        text(end_game_message, s_width/2 - 150, 70)

def starting_menu():
    """
    Draw the menu that is displayed to players upon starting game.
    """
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
    else:
        # Give instructions.
        textSize(15)
        fill(0)
        stroke(0)
        instruction_message = "Use UP and DOWN arrow keys to control the left side box to go up and down. First to 5 wins the game. Press any key when ready to continue..."
        text(instruction_message, 210, 200, 400, 100)

    return return_exit_value

def adjust_game_to_difficulty():
    """
    Make initial adjustments to the initial settings of the game.
    """
    global has_game_value_been_adjusted, sq_x_speed, sq_y_speed
    has_game_value_been_adjusted = True
    
    # Randomize positive or negative direciton of game ball
    random_pos_or_neg = random(-1, 1)
    if random_pos_or_neg < 0:
        random_pos_or_neg = -1
    else:
        random_pos_or_neg = 1

    # Set ball speed
    sq_x_speed = -4
    sq_y_speed = random_pos_or_neg * 3

def run_game():
    """
    Run the main game logic.
    """
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

    # Draw square (ball)    
    draw_square()
    
    # Check score
    check_score()

    # Return logic
    if not(in_game_over):
        # Not in game over state, return False to keep running this function.
        return False
    else:
        # In game over state, return True ot exit this function.
        return True

def check_score():
    """
    Check the score for both user and CPU. Which ever equals 5 first, global variables will be adjusted to
    display final results.
    """
    global user_score, cpu_score, in_game_over, did_user_win
    if user_score == 5:
        in_game_over = True
        did_user_win = True
    elif cpu_score == 5:
        in_game_over = True
        did_user_win = False

def cpu_logic():
    """
    Define and draw CPU paddle patterns based on predefined logic.
    """
    # Define globals
    global cpu_paddle_y_pos, cpu_paddle_speed
    
    # Set CPU paddle speed
    cpu_paddle_speed = 2

    # Update CPU paddle
    if cpu_paddle_y_pos < sq_y_pos:
        cpu_paddle_y_pos += cpu_paddle_speed
    elif cpu_paddle_y_pos > sq_y_pos:
        cpu_paddle_y_pos -= cpu_paddle_speed
    else:
        pass

    # Draw CPU paddle
    draw_paddle_rect(False, cpu_paddle_y_pos)

def draw_square():
    """
    Draw the game ball (sqaure). Also, checks if hitting paddles or bot/top of screen and adjusts accordingly.
    """
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
    """
    Draw main field.
    """
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
    """
    Draw paddle.
    """
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
    """
    Processing function, gets called when mouse is pressed and released.
    """
    # Define globals that are going to be used.
    global in_cpu_selection_screen, give_instructions
    
    if in_menu_screen:
        if not(in_cpu_selection_screen):
            # Check if user has clicked the PLAY button.
            if (mouseX >= 300 and mouseX <= 500) and (mouseY >= 250 and mouseY <= 350):
                give_instructions = True
                
def keyPressed():
    """
    Processing fucntion, gets called when any key is pressed.
    """
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
