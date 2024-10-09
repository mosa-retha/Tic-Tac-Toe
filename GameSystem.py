from Keys import Key


class MainGame(Key):
    def __init__(self):
        self.tic = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.key = {
            7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8
        }

    # checking if the winning conditions are met
    def win_check(self, n):
        if self.tic[0] == n and self.tic[1] == n and self.tic[2] == n:
            if n == "X":
                print("Player 1 Wins!")
            elif n == "O":
                print("Player 2 Wins!")
            return True
        elif self.tic[3] == n and self.tic[4] == n and self.tic[5] == n:
            if n == "X":
                print("Player 1 Wins!")
            elif n == "O":
                print("Player 2 Wins!")
            return True
        elif self.tic[6] == n and self.tic[7] == n and self.tic[8] == n:
            if n == "X":
                print("Player 1 Wins!")
            elif n == "O":
                print("Player 2 Wins!")
            return True
        elif self.tic[0] == n and self.tic[3] == n and self.tic[6] == n:
            if n == "X":
                print("Player 1 Wins!")
            elif n == "O":
                print("Player 2 Wins!")
            return True
        elif self.tic[1] == n and self.tic[4] == n and self.tic[7] == n:
            if n == "X":
                print("Player 1 Wins!")
            elif n == "O":
                print("Player 2 Wins!")
            return True
        elif self.tic[2] == n and self.tic[5] == n and self.tic[8] == n:
            if n == "X":
                print("Player 1 Wins!")
            elif n == "O":
                print("Player 2 Wins!")
            return True
        elif self.tic[0] == n and self.tic[4] == n and self.tic[8] == n:
            if n == "X":
                print("Player 1 Wins!")
            elif n == "O":
                print("Player 2 Wins!")
            return True
        elif self.tic[2] == n and self.tic[4] == n and self.tic[6] == n:
            if n == "X":
                print("Player 1 Wins!")
            elif n == "O":
                print("Player 2 Wins!")
            return True
        else:
            return False

    #  checks whether a position taken yet, if not an 'X' or 'O' is assigned to that position
    def taken(self, p):
        player = self.key[int(input(f"{p}: "))]
        if self.tic[player] == "X" or self.tic[player] == "O":
            print('This position is taken please pick another one')
            return self.taken(p)
        else:
            self.tic[player] = p

# --- below is for printing the ascii art of 'X' or 'O' to the designated position ---
    def one(self, num):
        if self.tic[0] == "X" or self.tic[0] == "O":
            if self.tic[0] == "O":
                return self.putOInSquares(num)
            elif self.tic[0] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

    def two(self, num):
        if self.tic[1] == "X" or self.tic[1] == "O":
            if self.tic[1] == "O":
                return self.putOInSquares(num)
            elif self.tic[1] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

    def three(self, num):
        if self.tic[2] == "X" or self.tic[2] == "O":
            if self.tic[2] == "O":
                return self.putOInSquares(num)
            elif self.tic[2] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

    def four(self, num):
        if self.tic[3] == "X" or self.tic[3] == "O":
            if self.tic[3] == "O":
                return self.putOInSquares(num)
            elif self.tic[3] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

    def five(self, num):
        if self.tic[4] == "X" or self.tic[4] == "O":
            if self.tic[4] == "O":
                return self.putOInSquares(num)
            elif self.tic[4] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

    def six(self, num):
        if self.tic[5] == "X" or self.tic[5] == "O":
            if self.tic[5] == "O":
                return self.putOInSquares(num)
            elif self.tic[5] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

    def seven(self, num):
        if self.tic[6] == "X" or self.tic[6] == "O":
            if self.tic[6] == "O":
                return self.putOInSquares(num)
            elif self.tic[6] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

    def eight(self, num):
        if self.tic[7] == "X" or self.tic[7] == "O":
            if self.tic[7] == "O":
                return self.putOInSquares(num)
            elif self.tic[7] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)

    def nine(self, num):
        if self.tic[8] == "X" or self.tic[8] == "O":
            if self.tic[8] == "O":
                return self.putOInSquares(num)
            elif self.tic[8] == "X":
                return self.putXInSquares(num)
        else:
            return self.putEInSquares(num)
