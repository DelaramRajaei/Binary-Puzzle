import numpy as np
from BinaryPuzzle import BinaryPuzzle


# Heuristics

class CSP:
    def __init__(self, puzzle, empty):
        self.binary_puzzle = BinaryPuzzle()
        self.puzzle = puzzle
        self.empty = empty

    def sortFunc(self, e):
        return len(e['values'])

    def MRV_heuristic(self, cp):
        while len(self.empty) > 0:
            self.empty.sort(key=self.sortFunc)
            row = self.puzzle[self.empty[0]['key'][0]]
            column = [row[self.empty[0]['key'][1]] for row in self.puzzle]
            if cp:
                self.forward_chaining()
            else:
                self.MAC()
            # print(empty)
            # empty[1]['values'] = [0,1,2]
            # empty[4]['values'] = [1]
            # empty[0]['values'] = []
        return

    def LCV_heuristic(self):
        return

    def forward_chaining(self):
        for i in enumerate(self.empty):

        return

    def MAC(self):
        return
