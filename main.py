from GameSystem import MainGame
from MiniMax import MiniMaxNode
import turtleG as t  # Custom module for Turtle graphics

# Function to print the game board in ASCII art, row by row
def print_ascii_art():
    # Initialize an empty string to accumulate the ASCII art for the board
    f = ""
    for i in range(0, 9, 3):  # Loop through each row in chunks of 3 for a 3x3 board
        if i > 0:
            # Add a separator line between each row of the board
            f += """  ________________________________________\n"""

        for j in range(7):  # Each row of ASCII art has 7 lines for visual formatting
            # Append ASCII art of each cell in the row, separated by vertical lines
            f += f"""{game.ascii_print(j, i)}|{game.ascii_print(j, i+1)}|{game.ascii_print(j, i+2)}\n"""

    return f  # Return the complete ASCII representation of the board

# Initialize main game instance and board
game = MainGame()  # Instance of the main game logic
tic = game.tic  # Tic-tac-toe board state array

# Function to print a welcome ASCII art message
def print_welcome_ascii():
    # Welcome ASCII art for a fun introduction to the game
    return """ 
               .__                                  __             __  .__           __                    __                  ._.
__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_  ____   _/  |_|__| ____   _/  |______    ____   _/  |_  ____   ____   | |
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\  |/ ___\  \   __\__  \ _/ ___\  \   __\/  _ \_/ __ \  | |
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  | |  \  \___   |  |  / __ \\  \___   |  | (  <_> )  ___/   \|
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__| |__|\___  >  |__| (____  /\___  >  |__|  \____/ \___  >  __
             \/          \/            \/     \/                               \/             \/     \/                    \/   \/
"""

# Function to choose display type: Turtle graphics or ASCII art
def display_type(play_view):
    # Show the game in Turtle graphics if play_view is True; otherwise, use ASCII art
    if play_view:
        display_turtle_graphics()
    else:
        print(print_ascii_art())

# Function to display the game using Turtle graphics
def display_turtle_graphics():
    # Iterate over each position on the tic-tac-toe board
    for i in range(9):
        # Check if position 'i' has an 'X' and hasn't been drawn yet
        if tic[i] == "X" and i not in t.printed:
            t.draw_number(i, t.key[i], erase=True)  # Erase the number in the cell
            t.draw_X(t.key[i])  # Draw the 'X' symbol in the cell
            t.printed.append(i)  # Mark this cell as drawn
        # Check if position 'i' has an 'O' and hasn't been drawn yet
        elif tic[i] == "O" and i not in t.printed:
            t.draw_number(i, t.key[i], erase=True)  # Erase the number in the cell
            t.draw_O(t.key[i])  # Draw the 'O' symbol in the cell
            t.printed.append(i)  # Mark this cell as drawn

# Main game loop for playing against the CPU
def play_with_cpu(play_view=False):
    game_started = True
    while game_started:
        # Player's turn (X)
        turn = "X"
        if not game.taken(turn, tic):
            display_type(play_view)  # Update display if move is invalid
            continue
        display_type(play_view)  # Update display after valid move
        winner = game.win_check(turn, tic)  # Check if player has won
        if winner or winner is None:  # Break loop if game ends
            break

        # CPU's turn (O)
        turn = "O"
        node = MiniMaxNode(tic)  # Initialize MiniMax algorithm for the board state
        node.insert(tic, turn)  # Insert current state into MiniMax
        num = node.minimax(turn)  # Get best move from MiniMax

        if not game.taken(turn, tic, num=num[2], cpu=True):
            display_type(play_view)  # Update display if CPU move is invalid
            continue
        display_type(play_view)  # Update display after valid CPU move
        winner = game.win_check(turn, tic)  # Check if CPU has won
        if winner or winner is None:  # Break loop if game ends
            break

# Main game loop for playing against another player
def play_with_player(play_view=False):
    game_started = True
    while game_started:
        # Player 1's turn (X)
        turn = "X"
        if not game.taken(turn, tic):
            display_type(play_view)  # Update display if move is invalid
            continue
        display_type(play_view)  # Update display after valid move
        winner = game.win_check(turn, tic)  # Check if player 1 has won
        if winner or winner is None:  # Break loop if game ends
            break

        # Player 2's turn (O)
        turn = "O"
        if not game.taken(turn, tic):
            display_type(play_view)  # Update display if move is invalid
            continue
        display_type(play_view)  # Update display after valid move
        winner = game.win_check(turn, tic)  # Check if player 2 has won
        if winner or winner is None:  # Break loop if game ends
            break

# Prompt to choose game mode: CPU or another player, CLI or GUI
def play_type(play_view=False):
    while True:
        # Ask user to choose CLI or GUI display
        play_view_input = input("Do you want to play with the CLI or GUI? (CLI/GUI): ").lower()
        play = ""
        if play_view_input == "gui":
            # Setup for Turtle Graphics GUI
            print("Turtle Graphics")
            print("Please wait for the turtle graphics to load...")
            print("A window will pop up")
            print("Enter your input in the console")
            print("Use the num pad to enter your input")
            play = t.get_user_player_type()  # Choose CPU or player for Turtle GUI
            t.set_window_properties()  # Setup Turtle window properties
            t.draw_board()  # Draw initial tic-tac-toe board
            play_view = True
        elif play_view_input == "cli":
            # Setup for CLI ASCII Art display
            print("ASCII Art")
            play = input("Do you want to play with CPU or Player? (CPU/Player): ").lower()
        else:
            print("Please enter a valid input")
            continue

        # Start the selected game mode based on user choice
        if play == "cpu":
            display_type(play_view)  # Show initial board state
            play_with_cpu(play_view)  # Play against CPU
            break
        elif play == "player":
            display_type(play_view)  # Show initial board state
            play_with_player(play_view)  # Play against another player
            break
        else:
            print("Please enter a valid input")

# Main function to start the game
def main():
    # Display welcome ASCII art message
    print(print_welcome_ascii())
    # Start the game mode selection prompt
    play_type()
    # Game over message after gameplay ends
    print("Game Over")
    print("Thanks for playing")
    print("Bye!")

if __name__ == "__main__":
    # Run the main function to start the game
    main()
