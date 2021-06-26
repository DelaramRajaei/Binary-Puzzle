import numpy as np
from BinaryPuzzle import BinaryPuzzle


class CSP:
    def __init__(self, empty):
        self.binary_puzzle = BinaryPuzzle()
        self.empty = empty

    def sortFunc(self, e):
        return len(e['values'])

    def MRV_heuristic(self, filled, empty):
        empty.sort(key=self.sortFunc)
        filled.append = empty[0]
        empty.pop(0)
        return filled, empty

        # row = self.puzzle[self.empty[0]['key'][0]]
        # column = [row[self.empty[0]['key'][1]] for row in self.puzzle]
        # print(empty)
        # empty[1]['values'] = [0,1,2]
        # empty[4]['values'] = [1]
        # empty[0]['values'] = []

    def LCV_heuristic(self):
        return

    def forward_chaining(self, table, filled, empty):
        if len(empty) == 0:
            return self.binary_puzzle.check_constraints(table)

        filled, empty = self.MRV_heuristic(filled, empty)
        while len(empty[0]['values']) > 0:
            i = empty[0]['key'][0]
            j = empty[0]['key'][1]
            values = empty[0]['values']
            table[i][j] = values[0]
            flag = self.forward_chaining(table, filled, empty)
            if flag:
                return True
            else:
                values.pop(0)
        return False

    def MAC(self):
        return
