##Help functions for stones/groups/all groups

from move import Move

""" Function returns the neighbour cells for the move.
    Neighbours are only moves which share a liberty,
    with the move.
"""
def get_neighbours(move):
    neighbours_cords = []
    for offset in range(-1, 2):
        if offset == 0:
            continue
        offset_x = move.x + offset
        offset_y = move.y + offset
        if offset_x > -1 and offset_x < 19:
            neighbours_cords.append(Move(offset_x, move.y, move.player))
        if offset_y > -1 and offset_y < 19:
            neighbours_cords.append(Move(move.x, offset_y, move.player))
    return neighbours_cords

""" Checking if the group has no liberties.
"""
def has_liberties(group):
    return len(group.liberties) > 0
