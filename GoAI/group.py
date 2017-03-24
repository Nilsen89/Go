##GROUP

import rules
import analyze

class Group(object):
    def __init__(self, group, player, board):
        self.group = group
        self.player = player

        if player == 'X': self.other_player = 'O'
        else: self.other_player = 'X'
        self.liberties = self.find_liberties(board)

    """ Adds move to group then update
        the object.
    """
    def add_move(self, move, board):
        self.group.append(move)
        self.update(board)

    """ Finds the liberties of the group.
        Liberties is empty adjacent cell on
        the board. Returns a list with the cells.
    """
    def find_liberties(self, board):
        liberties = []
        for move in self.group:
            neighbours = analyze.get_neighbours(move)
            for neighbour in neighbours:
                if board.get_cell(neighbour) == '.':
                    if not neighbour in liberties:
                        liberties.append(neighbour)
        return liberties
    
    """ Updates the group 'state', checking liberties
        and if the group is dead.
    """
    def update(self, board):
        self.liberties = self.find_liberties(board)

        if not self.liberties:
            self.is_group_dead(board)
            return False
        return True

    """ 
    """
    def is_group_dead(self, board):
        for move in self.group:
            board.set_cell(move, '.')
            #turn.add_capture(move)