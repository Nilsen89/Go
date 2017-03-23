##RULES

from move import Move
#from group import Group

def is_legal_move(board, move):
    if not is_empty(board, move):
        return False
    if is_self_atari(board, move):
        return False
    return True

def get_neighbours(move):
    neighbours_cords = []
    for offset in range(-1, 2):
        if offset == 0:
            continue
        offset_x = move.x + offset
        offset_y = move.y + offset
        if not (offset_x < 0 and offset_x < 18):
            neighbours_cords.append(Move(offset_x, move.y, move.player))
        if not (offset_y < 0 and offset_y < 18):
            neighbours_cords.append(Move(move.x, offset_y, move.player))
    return neighbours_cords

def is_empty(board, move):
    return board.get_cell(move) == '.'

def is_self_atari(board, move):
    neighbours_cords = get_neighbours(move)
    for moves in neighbours_cords:
        if not board.get_cell(move) == move.other_player:
            return False
    return True

def kill(board, group):
    if not group.free_liberites:
        print("Dead group")

def find_group(board, move):
    
    group = [move]
    opened = [move]
    closed = []
    
    while(len(opened) > 0):
        neighbours = get_neighbours(opened[0])
        closed.append(opened.pop(0))

        for neighbour in neighbours:
            if board.get_cell(neighbour) == move.player:
                if not neighbour in closed:
                    temp_move = Move(neighbour.x, neighbour.y, move.player)
                    group.append(temp_move)
                    opened.append(temp_move)
    return Group(group, move.player)

def check_input(player_input):
    if not ":" in player_input:
        return False
    player_input = player_input.split(":")
    if player_input[0].isdigit() and player_input[0].isdigit():
        for num in range(len(player_input)):
            player_input[num] = int(player_input[num])
            if player_input[num] < 1 or player_input[num] > 19:
                return False
    return player_input
