#OLD METHODS


def find_liberties(board):
    liberties = []
    for move in self.group:
        neighbours = Rules.get_neighbours(move)
        for neighbour in neighbours:
            if board.get_cell(neighbour) != self.player:
                liberties.append(neighbour)
    self.find_liberties(board)