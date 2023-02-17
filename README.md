
# BATTLEBOATS

Battleboats is a terminal game written in Python, running in Code Institute's mock terminal on Heroku.
The user is tasked to find the hidden boats on the computer's game board before the computer can find the boats on the players board.

[Live link to app >](https://battleboats-2.herokuapp.com/)

![Battleboats](assets/images/readme/bboats-main.png)
    index

## How to play

Battleboats is a variant of the classic board game Battleships. This version features boats which are only one square in size and are randomly placed on both players' boards.

The player is only able to see the position of their own boats, while the computer's boats are invisible.

Each turn starts with the player making a guess on where the computer's boats are hidden, then the computer makes a guess on the player's boats.
If a boat is found, it is "sunk". First side to find all the opponent's boats wins!
<br>
<br>

## Graphics

These are the symbols used in the game:

<code>. . . . .&nbsp;&nbsp;</code> Game board positions

<code>B&nbsp;&nbsp;</code> Boat 

<code>o&nbsp;&nbsp;</code> Missed shot 

<code>#&nbsp;&nbsp;</code> Hit / sunk boat 
<br>
<br>

## Features

### Existing Features

- Welcome screen
    - User is told the name and goal of the game
    - Number of hidden ships are shown to the user
    - User can start game by pressing ENTER
<br>
<br>
- Randomly generated game boards
    - Boats are placed in random positions on each board
    - The boats are hidden to the opponent
<br>
<br>
- User input prompt
    - User is asked to input row and column number of the computer's board
    - input is analyzed, feedback is given to the user
    - Computer automatically makes it's move after the player
<br>
<br>
- Feedback to user
    - User is shown the result of the last round through text
    - Game boards are redrawn to display the latest moves
    - Player and computer scores are updated
    - Any invalid input detected makes an error message appear
<br>
<br>
- Input validation and error-checking
    - User can only enter numbers
    - Only coordinates within the game board are allowed
    - Already sunk boats cannot be attacked again
    - User must enter a valid input to continue the game
<br>
<br>
- Game over screen
    - When either side sinks all the opponent's boats, the game is stopped and the winner is presented
    - User can press ENTER to restart the game
<br>
<br>
### Future (possible) Features
- Allow the player to input their own name
- Allow the player to set the board sizes (code is built to implement this easily)
- Include larger boats
<br>
<br>

## Data Model / Structure

The game uses a `Gameboard` class for it's model. Two instances are created which draws three game boards: One for the player and two for the computer (one of which is invisible to the user). 

The Gameboard class is used to store and process most of the data within the game, such as board size, number and position of boats, and the current state of each game board.

The computer uses two boards, since the invisible board is used to store the boat positions, while the visible board is used to display the hits and misses to the user. The Gameboard class har methods for checking for hits on one board and drawing them on the other.

The class uses the `make_board()` method to draw the board and place the boats at the beginning of the game, while the `redraw_board()` method checks for hits/misses, updates all boards each turn, displays gameplay messages and counts scores. 

Input prompts, validation and computer guesses are all handled within the main gameplay loop of the `new_game()` function.

<br>
<br>

## Development



<br>
<br>
    
## Testing


    bugs
    validator testing
<br>
<br>

## Deployment


<br>
<br>

## Credits


<br>
<br>
