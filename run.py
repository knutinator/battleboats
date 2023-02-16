from random import randint

# Inspiration taken from:
# https://codereview.stackexchange.com/questions/232013/a-simple-battleship-game


class Gameboard:
    """
    Class containing methods for drawing and updating game boards.
    Contains main game logic.
    """
    def __init__(self, name, size,):
        self.name = name
        self.size = size
        self.pl_game_board = []
        self.cpu_game_board = []
        self.x = None
        self.y = None
        self.cpu_board_inv = None
        self.player_score = 0
        self.cpu_score = 0
        self.game_over = 0

    def make_board(self):
        """
        Method to draw gameboards based on size argument.
        Places a number of boats randomly, boat count is based on size arg.
        """
        print(f"{self.name} BOARD")

        # Makes a board for player
        if self.name == "PLAYER":
            self.pl_game_board = [["."] * self.size for _ in range(self.size)]

        # Makes a board + an invisible board for computer
        if self.name == "COMPUTER":
            self.cpu_game_board = [["."] * self.size for _ in range(self.size)]
            self.cpu_board_inv = [["."] * self.size for _ in range(self.size)]

        # Generate random coordinates for boats
        boat_count = 0
        while boat_count < self.size:
            self.x = randint(0, self.size-1)
            self.y = randint(0, self.size-1)

            # Puts boats on player board
            if self.name == "PLAYER":
                if self.pl_game_board[self.x][self.y] == ".":
                    self.pl_game_board[self.x][self.y] = "B"
                    boat_count += 1

            # Puts invisible boats on cpu invisible board
            if self.name == "COMPUTER":
                if self.cpu_board_inv[self.x][self.y] == ".":
                    self.cpu_board_inv[self.x][self.y] = "B"
                    boat_count += 1

        # Makes game boards display without ""
        if self.name == "PLAYER":
            for point in self.pl_game_board:
                print(*point)

        if self.name == "COMPUTER":
            for point in self.cpu_game_board:
                print(*point)

        # Whitespace below boards
        print("\n")

    def redraw_board(self, x_row, y_column, cpu_x_row, cpu_y_column):
        """
        Method to redraw game boards to show latest moves.
        Also calculates hits/misses and game winners.
        """
        print(f"{self.name} BOARD")

        # Player board (top)
        if self.name == "PLAYER":
            # Checks for computer misses
            if not self.pl_game_board[cpu_x_row][cpu_y_column] == "B":
                self.pl_game_board[cpu_x_row][cpu_y_column] = "o"
                for point in self.pl_game_board:
                    print(*point)
                print("SPLASH! Computer missed!")
                print(f"CPU score: {self.cpu_score}")

            else:
                # Checks for computer hits
                self.pl_game_board[cpu_x_row][cpu_y_column] = "#"
                for point in self.pl_game_board:
                    print(*point)
                print("BOOM! Computer sank your boat...")
                self.cpu_score += 1
                print(f"CPU score: {self.cpu_score}")

        # Computer board (bottom)
        elif self.name == "COMPUTER":
            # Checks for player misses
            if not self.cpu_board_inv[x_row][y_column] == "B":
                self.cpu_game_board[x_row][y_column] = "o"
                for point in self.cpu_game_board:
                    print(*point)
                print("SPLASH! You missed...")
                print(f"Your score: {self.player_score}")

            # Checks if player already hit a boat at selected point
            elif self.cpu_game_board[x_row][y_column] == "#":
                for point in self.cpu_game_board:
                    print(*point)
                print("You already sank that ship!")
                print(f"Your score: {self.player_score}")

            else:
                # Checks for player hits
                self.cpu_game_board[x_row][y_column] = "#"
                for point in self.cpu_game_board:
                    print(*point)
                self.player_score += 1
                print("BOOM! You hit a boat!")
                print(f"Your score: {self.player_score}")

        # Checks if any player has won the game
        if self.cpu_score == self.size:
            print("\nComputer wins!\n")
            self.game_over = 1

        if self.player_score == self.size:
            print("\nPlayer wins!\n")
            self.game_over = 1

        print("\n")  # Whitespace below text


def new_game():
    """
    Function for starting and playing the game.
    Contains calls to draw the game boards
    and a loop that keeps the game running.
    """
    # The number arg below controls the board size and the number of boats
    player_board = Gameboard("PLAYER", 5)
    cpu_board = Gameboard("COMPUTER", 5)

    # Draws title screen and instructions for gameplay
    print("\nB A T T L E B O A T S\n")
    print(f"Each player has {player_board.size} hidden boats, (B).")
    print("Find them all to win!\n")
    input("\nPress ENTER to start game.\n")

    # Draws the game boards
    player_board.make_board()
    cpu_board.make_board()
    cpu_guesses = []

    # Main game loop:
    while player_board.game_over or cpu_board.game_over == 0:

        # player turn: prompts the player for input, checks for validity
        while True:
            try:
                print("Guess where the computer's boats are!\n")
                row = int(input(
                    f"Enter a row nr between 1 - {player_board.size}: "))
                column = int(input(
                    f"Enter a col nr between 1 - {player_board.size}: "))

                # Checks that input is an integer
            except ValueError:
                print(f"""
                Only enter numbers between 1 - {player_board.size}.\n""")
                continue

                # Checks that selected row is within board
            if row not in range(0, player_board.size+1):
                print(f"""
                Only enter numbers between 1 - {player_board.size}.\n""")
                continue

                # Checks that selected column is within board
            if column not in range(0, player_board.size+1):
                print(f"""
                Only enter numbers between 1 - {player_board.size}.\n""")
                continue

            else:
                break

        # Decreases the players input by 1 to get correct index (0-4)
        x_row = row - 1
        y_column = column - 1

        # Cpu turn: makes a random selection on the board,
        # checks if already selected
        count = 0
        while count < 1:
            cpu_board.x = randint(0, cpu_board.size-1)
            cpu_board.y = randint(0, cpu_board.size-1)

            # Converts both ints to strings, adds them,
            # converts back to ints to get a 2-digit int
            cpu_point = int(str(cpu_board.x) + str(cpu_board.y))

            # Checks if 2-digit int is already in list, adds to list if not
            if cpu_point in cpu_guesses:
                continue
            else:
                cpu_guesses.append(cpu_point)
            count += 1

        # Stores the computers selection in variables
        cpu_x_row = cpu_board.x
        cpu_y_column = cpu_board.y

        # Redraws the game boards
        print("\n")  # Spacing above game boards
        player_board.redraw_board(x_row, y_column, cpu_x_row, cpu_y_column)
        cpu_board.redraw_board(x_row, y_column, cpu_x_row, cpu_y_column)

        # Checks if any player has won the game
        if player_board.game_over or cpu_board.game_over == 1:
            break  # Stops the main game loop

    input("\nPress ENTER to restart game.\n")
    new_game()


# Runs the whole game
new_game()
