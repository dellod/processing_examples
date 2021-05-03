# pong.pyde
# Pong game
# SCRP
# Daryl Dang

# CONSTANTS
game_modes = ("EASY", "MEDI", "HARD")

# GLOBALS
s_width, s_height = 800, 500
in_menu_screen = True
in_cpu_selection_screen = False
give_instructions = False
in_game = False
game_mode_difficulty = game_modes[1] # Set to MEDIUM by default

def settings():
    size(s_width, s_height)
    
def draw():
    # Draw starting menu
    if not(starting_menu()):
        #print("here")
        pass
    elif not(start_game()):
        pass
    
def starting_menu():
    # State globals being used.
    global in_menu_screen, in_cpu_selection_screen, in_game
    
    # Set return value of function.
    return_exit_value = False
    if in_game:
        # If true, means the game is ready to be started.
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

def start_game():
    # TODO
    background(0)
    return False

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
        


    
