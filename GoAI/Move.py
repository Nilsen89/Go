##Move

class Move(object):
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        if player == 'X': self.other_player = 'O'
        else: self.other_player = 'X'

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__