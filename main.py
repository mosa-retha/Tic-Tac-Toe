from GameSystem import MainGame
from Minimax import MiniMax

# from random import randint, choice


# prints ascii art step by step

def print_ascii_art():
    f = ""
    for i in range(0,9,3):
        if i > 0:
            f += """  ________________________________________\n"""

        for j in range(7):
            f += f"""{game.ascii_print(j, i)}|{game.ascii_print(j, i+1)}|{game.ascii_print(j, i+2)}\n"""

    return f


game = MainGame()


minimax = MiniMax()
tic = game.tic


print(print_ascii_art())
game_started = True

# the game loop
while game_started:
    turn = game.turn_x_o()
    if not game.taken(turn, tic):
        print(print_ascii_art())
        continue
    print(print_ascii_art())
    if game.win_check(turn, tic):
        break

