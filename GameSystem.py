from Keys import Key


class MainGame(Key):
    def __init__(self):
        # Initialize the tic-tac-toe board and other properties
        self.tic = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Empty board represented by a list
        self.key = {  # Mapping of numpad keys to board positions
            7: 0, 8: 1, 9: 2,
            4: 3, 5: 4, 6: 5,
            1: 6, 2: 7, 3: 8
        }
        self.turn = False  # Tracks the current player's turn

    # Function to toggle between 'X' and 'O' for each turn
    def turn_x_o(self):
        self.turn = not self.turn  # Switch the turn
        if self.turn:
            return "X"  # Return 'X' for Player 1
        else:
            return "O"  # Return 'O' for Player 2

    # Checks for winning conditions or a tie
    def win_check(self, n, tic_list, cpu=False):
        # Check each possible winning line on the board
        if tic_list[0] == n and tic_list[1] == n and tic_list[2] == n:
            if n == "X" and not cpu:
                print("Player 1 Wins!")
            elif n == "O" and not cpu:
                print("Player 2 Wins!")
            return True
        elif tic_list[3] == n and tic_list[4] == n and tic_list[5] == n:
            if n == "X" and not cpu:
                print("Player 1 Wins!")
            elif n == "O" and not cpu:
                print("Player 2 Wins!")
            return True
        elif tic_list[6] == n and tic_list[7] == n and tic_list[8] == n:
            if n == "X" and not cpu:
                print("Player 1 Wins!")
            elif n == "O" and not cpu:
                print("Player 2 Wins!")
            return True
        elif tic_list[0] == n and tic_list[3] == n and tic_list[6] == n:
            if n == "X" and not cpu:
                print("Player 1 Wins!")
            elif n == "O" and not cpu:
                print("Player 2 Wins!")
            return True
        elif tic_list[1] == n and tic_list[4] == n and tic_list[7] == n:
            if n == "X" and not cpu:
                print("Player 1 Wins!")
            elif n == "O" and not cpu:
                print("Player 2 Wins!")
            return True
        elif tic_list[2] == n and tic_list[5] == n and tic_list[8] == n:
            if n == "X" and not cpu:
                print("Player 1 Wins!")
            elif n == "O" and not cpu:
                print("Player 2 Wins!")
            return True
        elif tic_list[0] == n and tic_list[4] == n and tic_list[8] == n:
            if n == "X" and not cpu:
                print("Player 1 Wins!")
            elif n == "O" and not cpu:
                print("Player 2 Wins!")
            return True
        elif tic_list[2] == n and tic_list[4] == n and tic_list[6] == n:
            if n == "X" and not cpu:
                print("Player 1 Wins!")
            elif n == "O" and not cpu:
                print("Player 2 Wins!")
            return True
        elif " " not in tic_list:  # If no empty spaces remain, it's a tie
            if not cpu:
                print("Tie!")
            return None
        else:
            return False  # Continue playing if no win/tie conditions met

    # Prompts user for input and maps input to the board index
    def game_input(self, x_o):
        try:
            player = self.key[int(input(f"{x_o}: "))]  # Get player's input mapped to board index
            print(player)
            return player
        except (KeyError, ValueError):
            print('Please enter a number between 1-9')  # Error handling for invalid input
            return self.game_input(x_o)  # Retry input on error

    # Checks if a position is already taken; assigns 'X' or 'O' if not taken
    def taken(self, x_o, tic_list, num=0, cpu=False):
        if cpu:
            game_input = num  # For CPU, take the provided move
        else:
            game_input = self.game_input(x_o)  # For player, prompt input

        try:
            if tic_list[game_input] == " ":  # Check if the position is empty
                tic_list[game_input] = x_o  # Assign 'X' or 'O' to the position
                return True
            else:
                print('This position is taken please pick another one')  # Notify if position is taken
                return False
        except (KeyError, ValueError, TypeError):
            print('Please enter a number between 1-9')  # Handle invalid input
            return False

    # Prints ASCII art for 'X' or 'O' based on the board's current state
    def ascii_print(self, num, list_index):
        if self.tic[list_index] == "O" or self.tic[list_index] == "X":
            if self.tic[list_index] == "O":
                return self.putOInSquares(num)  # Print 'O' in ASCII art format
            elif self.tic[list_index] == "X":
                return self.putXInSquares(num)  # Print 'X' in ASCII art format
        else:
            return self.putEInSquares(num)  # Print an empty square in ASCII format
