from GameSystem import MainGame
from random import choice

class MiniMaxNode(MainGame):
    def __init__(self, tac_list, turn="X", depth=0, parent_index=None):
        super().__init__()
        # Initialize a node with board state, player turn, depth, parent index, and winner status
        self.tic_list = tac_list  # Current board state
        self.turn = turn  # Current player's turn
        self.children = []  # List to store child nodes for each possible move
        self.depth = depth  # Depth level of this node in the minimax tree
        self.parent_index = parent_index  # Index of the move that created this node
        self.winner = self.win_check(turn, tac_list, cpu=True)  # Check if there's a winner at this node

    # Helper function to switch turns between "X" and "O"
    def turn_x_o_(self, turn):
        if turn == "X":
            return "O"
        else:
            return "X"

    # Recursive function to build the minimax tree by inserting possible moves
    def insert(self, tac_list, turn, depth=0):
        if self.winner:  # If a winner is found, end insertion at this node
            return self.depth

        self.tic_list = tac_list
        self.children = []  # Clear children list to store new child nodes
        self.turn = turn

        # Loop through each position to create child nodes for available moves
        for i in range(9):
            if tac_list[i] == " ":
                new_tic_list = tac_list.copy()  # Create a new board state for each possible move
                new_tic_list[i] = turn  # Place the current player's mark
                # Create and add a child node for this move
                self.children.append(MiniMaxNode(new_tic_list, turn, depth + 1, parent_index=i))
                # Recursively build the minimax tree for the next player's turn
                self.children[-1].insert(new_tic_list, self.turn_x_o_(turn), self.depth + 1)

    # Minimax function to determine the best move based on maximizing/minimizing the score
    def minimax(self, turn):
        results = []
        # Get available moves (empty spaces) on the board
        available_choices = [i for i in range(9) if self.tic_list[i] == " "]

        # Prefer center if available;
        if self.tic_list[4] == " ":
            return -1, self.depth, 4
        # If center is unavailable and only one move has been made, return a random corner move
        elif len(available_choices) == 8:
            return -1, self.depth, choice([0, 2, 6, 8])

        # If game is tied (no winner and no empty spaces), return a neutral score of 0
        if self.winner is None and " " not in self.tic_list:
            return 0, self.depth, self.parent_index
        elif self.winner:
            # Return a positive score for "X" win, negative for "O" win
            if turn == "X":
                return 1, self.depth, self.parent_index
            elif turn == "O":
                return -1, self.depth, self.parent_index


        # If it's "X"'s turn (maximizing player)
        if turn == "X":
            # Recursively get minimax values from child nodes
            for child in self.children:
                ch = child.minimax("X")
                if isinstance(ch, tuple) and ch not in results:
                    results.append(ch)
                elif isinstance(ch, list) and ch not in results:
                    results.extend(ch)

            # Filter for winning moves with highest priority
            r = set(filter(lambda x: x[0] == 1, results))
            try:
                win = sorted(r, key=lambda x: x[1])  # Sort by depth to prefer quickest win
                return win[0]
            except:
                # If no winning moves, prefer moves that result in a draw (score of 0)
                r = set(filter(lambda x: x[0] == 0, results))
                win = sorted(r, key=lambda x: x[1])
                return win[0]

        # If it's "O"'s turn (minimizing player)
        else:
            for child in self.children:
                ch = child.minimax("O")
                if isinstance(ch, tuple) and ch not in results:
                    results.append(ch)
                elif isinstance(ch, list) and ch not in results:
                    results.extend(ch)

            # Filter for moves that cause "X" to lose, with lowest priority for worst outcome
            r = set(filter(lambda x: x[0] == -1, results))
            try:
                win = sorted(r, key=lambda x: x[1])  # Sort by depth to prioritize quickest win for "O"
                return win[0]
            except:
                # If no losing moves, prefer draws (score of 0)
                r = set(filter(lambda x: x[0] == 0, results))
                win = sorted(r, key=lambda x: x[1])
                return win[0]


# Run a basic test of the MiniMaxNode class
if __name__ == "__main__":
    tic_list = [" ", " ", " ",
                " ", "O", " ",
                "X", " ", " "]  # Sample board state
    node = MiniMaxNode(tic_list)
    node.insert(tic_list, "O")  # Build minimax tree with "O" as the starting player
    print("win results: ", node.minimax("O"))  # Calculate and print optimal move for "O"
