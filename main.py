from GameSystem import MainGame
# from random import randint, choice


# prints ascii art step by step
def f():
    f = f"""
    {game.one(0)}|{game.two(0)}|{game.three(0)}
    {game.one(1)}|{game.two(1)}|{game.three(1)}
    {game.one(2)}|{game.two(2)}|{game.three(2)}
    {game.one(3)}|{game.two(3)}|{game.three(3)}
    {game.one(4)}|{game.two(4)}|{game.three(4)}
    {game.one(5)}|{game.two(5)}|{game.three(5)}
    {game.one(6)}|{game.two(6)}|{game.three(6)}
    ________________________________________
    {game.four(0)}|{game.five(0)}|{game.six(0)}
    {game.four(1)}|{game.five(1)}|{game.six(1)}
    {game.four(2)}|{game.five(2)}|{game.six(2)}
    {game.four(3)}|{game.five(3)}|{game.six(3)}
    {game.four(4)}|{game.five(4)}|{game.six(4)}
    {game.four(5)}|{game.five(5)}|{game.six(5)}
    {game.four(6)}|{game.five(6)}|{game.six(6)}
    ________________________________________
    {game.seven(0)}|{game.eight(0)}|{game.nine(0)}
    {game.seven(1)}|{game.eight(1)}|{game.nine(1)}
    {game.seven(2)}|{game.eight(2)}|{game.nine(2)}
    {game.seven(3)}|{game.eight(3)}|{game.nine(3)}
    {game.seven(4)}|{game.eight(4)}|{game.nine(4)}
    {game.seven(5)}|{game.eight(5)}|{game.nine(5)}
    {game.seven(6)}|{game.eight(6)}|{game.nine(6)}
    """
    return f


# direc = {
#     0: [0, 1, 2],
#     1: [1, 4, 7],
#     2: [2, 5, 8],
#     3: [3, 4, 5],
#     4: [0, 3, 6],
#     5: [6, 7, 8],
#     6: [0, 4, 8],
#     7: [2, 4, 6]
# }


# def blocking():
#     x_indice = [i for i, value in enumerate(tic) if value == "X"]
#     print(x_indice)
#     for key, item in direc.items():
#         for x in item:
#             if x in x_indice:


# def taken(com):
#     if tic[com] == "X" or tic[com] == "O":
#         return taken(com)
#     else:
#         tic[com] = "O"

game = MainGame()
#
# rand = randint(0, 8)
# print(rand)
tic = game.tic
# winpos = {key: item for (key, item) in direc.items() if rand in item}
#
#
# for key, item in winpos.items():
#     for id in item:
#         if rand == id:
#             item.remove(id)


# for key, item in winpos.items():
#     if tic[item[0]] == " " and tic[item[1]] == " ":
#         pick = choice(key)
#
#         break

# def com_select():
#     fpick = choice(list(winpos.keys()))
#     print(fpick)
#     if tic[item[0]] == " " and tic[item[1]] == " ":
#         print(winpos[fpick])
#         spick = choice(winpos[fpick])
#         taken(spick)


print(f())
game_started = True

# the game loop
while game_started:
    game.taken("X")
    print(tic)
    print(f())
    if game.win_check("X"):
        break
    game.taken("O")
    print(tic)
    print(f())
    if game.win_check("O"):
        break
