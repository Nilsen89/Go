## Player

class Player(object):
    def __init__(self, player):
        self.player = player
        self.captures = []

    def __str__(self):
        return str(self.player)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def add_capture(self, capture):
        self.captures.append(capture)