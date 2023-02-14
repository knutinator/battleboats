# sketch of Battleboats program

# function to start a new game

# a function that draws the board for the user and the computer

class Gameboard:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def make_board(self):
        game_board = [["."] * self.size for _ in range(self.size)]
        for point in game_board:
            print(*point)


player_board = Gameboard("Player", 5)
player_board.make_board()



# a function that randomly places boats for each player
# a turn counter function that tells how long the game has been played
# a while loop that keeps the game running until win or lose condition are met
# a function that shows which player won the game and asks for a rematch

# the main game loop, which includes:
 
    
#player turn
# prompt the player for input         
# check if the player's input is valid (and returns error message)
# check whether the players input is a hit or miss
# draw the players input (and result) on the computer's game board
# check if any player has won the game

#cpu turn
# make a random selection on the board
# check if the cpu:s choice is a hit or miss
# draw the cpu:s choice on the players game board
# check if any player has won the game
# increase the turn counter by one