import numpy as np
from BinaryPuzzle import BinaryPuzzle


class CSP:

    def CSP_Backtracking(self, table=[], empty=[]):
        if len(empty) == 0 or self.check_table(table):
            return table
        var = self.MRV_heuristic(empty)
        for domain in var['values']:
            table[var['key'][0]][var['key'][1]] = domain
            result = self.forward_checking(table, empty)
            if not result:
                table[var['key'][0]][var['key'][1]] = '-'
                empty.append({'key': tuple([var['key'][0], var['key'][1]]), 'values': [0, 1]})
            else:
                result = self.CSP_Backtracking(table, empty)
                if result is not None:
                    return result
        return None

    def sort_function(self, e):
        return len(e['values'])

    def MRV_heuristic(self, empty=[]):
        empty.sort(key=self.sort_function)
        return empty.pop(0)
        # row = self.puzzle[self.empty[0]['key'][0]]
        # column = [row[self.empty[0]['key'][1]] for row in self.puzzle]
        # print(empty)
        # empty[1]['values'] = [0,1,2]
        # empty[4]['values'] = [1]
        # empty[0]['values'] = []

    def LCV_heuristic(self):
        return

    def forward_checking(self, table, empty_spot):
        binaryPuzzle = BinaryPuzzle()
        for i in range(len(table)):
            # Row
            # Check constrains
            row = table[i]
            if not binaryPuzzle.check_constraints(row, empty_spot, 'row', i):
                return False
            # Row
            # Check constrains
            column = [row[i] for row in table]
            if not binaryPuzzle.check_constraints(column, empty_spot, 'column', i):
                return False
        return True

    def MAC(self):
        return

    def clone(self, table):
        new_table = []
        new_table.extend(table)
        return new_table

    def check_table(self, table):
        for i in range(len(table)):
            if table[i].__contains__('-'):
                return False
        return True
