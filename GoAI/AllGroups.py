#All Groups

class AllGroups(object):
    def __init__(self):
        self.groups = []
    
    def add_group(self, group):
        self.groups.append(group)
    
    def add_move_to_group(self, move, group, board):
        group.add_move(move, board)

    def move_part_of_any_group(self, move, board):
        groups = []
        player_groups = []
        other_groups = []
        for group in self.groups:
            if move in group.liberties:
                groups.append(group)
        
        if len(groups) == 0:
            return False

        for group in groups:
                if group.player == move.player:
                    player_groups.append(group)
                else:
                    other_groups.append(group)

        if len(player_groups) == 1:
            self.add_move_to_group(move, player_groups[0], board)
            return True
        elif len(player_groups) > 1:
            self.join_groups(player_groups, board, move)
            return True
        elif len(other_groups):
            for group in other_groups:
                group.update()
    
    def join_groups(self, groups, board, move):
        joined_groups = None
        for group in groups:
            if joined_groups:
                joined_groups.group.extend(group.group)
            else:
                joined_groups = group
            self.groups.remove(group)
        self.groups.append(joined_groups)
        self.add_move_to_group(move, joined_groups, board)
        
    def update(self, move, board):
        for group in self.groups:
            #Slow
            if move in group.group:
                continue
            for lib in group.free_liberties:
                if move.x == lib.x and move.y == lib.y:
                    if not group.update(board):
                        self.groups.remove(group)