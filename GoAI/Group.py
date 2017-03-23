##GROUP

import Rules

class Group(object):
    def __init__(self, group, player, board):
        self.group = group
        self.player = player

        if player == 'X': self.other_player = 'O'
        else: self.other_player = 'X'

        self.liberties = self.find_liberties(board)
        self.free_liberties = self.find_free_liberties(board)

    def add_move(self, move, board):
        self.group.append(move)
        self.update(board)

    def find_liberties(self, board):
        liberties = []
        for move in self.group:
            neighbours = Rules.get_neighbours(move)
            for neighbour in neighbours:
                if board.get_cell(neighbour) != self.player:
                    liberties.append(neighbour)
        return liberties

    def find_free_liberties(self, board):
        free_liberties = []
        for liberty in self.liberties:
            if not board.get_cell(liberty) == self.other_player:
                free_liberties.append(liberty)
        return free_liberties

    def update(self, board):
        self.liberties = self.find_liberties(board)
        self.free_liberties = self.find_free_liberties(board)

        if not self.free_liberties:
            self.kill_group(board)
            return False
        else: return True

    def kill_group(self, board):
        for move in self.group:
            board.set_cell(move, '.')
