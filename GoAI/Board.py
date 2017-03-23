##AI START
import Rules

class Board(object):
    def __init__(self):
        self.board = [['.' for x in range(0,19)] for cell in range(0,19)]

    def add_move(self, move):
        if Rules.is_legal_move(self, move):
            self.board[move.x][move.y] = move.player
            return True
        else:
            print("Illegal Move")
            return False

    def set_cell(self, move, to):
        self.board[move.x][move.y] = to

    def get_cell(self, move):
        return self.board[move.x][move.y]

    def print_board(self):
        for line in self.board:
            for cell in line:
                print(cell, end=" ")
            print("")