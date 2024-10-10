from random import randint, choice

from GameSystem import MainGame
"""
[_,_,_
_,_,_
_,_,_]
"""

class MiniMax(MainGame):
    def __init__(self):
        super().__init__()
        self.mini = -1
        self.max = +1
        self.tie = 0



    def minimax(self, tic_list,count=0):
        turn = self.turn_x_o()
        print(tic_list)
        available_choices = [index for index, value in enumerate(tic_list) if value == " "]

        if self.win_check("O", tic_list):
            return self.mini, count
        if self.win_check("X", tic_list):
            return self.max, count
        if " " not in tic_list:
            return self.tie, count

        choice_ = choice(available_choices)

        if self.taken(turn,num=choice_, tic_list=tic_list, ai=True):
            count += 1
            return self.minimax(tic_list,count)











