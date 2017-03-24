#SFG READER

class SGFReader(object):
    def __init__(self, path):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
                         'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r','s']
        self.data = self.readfile(path)
        self.moves = self.analyze(self.data)

    """ Read the file and store in data array.
    """
    def readfile(self, file_path):
        data = []
        file_open = open(file_path, "r")
        for line in file_open:
            data.append(line)
        return data

    """ Analyze the data, and get moves.
    """
    def analyze(self, data):
        moves = []
        for line in self.data:
            if ((line[0:3] == ";B[" or line[0:3] == ";W[") and line[3:4] in self.alphabet):
                x = self.alphabet.index(line[3:4])
                y = self.alphabet.index(line[4:5])
                moves.append([x, y])
        return moves