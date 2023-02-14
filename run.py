from random import randint
# sketch of Battleboats program

# Inspiration taken from:
# https://codereview.stackexchange.com/questions/232013/a-simple-battleship-game

# function to start a new game

# a function that draws the board for the user and the computer
class Gameboard:
    def __init__(self, name, size,):
        self.name = name
        self.size = size
        

    def make_board(self):
        print(self.name)
        game_board = [["."] * self.size for _ in range(self.size)]
        for point in game_board:
            print(*point)
        print("\n")

    def make_boats(self):
        x = randint(0, self.size)
        y = randint(0, self.size)
        print(x, y)


player_board = Gameboard("PLAYER", 5)
player_board.make_board()
player_board.make_boats()

cpu_board = Gameboard("CPU", 5)
cpu_board.make_board()


# a function that randomly places boats for each player
    # select a random column and a random row in the board

    # generate a boat
    # item x in list y in player_board list
    




    # loop 5 times


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