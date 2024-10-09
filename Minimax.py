from GameSystem import MainGame
"""
[_,_,_
_,_,_
_,_,_]
"""

class MiniMax(MainGame):
    def __init__(self, tac_toe_list=[]):
        super().__init__()
        self.tac = tac_toe_list
        self.mini = -1
        self.max = +1
        self.tie = 0



    def minimax(self, count=0):
        if self.win_check("O"):
            return self.mini
        if self.win_check("X"):
            return self.max






