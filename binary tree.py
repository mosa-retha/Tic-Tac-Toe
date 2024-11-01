from GameSystem import MainGame


class Node(MainGame):
    def __init__(self, tic_list, turn="X", depth=0):
        super().__init__()
        self.tic_list = tic_list
        self.turn = turn
        self.children = []
        self.depth = depth
        print(tic_list[:3])
        print(tic_list[3:6])
        print(tic_list[6:])
        print(self.depth)
        self.winner = self.win_check(turn, tic_list)


    def turn_x_o_(self, turn):
        if turn == "X":
            return "O"
        else:
            return "X"

    def insert(self, tic_list, turn, depth=0):

        print(" ___________________")
        if self.winner:
            return self.winner
        self.tic_list = tic_list
        self.children = []
        self.turn = turn
        for i in range(9):
            if tic_list[i] == " ":
                new_tic_list = tic_list.copy()
                new_tic_list[i] = turn
                self.children.append(Node(new_tic_list, turn, depth + 1))
                self.children[-1].insert(new_tic_list, self.turn_x_o_(turn), self.depth + 1)

    def minimax(self, turn):
        if self.winner:
            if self.winner == "X":
                return 1
            else:
                return -1
        elif not self.children:
            return 0
        if turn == "X":
            pass




if __name__ == "__main__":
    tic_list = [" ", "O", "X",
                " ", "O", " ",
                "O", "X", "X"]
    node = Node(tic_list)
    node.insert(tic_list, "X")
    print(node.minimax("X"))

