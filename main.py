from GameSystem import MainGame

from MiniMax import MiniMaxNode



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





def play_with_cpu():
    game_started = True
    while game_started:
        turn = "X"

        if not game.taken(turn, tic):
            print(print_ascii_art())
            continue

        print(print_ascii_art())
        winner = game.win_check(turn, tic)
        if winner or winner is None:
            break

        turn = "O"
        node = MiniMaxNode(tic)
        node.insert(tic, turn)
        num = node.minimax(turn)

        if not game.taken(turn, tic, num=num[2], cpu=True):
            print(print_ascii_art())
            continue

        print(print_ascii_art())
        winner = game.win_check(turn, tic)
        if winner or winner is None:
            break


def play_with_player():
    game_started = True
    while game_started:
        turn = "X"
        if not game.taken(turn, tic):
            print(print_ascii_art())
            continue

        print(print_ascii_art())
        winner = game.win_check(turn, tic)
        if winner or winner is None:
            break

        turn = "O"
        if not game.taken(turn, tic):
            print(print_ascii_art())
            continue

        print(print_ascii_art())
        winner = game.win_check(turn, tic)
        if winner or winner is None:
            break


def play_type():
    while True:
        play = input("Do you want to play with CPU or Player? (CPU/Player): ").lower()
        print(print_ascii_art())
        if play == "cpu":
            play_with_cpu()
            break
        elif play == "player":
            play_with_player()
            break
        else:
            print("Please enter a valid input")



if __name__ == "__main__":
    print(print_welcome_ascii())
    play_type()
    print("Game Over")
    print("Thanks for playing")
    print("Bye!")


