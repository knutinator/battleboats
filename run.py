from random import randint

# Inspiration taken from:
# https://codereview.stackexchange.com/questions/232013/a-simple-battleship-game

# function to start a new game

class Gameboard:
    def __init__(self, name, size,):
        self.name = name
        self.size = size
        self.pl_game_board = None
        self.cpu_game_board = None
        self.x = None
        self.y = None
        self.cpu_board_inv = None
        self.player_score = 0
        self.cpu_score = 0
        self.game_over = 0
    
        
    # method to draw the board for the user and the computer    
    def make_board(self):
        """
        Draws gameboards based on size argument.
        Places a number of boats randomly, boat count is based on size arg.
        """
        print(f"{self.name} BOARD")

        # makes a board for player
        if self.name == "PLAYER":
            self.pl_game_board = [["."] * self.size for _ in range(self.size)]
            
        # makes a board + an invisible board for computer
        if self.name == "COMPUTER":
            self.cpu_game_board = [["."] * self.size for _ in range(self.size)]
            self.cpu_board_inv = [["."] * self.size for _ in range(self.size)]
        
        # generate random coordinate
        count = 0
        while count < self.size:
            self.x = randint(0, self.size-1)
            self.y = randint(0, self.size-1)
            # sometimes generates same number twice, add function to check,
            # maybe while game_board[x][y] == B: randomize again?
            count += 1 
            # puts boats on player board
            if self.name == "PLAYER":
                if self.pl_game_board[self.x][self.y] == ".":
                    self.pl_game_board[self.x][self.y] = "B"
            # puts invisible boats on cpu invisible board
            if self.name == "COMPUTER":
                if self.cpu_board_inv[self.x][self.y] == ".":
                    self.cpu_board_inv[self.x][self.y] = "B"    

        # makes game boards display without ""
        if self.name == "PLAYER":        
            for point in self.pl_game_board: 
                print(*point)

        if self.name == "COMPUTER":
            for point in self.cpu_game_board: 
                print(*point)
        print("\n")

        # TEMP, just to see hidden cpu board
        if self.name == "COMPUTER":
            print("invisible cpu board")
            for point in self.cpu_board_inv:
                print(*point)
            print("\n")
            

    # method to check if user input is valid    
    def check_valid(self, x_row, y_column):
        print("check_valid")    


    # redraw board
    def redraw_board(self, x_row, y_column, cpu_x_row, cpu_y_column):  
        print(f"{self.name} BOARD")
        if self.name == "COMPUTER": # Computer board (bottom)
            if not self.cpu_board_inv[x_row][y_column] == "B":
                self.cpu_game_board[x_row][y_column] = "o"
                for point in self.cpu_game_board:
                    print(*point)
                print("SPLASH! You missed...")    
                print(f"Your score: {self.player_score}")  
            else:
                self.cpu_game_board[x_row][y_column] = "#"                
                for point in self.cpu_game_board:
                    print(*point)
                self.player_score += 1  
                print("BOOM! You hit a boat!")
                print(f"Your score: {self.player_score}")
                            
        elif self.name == "PLAYER": # Player board (top)
            if not self.pl_game_board[cpu_x_row][cpu_y_column] == "B":
                self.pl_game_board[cpu_x_row][cpu_y_column] = "o"
                for point in self.pl_game_board:
                    print(*point)
                print("SPLASH! Computer missed!")
                print(f"CPU score: {self.cpu_score}")      
            else:
                self.pl_game_board[cpu_x_row][cpu_y_column] = "#"
                for point in self.pl_game_board:
                    print(*point)
                print("BOOM! Computer sank your boat...")
                self.cpu_score += 1
                print(f"CPU score: {self.cpu_score}")    
        
        if self.cpu_score == self.size:
            print("cpu wins")
            self.game_over = 1

        if self.player_score == self.size:
            print("player wins")
            self.game_over = 1    

        print("\n")  

    
    


# a turn counter function that tells how long the game has been played
# a while loop that keeps the game running until win or lose condition are met
# a function that shows which player won the game and asks for a rematch


# draws game boards
def new_game():
    print("\nB A T T L E B O A T S\n")
    player_board = Gameboard("PLAYER", 5)
    player_board.make_board()
    cpu_board = Gameboard("COMPUTER", 5)
    cpu_board.make_board()  
    game_over = 0

    # main game loop:
    while player_board.game_over or cpu_board.game_over == 0:
        # player turn
        # prompt the player for input  
        print("Guess where the computer's boats are!\n")
        row = int(input(f"Enter a row nr between 1 - {player_board.size}: "))
        column = int(input(f"Enter a column nr between 1 - {player_board.size}: "))
        # decreases the players input by 1, to get correct index (0-4)
        x_row = row - 1
        y_column = column - 1

        # check if the player's input is valid (and returns error message)
        player_board.check_valid(x_row, y_column)

        # draw the players input (and result) on the computer's game board
        # check if any player has won the game

        #cpu turn
        # make a random selection on the board
        count = 0
        while count < cpu_board.size:
            cpu_board.x = randint(0, cpu_board.size-1)
            cpu_board.y = randint(0, cpu_board.size-1)
            # sometimes generates same number twice, add function to check,
            # maybe while game_board[x][y] == B: randomize again?
            count += 1 

        cpu_x_row = cpu_board.x
        cpu_y_column = cpu_board.y
        # check if the cpu:s choice is a hit or miss
        # draw the cpu:s choice on the players game board
        # check if any player has won the game
        # increase the turn counter by one
        
        # player_board.redraw_board()
        player_board.redraw_board(x_row, y_column, cpu_x_row, cpu_y_column)
        cpu_board.redraw_board(x_row, y_column, cpu_x_row, cpu_y_column)

        if player_board.game_over or cpu_board.game_over == 1:
            break
        

new_game()
