import copy
from BinaryPuzzle import BinaryPuzzle


class CSP:
    def __init__(self, constrains):
        self.stages = []
        self.constrains_checking = constrains

    def CSP_Backtracking(self, table=[], empty=[]):
        local_table = copy.deepcopy(table)
        local_empty = copy.deepcopy(empty)
        if len(empty) == 0 or self.check_table(table):
            return table
        selected = self.MRV_heuristic(local_empty)
        for domain in selected['values']:
            local_table[selected['key'][0]][selected['key'][1]] = domain
            if self.constrains_checking:
                result = self.forward_checking(local_table, local_empty)
            else:
                result = self.MAC(table, empty, selected['key'][0])
            self.stages.append(local_table)
            self.print_result(local_table, len(local_table), local_empty)
            if not result:
                local_table = copy.deepcopy(table)
                local_empty = copy.deepcopy(empty)
            else:
                result = self.CSP_Backtracking(local_table, local_empty)
                if result is not None:
                    return result
                else:
                    local_table = copy.deepcopy(table)
                    local_empty = copy.deepcopy(empty)
                    if local_empty.__contains__(selected):
                        local_empty.remove(selected)
        return None

    def sort_function(self, e):
        return len(e['values'])

    def MRV_heuristic(self, empty=[]):
        empty.sort(key=self.sort_function)
        return empty.pop(0)

    def LCV_heuristic(self):
        return

    def forward_checking(self, table, empty_spot):
        binaryPuzzle = BinaryPuzzle()
        binaryPuzzle.clear()
        flag = True
        for i in range(len(table)):
            # Row
            # Check constrains
            row = table[i]
            res = binaryPuzzle.check_constraints(row, empty_spot, 'row', i)
            if not res:
                flag = False
            # Column
            # Check constrains
            column = [row[i] for row in table]
            res = binaryPuzzle.check_constraints(column, empty_spot, 'column', i)
            if not res:
                flag = False
        return flag

    def MAC(self, table, empty_spot, index):
        binaryPuzzle = BinaryPuzzle()
        binaryPuzzle.clear()
        changed_empty = copy.deepcopy(empty_spot)
        flag = True
        # Row
        # Check constrains
        row = table[index]
        res = binaryPuzzle.check_constraints(row, changed_empty, 'row', index)
        if not res:
            flag = False
        # Column
        # Check constrains
        column = [row[index] for row in table]
        res = binaryPuzzle.check_constraints(column, changed_empty, 'column', index)
        if not res:
            flag = False
        new_list = self.diff(empty_spot, changed_empty)
        for i in range(len(new_list)):
            # Row
            # Check constrains
            row = table[i]
            res = binaryPuzzle.check_constraints(row, new_list, 'row', i)
            if not res:
                flag = False
            # Row
            # Check constrains
            column = [row[i] for row in table]
            res = binaryPuzzle.check_constraints(column, new_list, 'column', i)
            if not res:
                flag = False
        return flag

    def check_table(self, table):
        for i in range(len(table)):
            if table[i].__contains__('-'):
                return False
        return True

    def print_result(self, puzzle, n, empty):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[i][j] == '-':
                    for k in range(len(empty)):
                        if empty[k]['key'] == (i, j):
                            print(empty[k]['values'], end='')
                else:
                    print("  ", puzzle[i][j], "   ", end='', sep='')
            print()
        print('\n')

    def diff(self, li1, li2):
        changed = copy.deepcopy(li2)
        for i in range(len(li1)):
            length = len(li2)
            for j in range(length):
                if li1[i]['key'] == li2[j]['key']:
                    if li1[i]['values'] == li2[j]['values']:
                        changed.remove(li1[i])
                    else:
                        break
        return changed
