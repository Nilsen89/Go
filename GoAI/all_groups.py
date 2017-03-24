#All Groups

from group import Group

class AllGroups(object):
    def __init__(self):
        self.groups = []
    
    """ Adds a group the collection
        of all groups.
    """
    def add_group(self, group):
        self.groups.append(group)

    """ Removes a group for the collection
        of all groups.
    """
    def remove_group(self, group):
        self.groups.remove(group)

    def move_part_of_any_group(self, move, board, player):

        groups = []
        player_groups = []
        other_groups = []
        for group in self.groups:
            for lib in group.liberties:
                if lib.x == move.x and lib.y == move.y:
                    groups.append(group)

        for group in groups:
            if group.player == move.player:
                player_groups.append(group)
            else:
                other_groups.append(group)

        if len(player_groups) == 1:
            player_groups[0].add_move(move, board)

        elif len(player_groups) > 1:
            self.join_groups(player_groups, board, move) 

        if other_groups:
            for group in other_groups:
                if not group.update(board):
                    self.remove_group(group)

        if len(player_groups) == 0:
            self.add_group(Group([move], move.player, board))

    """ Join two or more groups together,
        add the new move to the joined group.
    """
    def join_groups(self, groups, board, move):
        joined_groups = None
        for group in groups:
            if joined_groups:
                joined_groups.group.extend(group.group)
            else:
                joined_groups = group
            self.groups.remove(group)
        self.groups.append(joined_groups)
        joined_groups.add_move(move, board)