#SFG READER

class SGFReader(object):
    def __init__(self, path):
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
                    'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r',
                     's']
        self.data = self.readfile(path)
        self.moves = self.analyze(self.data)

    #Function to read the dataset files
    def readfile(self, file_path):
        data = []
        file_open = open(file_path, "r")
        for line in file_open:
            data.append(line)
        return data

    def analyze(self, data):
        moves = []
        for line in self.data:
            if ((line[0:3] == ";B[" or line[0:3] == ";W[") and line[3:4] in self.alphabet):
                x = self.alphabet.index(line[3:4])
                y = self.alphabet.index(line[4:5])
                moves.append([x, y])
        return moves