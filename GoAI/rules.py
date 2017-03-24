##RULES

import analyze
from move import Move
#from group import Group

""" Checks if the move follow all Go rules.
    Returns False if one or more rules are 
    broken. True otherwise.
"""
def is_legal_pre_move(board, move):
    if not is_empty(board, move):
        print("Illegal Move")
        return False
    return True

def is_legal_post_move(board, move):
    if ko():
        #ToDo
        pass
    if is_self_atari(board, move):
        return False
    return True

""" Checks if the move is being placed
    on an empty cell at the board.
"""
def is_empty(board, move):
    return board.get_cell(move) == '.'

""" Checks if the move being placed
    is in self atari.
"""
def is_self_atari(board, move):
    neighbours_cords = analyze.get_neighbours(move)
    for moves in neighbours_cords:
        if not board.get_cell(move) == move.other_player:
            return False
    return True

""" Checks if group should be captured.
"""
def capture(board, group):
    if not group.free_liberites:
        print("Dead group")

""" Checks if the move followed
    Ko rules.
"""
def ko():
    pass