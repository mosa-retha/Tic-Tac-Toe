import pytest
from MiniMax import MiniMaxNode

def test_turn_x_o_():
    node = MiniMaxNode([" "]*9)
    assert node.turn_x_o_("X") == "O"
    assert node.turn_x_o_("O") == "X"

def test_insert():
    node = MiniMaxNode([" "]*9)
    node.insert([" "]*9, "X")
    assert len(node.children) > 0

def test_minimax():
    tic_list = [" ", " ", " ",
                " ", "O", " ",
                "X", " ", " "]
    node = MiniMaxNode(tic_list)
    node.insert(tic_list, "O")
    result = node.minimax("O")
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert result[0] in [-1, 0, 1]


