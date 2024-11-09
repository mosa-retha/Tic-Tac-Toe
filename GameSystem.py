from Keys import Key


class MainGame(Key):
    def __init__(self):
        self.tic = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.key = {
            7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8
        }
        self.turn = False

    def turn_x_o(self):
        self.turn = not self.turn
        if self.turn:
            return "X"
        else:
            return "O"


    # checking if the winning conditions are met
    def win_check(self, n, tic_list, cpu=False):

        if tic_list[0] == n and tic_list[1] == n and tic_list[2] == n:
            if n == "X" and cpu == False:
                print("Player 1 Wins!")
            elif n == "O" and cpu == False:
                print("Player 2 Wins!")
            return True
        elif tic_list[3] == n and tic_list[4] == n and tic_list[5] == n:
            if n == "X" and cpu == False:
                print("Player 1 Wins!")
            elif n == "O" and cpu == False:
                print("Player 2 Wins!")
            return True
        elif tic_list[6] == n and tic_list[7] == n and tic_list[8] == n:
            if n == "X" and cpu == False:
                print("Player 1 Wins!")
            elif n == "O" and cpu == False:
                print("Player 2 Wins!")
            return True
        elif tic_list[0] == n and tic_list[3] == n and tic_list[6] == n:
            if n == "X" and cpu == False:
                print("Player 1 Wins!")
            elif n == "O" and cpu == False:
                print("Player 2 Wins!")
            return True
        elif tic_list[1] == n and tic_list[4] == n and tic_list[7] == n:
            if n == "X" and cpu == False:
                print("Player 1 Wins!")
            elif n == "O" and cpu == False:
                print("Player 2 Wins!")
            return True
        elif tic_list[2] == n and tic_list[5] == n and tic_list[8] == n:
            if n == "X" and cpu == False:
                print("Player 1 Wins!")
            elif n == "O" and cpu == False:
                print("Player 2 Wins!")
            return True
        elif tic_list[0] == n and tic_list[4] == n and tic_list[8] == n:
            if n == "X" and cpu == False:
                print("Player 1 Wins!")
            elif n == "O" and cpu == False:
                print("Player 2 Wins!")
            return True
        elif tic_list[2] == n and tic_list[4] == n and tic_list[6] == n:
            if n == "X" and cpu == False:
                print("Player 1 Wins!")
            elif n == "O" and cpu == False:
                print("Player 2 Wins!")
            return True
        elif " " not in tic_list:
            if not cpu: print("Tie!")
            return None
        else:
            return False


    def game_input(self, x_o):
        player = self.key[int(input(f"{x_o}: "))]
        print(player)
        return player


    #  checks whether a position taken yet, if not an 'X' or 'O' is assigned to that position
    def taken(self, x_o, tic_list, num=0, cpu = False):

        if cpu:
            game_input = num
        else:
            game_input = self.game_input(x_o)
        try:
            if tic_list[game_input] == " ":
                tic_list[game_input] = x_o
                return True
            else:
                print('This position is taken please pick another one')
                return False
        except (KeyError, ValueError):
            print('Please enter a number between 1-9')
            return False

# --- below is for printing the ascii art of 'X' or 'O' to the designated position ---

    def ascii_print(self, num, list_index):
        if self.tic[list_index] == "O" or self.tic[list_index] == "X":
            if self.tic[list_index] == "O":
                return self.putOInSquares(num)
            elif self.tic[list_index] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

