from random import randint

# Inspiration taken from:
# https://codereview.stackexchange.com/questions/232013/a-simple-battleship-game

# function to start a new game
print("\nB A T T L E B O A T S\n")

# a function that draws the board for the user and the computer
class Gameboard:
    def __init__(self, name, size,):
        self.name = name
        self.size = size
        

    def make_board(self):
        """
        Draws a gameboard based on size argument.
        Places a number of boats randomly, boat count is based on size arg.
        """
        print(self.name)
        game_board = [["."] * self.size for _ in range(self.size)]
        count = 0
        
        while count < self.size:
            x = randint(0, self.size-1)
            y = randint(0, self.size-1)
            # sometimes generates same number twice, add function to check,
            # maybe while game_board[x][y] == B: randomize again?
            # print(f"x, y {x, y}")
            count += 1 
            if game_board[x][y] == ".":
                game_board[x][y] = "B"

        for point in game_board:
            print(*point)
        print("\n")


    def check_valid(self):    


    def check_hit(self):   


    def redraw_board(self):    


# Function that hides the CPU boats, but keeps them in memory


# a function that randomly places boats for each player
    # select a random column and a random row in the board
    # generate a boat
    # item x in list y in player_board list
    # loop 5 times


# a turn counter function that tells how long the game has been played
# a while loop that keeps the game running until win or lose condition are met
# a function that shows which player won the game and asks for a rematch

# the main game loop, which includes:
 
def run_game():
    player_board = Gameboard("PLAYER", 5)
    player_board.make_board()

    cpu_board = Gameboard("COMPUTER", 5)
    cpu_board.make_board()   

#player turn
    # prompt the player for input  
    print("Guess where the computer's boats are!")
    row = int(input(f"Enter a row number between 1 - {player_board.size}: "))
    column = int(input(f"Enter a column number between 1 - {player_board.size}: "))
    # decreases the players input by 1, to get correct index (0-4)
    x_row = row - 1
    y_column = column - 1

    # check if the player's input is valid (and returns error message)
    player_board.check_valid()

    # check whether the players input is a hit or miss
    player_board.check_hit()

    # draw the players input (and result) on the computer's game board
    # check if any player has won the game

#cpu turn
    # make a random selection on the board
    # check if the cpu:s choice is a hit or miss
    # draw the cpu:s choice on the players game board
    # check if any player has won the game
    # increase the turn counter by one

run_game()