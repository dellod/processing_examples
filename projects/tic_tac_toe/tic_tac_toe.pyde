# TicTacToe,pyde
# Play a game of Tic Tac Toe
# Andrew Truong

def setup():
    size(900,900) #900x900 grid to allow for easy division for grid
    background(255)
    textSize(200)
    textAlign(CENTER, CENTER)
    line(300,0,300,900)
    line(600,0,600,900)
    line(0,300,900,300)
    line(0,600,900,600)


#Function to draw the X symbol at proper coordinates
def draw_X(x_coord,y_coord):
    text("X",x_coord,y_coord)
    
#Function to draw the Y symbol at proper coordinates    
def draw_O(x_coord,y_coord):
    text("O",x_coord,y_coord)

#Function to get x and y coordinates once user presses the mouse
def get_player_input(counter):
    mouseX_coord = 1000
    mouseY_coord = 1000
    turn = False
    
    if mousePressed:
        mouseX_coord = mouseX
        mouseY_coord = mouseY
        turn = True
    return mouseX_coord, mouseY_coord, turn 

#Function to place X or O on proper portion of the grid
def place_XO(mouseX_coord, mouseY_coord, counter,list_coords):
    #Check if mouse X coordinate is in the first column
    if 0 <= mouseX_coord <= 300:
        #Check if mouse Y coordinate is in the first row
        if 0 <= mouseY_coord <= 300:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board[0][0] == "":
                draw_O(150,150)
                list_coords = 0,0
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter
            elif counter % 2 != 0 and board [0][0] == "":
                draw_X(150,150)
                list_coords = 0,0
                counter += 1
        #Check if mouse Y coordinate is in the second row
        elif 300 < mouseY_coord <= 600:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board[0][1] == "":
                draw_O(150,450)
                list_coords = 0,1
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter
            elif counter % 2 != 0 and board[0][1] == "":
                draw_X(150,450)
                list_coords = 0,1
                counter += 1
        #Check if mouse Y coordinate is in the second row
        elif 600 < mouseY_coord <= 900:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board[0][2] == "":
                draw_O(150,750)
                list_coords = 0,2
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter
            elif counter % 2 != 0 and board[0][2] == "":
                draw_X(150,750)
                list_coords = 0,2
                counter += 1
    #Check if mouse X coordinate is in the second column
    elif 300 < mouseX_coord <= 600:
        #Check if mouse Y coordinate is in the first row
        if 0 <= mouseY_coord <= 300:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board[1][0] == "":
                draw_O(450,150)
                list_coords = 1,0
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter
            elif counter % 2 != 0 and board[1][0] == "":
                draw_X(450,150)
                list_coords = 1,0
                counter += 1
        #Check if mouse Y coordinate is in the second row
        elif 300 < mouseY_coord <= 600:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board[1][1] == "":
                draw_O(450,450)
                list_coords = 1,1
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter
            elif counter % 2 != 0 and board[1][1] == "":
                draw_X(450,450)
                list_coords = 1,1
                counter += 1
        #Check if mouse Y coordinate is in the second row
        elif 600 < mouseY_coord <= 900:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board [1][2]== "":
                draw_O(450,750)
                list_coords = 1,2
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter
            elif counter % 2 != 0 and board[1][2] == "":
                draw_X(450,750)
                list_coords = 1,2
                counter += 1
    #Check if mouse X coordinate is in the third column
    elif 600 < mouseX_coord <= 900:
        #Check if mouse Y coordinate is in the first row
        if 0 <= mouseY_coord <= 300:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board[2][0] == "":
                draw_O(750,150)
                list_coords = 2,0
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter    
            elif counter % 2 != 0 and board[2][0] == "":
                draw_X(750,150)
                list_coords = 2,0
                counter += 1
        #Check if mouse Y coordinate is in the second row
        elif 300 < mouseY_coord <= 600:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board[2][1] == "":
                draw_O(750,450)
                list_coords = 2,1
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter 
            elif counter % 2 != 0 and board[2][1] == "":
                draw_X(750,450)
                list_coords = 2,1
                counter += 1
        #Check if mouse Y coordinate is in the third row
        elif 600 < mouseY_coord <= 900:
            #If counter is even and index in board list is empty then draw O and update counter
            if counter % 2 == 0 and board[2][2] == "":
                draw_O(750,750)
                list_coords = 2,2
                counter += 1
            #If counter is odd and index in board list is empty then draw X and update counter
            elif counter % 2 != 0 and board[2][2] == "":
                draw_X(750,750)
                list_coords = 2,2
                counter += 1

    return list_coords,counter

#Using list_coords tuple to append X or O into Board List depending on turn
def add_XO_to_list(list_coords,board):
    i, j = list_coords
    
    if counter % 2 != 0:
        board[i][j] = "O"
    elif counter % 2 == 0:
        board[i][j] = "X"

    return board

#Check if requirements suffice for a win
def check_win(board):
    for i in range(3):
        #Check if three in a row vertically
        if board[i][0] != "":
            if board[i][0] == board[i][1] == board[i][2]:
                return True
        #Check if three in a horizontally
        if board[0][i] != "":
            if board[0][i] == board[1][i] == board[2][i]:
                return True
    #check if three in a row diagonally
    if board[0][0] != "":
        if board[0][0] == board[1][1] == board[2][2]:
            return True
    #check if three in a row diagonally
    if board[0][2] != "":
        if board[2][0] == board[1][1] == board[0][2]:
            return True
    return False
#Checks if no win has been settled and board list is full
def check_tie(board,win):
    draw_count = 0
    #if it is no true that someone has won
    if not win:
        #Check if all positions in board list are non null
        for i in range(3):
            for j in range(3):
                if board[i][j] != "":
                    draw_count += 1
    #If all 9 elements in the list are filled then the game is a tie
    if draw_count == 9:
        return True
    
    return False

counter = 1 # Will allow program to keep track of whose turn it is
board = [] #Initialize board list
win = False #Initialize that the board is not in a winning state
tie = False #Initialize that the board is not in a tie state
list_coords = 0,0 #Tuple data type to keep track of the coordinates of the mousepress

#Makes board list a 2D array that is size 3x3 to match board size
for i in range(3):
    board += [["","",""]]

cont = False #Checker variable to allow draw function to wait for an input

def draw():
    global counter, board,win,tie,list_coords,cont
    #Loop will wait for input before breaking out of loop
    while not cont:
        #if statement to continue if board is not in a tie or winning state
        if not win:
            
            mouseX_coord,mouseY_coord,clicked = get_player_input(counter)
            list_coords, counter = place_XO(mouseX_coord, mouseY_coord,counter, list_coords)
            #If player has done a mouseclick
            if clicked:
                #appends list coordinates to list
                board = add_XO_to_list(list_coords,board)
            
            #Create indicator in top right to show whose turn it is
            fill("#FF9512")
            square(850,0,50)
            fill(0)
            #Displays X if it is X's turn
            if counter % 2 != 0:
                textSize(20)
                text("X",875,25)
                textSize(100)
            #Displays O if it is O's turn
            if counter % 2 == 0: 
                textSize(20)
                text("O",875,25)
                textSize(100)
            #check if board state has a win
            win = check_win(board)
            #check if board state has a tie
            tie = check_tie(board,win)
        
    
        #Proceeds if board has a winning state    
        if win:
            #If O is in the counter then print text to display they won
            if counter % 2 != 0:
                fill("#FF1A1A")
                textSize(50)
                text("O won!",450,450)
                text("Press any Key to Play Again",450,350)
                textSize(150)
                fill(0)
            #If X is in the counter then print text to display they won
            else:
                fill("#FF1A1A")
                textSize(50)
                text("X won!",450,450)
                text("Press any Key to Play Again",450,350)
                textSize(150)
                fill(0)
            #If user presses a key then state of the game will reset
            if keyPressed:
                counter = 1
                board = []
                win = False
                tie = False
                list_coords = 0,0
                for i in range(3):
                    board += [["","",""]]
                clear()
                setup()
       #Proceeds if board is in a tie state 
        if tie:
            #Displays to grid that the game is a tie
            fill("#FF1A1A")
            textSize(50)
            text("It's a Tie!",450,450)
            text("Press any Key to Play Again",450,350)
            textSize(150)
            fill(0)
            #If user presses a key then state of the game will reset
            if keyPressed:
                counter = 1
                board = []
                win = False
                tie = False
                list_coords = 0,0
                for i in range(3):
                    board += [["","",""]]
                clear()
                setup()
            
        cont = True
    cont = False
