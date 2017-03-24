#DEBUG

def set_group_numbers(board, all_groups, numbers):

    board.board = [['.' for x in range(0,19)] for cell in range(0,19)]

    if numbers:
        counter = 1
        for group in all_groups.groups:
            for move in group.group:
                board.set_cell(move, counter)
            if counter > 8: counter = 0
            counter = counter + 1
    else:
        for group in all_groups.groups:
            for move in group.group:
                board.set_cell(move, group.player)

def print_group_to_move(board, all_groups, move):
    board.board = [['.' for x in range(0,19)] for cell in range(0,19)]
    for group in all_groups.groups:
        if move in group.group:
            for move in group.group:
                board.set_cell(move, move.player)

    board.print_board()

def find_group(board, move):
    
    group = [move]
    opened = [move]
    closed = []
    
    while(len(opened) > 0):
        neighbours = analyze.get_neighbours(opened[0])
        closed.append(opened.pop(0))

        for neighbour in neighbours:
            if board.get_cell(neighbour) == move.player:
                if not neighbour in closed:
                    temp_move = Move(neighbour.x, neighbour.y, move.player)
                    group.append(temp_move)
                    opened.append(temp_move)
    return Group(group, move.player)