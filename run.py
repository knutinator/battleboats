from random import randint

# Inspiration taken from:
# https://codereview.stackexchange.com/questions/232013/a-simple-battleship-game

# function to start a new game
print("\nB A T T L E B O A T S\n")


class Gameboard:
    def __init__(self, name, size,):
        self.name = name
        self.size = size
        self.game_board = None
        self.x = None
        self.y = None
        self.cpu_board_inv = None
        
    # method to draw the board for the user and the computer    
    def make_board(self):
        """
        Draws a gameboard based on size argument.
        Places a number of boats randomly, boat count is based on size arg.
        """
        print(self.name)

        # makes a board
        self.game_board = [["."] * self.size for _ in range(self.size)]
        
        # makes an invisible board for cpu
        if self.name == "COMPUTER":
            self.cpu_board_inv = [["o"] * self.size for _ in range(self.size)]
        
        # generate random number
        count = 0
        while count < self.size:
            self.x = randint(0, self.size-1)
            self.y = randint(0, self.size-1)
            # sometimes generates same number twice, add function to check,
            # maybe while game_board[x][y] == B: randomize again?
            count += 1 
            # puts boats on player board
            if self.name == "PLAYER":
                if self.game_board[self.x][self.y] == ".":
                    self.game_board[self.x][self.y] = "B"
            # puts invisible boats on cpu invisible board
            if self.name == "COMPUTER":
                if self.cpu_board_inv[self.x][self.y] == "o":
                    self.cpu_board_inv[self.x][self.y] = "B"    

        # makes game board display without ""        
        for point in self.game_board:
            print(*point)
        print("\n")
        
        # TEMP, just to see hidden cpu board
        if self.name == "COMPUTER":
            print(f"invisible: {self.cpu_board_inv}")

    # method to check if user input is valid    
    def check_valid(self, x_row, y_column):
        print("check_valid")    

    # method to check if user input is a hit
    def check_hit(self, x_row, y_column):
        print("check_hit")    

    # method to draw new symbols on the board
    def redraw_board(self):  
        print(None)      

# a turn counter function that tells how long the game has been played
# a while loop that keeps the game running until win or lose condition are met
# a function that shows which player won the game and asks for a rematch

# the main game loop
# NEEDS TO BE A WHILE LOOP, THAT RUNS UNTIL SOMEONE WINS

def run_game():
    # These must be outside loop: (put into populate_game function)
    player_board = Gameboard("PLAYER", 5)
    player_board.make_board()

    cpu_board = Gameboard("COMPUTER", 5)
    cpu_board.make_board()   
    
#player turn
    # prompt the player for input  
    print("Guess where the computer's boats are!\n")
    row = int(input(f"Enter a row number between 1 - {player_board.size}: "))
    column = int(input(f"Enter a column number between 1 - {player_board.size}: "))
    # decreases the players input by 1, to get correct index (0-4)
    x_row = row - 1
    y_column = column - 1

    # check if the player's input is valid (and returns error message)
    player_board.check_valid(x_row, y_column)

    # check whether the players input is a hit or miss (on computers board)
    cpu_board.check_hit(x_row, y_column)

    # draw the players input (and result) on the computer's game board
    # check if any player has won the game

#cpu turn
    # make a random selection on the board
    # check if the cpu:s choice is a hit or miss
    # draw the cpu:s choice on the players game board
    # check if any player has won the game
    # increase the turn counter by one


run_game()