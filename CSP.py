import copy
from BinaryPuzzle import BinaryPuzzle
# import sys
#
# sys.setrecursionlimit(5000)


class CSP:

    def CSP_Backtracking(self, table=[], empty=[]):
        local_table = copy.deepcopy(table)
        local_empty = copy.deepcopy(empty)
        if len(empty) == 0 or self.check_table(table):
            return table
        var = self.MRV_heuristic(local_empty)
        for domain in var['values']:
            # clone_empty = empty[:]
            local_table[var['key'][0]][var['key'][1]] = domain
            self.print_result(local_table, len(local_table))
            result = self.forward_checking(local_table, local_empty)
            # print("global")
            # self.print_result(table, len(local_table))
            # result = self.MAC(table, empty, var['key'][0])
            if not result:
                local_table = copy.deepcopy(table)
                local_empty = copy.deepcopy(empty)
                # empty = clone_empty
                # table[var['key'][0]][var['key'][1]] = '-'
                # empty.append({'key': tuple([var['key'][0], var['key'][1]]), 'values': [0, 1]})
            else:
                result = self.CSP_Backtracking(local_table, local_empty)
                if result is not None:
                    return result
                else:
                    local_table = copy.deepcopy(table)
                    local_empty = copy.deepcopy(empty)
                #     empty.append({'key': tuple([var['key'][0], var['key'][1]]), 'values': [0, 1]})
                #     # empty = clone_empty
                #     table[var['key'][0]][var['key'][1]] = '-'
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

    def MAC(self, table, empty_spot, i):
        binaryPuzzle = BinaryPuzzle()
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

    def print_result(self, puzzle, n):
        for i in range(n):
            print(puzzle[i])
        print('\n')
