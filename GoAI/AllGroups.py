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
        for group in self.groups:
            if move in group.liberties and move.player == group.player:
                groups.append(group)

        if len(groups) == 1:
            self.add_move_to_group(move, groups[0], board)
            return True
        elif len(groups) == 0:
            return False
        else:
            self.join_groups(groups, board)
    
    def join_groups(self, groups, board):
        joined_groups = None
        for group in groups:
            if joined_groups:
                joined_groups.group.extend(group.group)
            else:
                joined_groups = group
            print(len(self.groups))
            self.groups.remove(group)
            print(len(self.groups))
        joined_groups.update(board)
        self.groups.append(joined_groups)
        

    def update(self, move, board):
        for group in self.groups:
            #Slow
            if move in group.group:
                continue
            for lib in group.free_liberties:
                if move.x == lib.x and move.y == lib.y:
                    if not group.update(board):
                        self.groups.remove(group)