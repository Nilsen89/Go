##AI START
import rules

class Board(object):
    def __init__(self):
        self.board = [['.' for x in range(0,19)] for cell in range(0,19)]

    def add_move(self, move):
        self.board[move.x][move.y] = move.player

    def set_cell(self, move, to):
        self.board[move.x][move.y] = to

    def get_cell(self, move):
        return self.board[move.x][move.y]

    def print_board(self):
        cord = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(" ", end=" ")
        for cor in cord:
            print(cor, end=" ")
        print("")
        for line in range(len(self.board)):
            print(cord[line], end=" ") 
            for cell in self.board[line]:
                print(cell, end=" ")
            print("")