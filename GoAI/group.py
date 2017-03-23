##GROUP

import rules

class Group(object):
    def __init__(self, group, player, board):
        self.group = group
        self.player = player

        if player == 'X': self.other_player = 'O'
        else: self.other_player = 'X'
        self.liberties = []
        self.update(board)
        
        #self.liberties = self.find_liberties(board)

    def add_move(self, move, board):
        self.group.append(move)
        self.update(board)

    def find_liberties(self, board):
        liberties = []
        for move in self.group:
            neighbours = rules.get_neighbours(move)
            for neighbour in neighbours:
                if board.get_cell(neighbour) == '.':
                    if not neighbour in liberties:
                        liberties.append(neighbour)
        return liberties

    def update(self, board):
        self.liberties = self.find_liberties(board)

        if not self.liberties:
            self.kill_group(board)
            return False
        return True

    def kill_group(self, board):
        for move in self.group:
            board.set_cell(move, '.')
