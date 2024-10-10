from GameSystem import MainGame
from Minimax import MiniMax

# from random import randint, choice


# prints ascii art step by step
def f():
    f = f"""
    {game.ascii_print(0, 0)}|{game.ascii_print(0,1)}|{game.ascii_print(0, 2)}
    {game.ascii_print(1, 0)}|{game.ascii_print(1,1)}|{game.ascii_print(1, 2)}
    {game.ascii_print(2, 0)}|{game.ascii_print(2,1)}|{game.ascii_print(2, 2)}
    {game.ascii_print(3, 0)}|{game.ascii_print(3,1)}|{game.ascii_print(3, 2)}
    {game.ascii_print(4, 0)}|{game.ascii_print(4,1)}|{game.ascii_print(4, 2)}
    {game.ascii_print(5, 0)}|{game.ascii_print(5,1)}|{game.ascii_print(5, 2)}
    {game.ascii_print(6, 0)}|{game.ascii_print(6,1)}|{game.ascii_print(6, 2)}
    ________________________________________
    {game.ascii_print(0,3)}|{game.ascii_print(0,4)}|{game.ascii_print(0,5)}
    {game.ascii_print(1,3)}|{game.ascii_print(1,4)}|{game.ascii_print(1,5)}
    {game.ascii_print(2,3)}|{game.ascii_print(2,4)}|{game.ascii_print(2,5)}
    {game.ascii_print(3,3)}|{game.ascii_print(3,4)}|{game.ascii_print(3,5)}
    {game.ascii_print(4,3)}|{game.ascii_print(4,4)}|{game.ascii_print(4,5)}
    {game.ascii_print(5,3)}|{game.ascii_print(5,4)}|{game.ascii_print(5,5)}
    {game.ascii_print(6,3)}|{game.ascii_print(6,4)}|{game.ascii_print(6,5)}
    ________________________________________
    {game.ascii_print(0,6)}|{game.ascii_print(0,7)}|{game.ascii_print(0,8)}
    {game.ascii_print(1,6)}|{game.ascii_print(1,7)}|{game.ascii_print(1,8)}
    {game.ascii_print(2,6)}|{game.ascii_print(2,7)}|{game.ascii_print(2,8)}
    {game.ascii_print(3,6)}|{game.ascii_print(3,7)}|{game.ascii_print(3,8)}
    {game.ascii_print(4,6)}|{game.ascii_print(4,7)}|{game.ascii_print(4,8)}
    {game.ascii_print(5,6)}|{game.ascii_print(5,7)}|{game.ascii_print(5,8)}
    {game.ascii_print(6,6)}|{game.ascii_print(6,7)}|{game.ascii_print(6,8)}
    """
    return f


game = MainGame()
minimax = MiniMax()
tic = game.tic


print(f())
game_started = True

# the game loop
while game_started:
    turn = game.turn_x_o()
    print(minimax.minimax(tic))
    if not game.taken(turn, tic):
        print(f())
        continue
    print(f())
    if game.win_check(turn, tic):
        break

