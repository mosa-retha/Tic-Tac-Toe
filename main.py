from more_itertools.more import first

from GameSystem import MainGame

from MiniMax import MiniMaxNode

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


tic = game.tic

def print_welcome_ascii():
    return """ 
               .__                                  __             __  .__           __                    __                  ._.
__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_  ____   _/  |_|__| ____   _/  |______    ____   _/  |_  ____   ____   | |
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\  |/ ___\  \   __\__  \ _/ ___\  \   __\/  _ \_/ __ \  | |
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  | |  \  \___   |  |  / __ \\  \___   |  | (  <_> )  ___/   \|
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__| |__|\___  >  |__| (____  /\___  >  |__|  \____/ \___  >  __
             \/          \/            \/     \/                               \/             \/     \/                    \/   \/

"""

print(print_ascii_art())
game_started = True

# the game loop
while game_started:
    turn = "X"

    if not game.taken(turn, tic):
        print(print_ascii_art())
        continue

    if game.win_check(turn, tic):
        break

    turn = "O"
    node = MiniMaxNode(tic)
    node.insert(tic, turn)
    num = node.minimax(turn)

    if not game.taken(turn,tic, num=num[2] , ai=True):
        print(print_ascii_art())
        continue
    print(print_ascii_art())
    if game.win_check(turn, tic):
        break

