from GameSystem import MainGame

from MiniMax import MiniMaxNode

import turtleG as t



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


def display_type(play_view):
    if play_view:
        display_turtle_graphics()
    else:
        print(print_ascii_art())



def display_turtle_graphics():
    inverted_key = invert_dict(game.key)
    for i in range(9):
        if tic[i] == "X" and i not in t.printed:
            t.draw_number(inverted_key[i], t.key[i], erase=True)
            t.draw_X(t.key[i])
            t.printed.append(i)
        elif tic[i] == "O" and i not in t.printed:
            t.draw_number(inverted_key[i], t.key[i], erase=True)
            t.draw_O(t.key[i])
            t.printed.append(i)

def invert_dict(d):
    return {v: k for k, v in d.items()}

def play_with_cpu(play_view=False):
    game_started = True
    while game_started:
        turn = "X"

        if not game.taken(turn, tic):
            display_type(play_view)
            continue
        display_type(play_view)
        winner = game.win_check(turn, tic)
        if winner or winner is None:
            break

        turn = "O"
        node = MiniMaxNode(tic)
        node.insert(tic, turn)
        num = node.minimax(turn)

        if not game.taken(turn, tic, num=num[2], cpu=True):
            display_type(play_view)
            continue
        display_type(play_view)
        winner = game.win_check(turn, tic)
        if winner or winner is None:
            break


def play_with_player(play_view=False):
    game_started = True
    while game_started:
        turn = "X"
        if not game.taken(turn, tic):
            display_type(play_view)
            continue
        display_type(play_view)
        winner = game.win_check(turn, tic)
        if winner or winner is None:
            break

        turn = "O"
        if not game.taken(turn, tic):
            display_type(play_view)
            continue
        display_type(play_view)
        winner = game.win_check(turn, tic)
        if winner or winner is None:
            break




def play_type(play_view=False):
    while True:
        play_view_input = input("Do you want to play with the CLI or GUI? (CLI/GUI): ").lower()
        play = ""
        if play_view_input == "gui":
            print("Turtle Graphics")
            print("Please wait for the turtle graphics to load")
            print("A window will pop up")
            print("Please enter your input in the console")
            print("Please use the num pad to enter your input")
            play = t.get_user_player_type()
            t.set_window_properties()
            t.draw_board()
            play_view = True
        elif play_view_input == "cli":
            print("ASCII Art")
            play = input("Do you want to play with CPU or Player? (CPU/Player): ").lower()
        else:
            print("Please enter a valid input")
            continue


        if play == "cpu":
            display_type(play_view)
            play_with_cpu(play_view)
            break
        elif play == "player":
            display_type(play_view)
            play_with_player(play_view)
            break
        else:
            print("Please enter a valid input")


def main():
    print(print_welcome_ascii())
    play_type()
    print("Game Over")
    print("Thanks for playing")
    print("Bye!")

if __name__ == "__main__":
    main()


