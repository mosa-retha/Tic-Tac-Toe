from GameSystem import MainGame
from random import choice


class MiniMaxNode(MainGame):
    def __init__(self, tac_list, turn="X", depth=0, parent_index=None):
        super().__init__()
        self.tic_list = tac_list
        self.turn = turn
        self.children = []
        self.depth = depth
        self.parent_index = parent_index
        self.winner = self.win_check(turn, tac_list, cpu=True)


    def turn_x_o_(self, turn):
        if turn == "X":
            return "O"
        else:
            return "X"

    def insert(self, tac_list, turn, depth=0):

        if self.winner:
            return self.depth
        self.tic_list = tac_list
        self.children = []
        self.turn = turn
        for i in range(9):
            if tac_list[i] == " ":
                new_tic_list = tac_list.copy()
                new_tic_list[i] = turn
                self.children.append(MiniMaxNode(new_tic_list, turn, depth + 1, parent_index=i ))
                self.children[-1].insert(new_tic_list, self.turn_x_o_(turn), self.depth + 1)

    def minimax(self, turn):
        results = []
        available_choices = [ i for i in range(9) if self.tic_list[i] == " "]
        if self.tic_list[4] == " ":
            return -1, self.depth, 4

        if len(available_choices) == 8:
            return -1, self.depth, choice([0,2,6,8])


        if self.winner is None and " " not in self.tic_list:
            return 0, self.depth, self.parent_index
        elif self.winner:
            if turn == "X":
                return 1, self.depth, self.parent_index
            elif turn == "O":
                return -1, self.depth, self.parent_index
        elif self.winner is None:
            return 0, self.depth, self.parent_index


        if turn == "X":

            for child in self.children:
                ch = child.minimax("X")
                if isinstance(ch, tuple) and not ch in results:
                    results.append(ch)
                elif isinstance(ch, list) and not ch in results:
                    results.extend(ch)


            r = set(filter(lambda x: x[0] == 1, results))

            try :
                win = sorted(r, key=lambda x: x[1])
                return win[0]
            except:
                r = set(filter(lambda x: x[0] == 0, results))
                win = sorted(r, key=lambda x: x[1])
                return win[0]
        else:
            for child in self.children:
                ch = child.minimax("O")
                if isinstance(ch, tuple) and not ch in results:
                    results.append(ch)
                elif isinstance(ch, list) and not ch in results:
                    results.extend(ch)


            r = set(filter(lambda x: x[0] == -1, results))

            try :

                win = sorted(r, key=lambda x: x[1])
                return win[0]
            except:
                r = set(filter(lambda x: x[0] == 0, results))
                win = sorted(r, key=lambda x: x[1])
                return win[0]





if __name__ == "__main__":
    tic_list = [" ", " ", " ",
                " ", "O", " ",
                "X", " ", " "]
    node = MiniMaxNode(tic_list)
    node.insert(tic_list, "O")
    print("win results: ",node.minimax("O"))

