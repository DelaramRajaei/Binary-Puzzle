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
                result, local_empty = self.MAC(local_table, local_empty)
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

    def MAC(self, table, empty_spot):
        binaryPuzzle = BinaryPuzzle()
        binaryPuzzle.clear()
        changed_empty = copy.deepcopy(empty_spot)
        unchanged = []
        flag = True
        while len(changed_empty) != 0:
            new_list = changed_empty
            self.forward_checking(table, new_list)
            new_list, temp = self.diff(changed_empty, new_list)
            unchanged.extend(temp)
            changed_empty = new_list

        return flag, unchanged

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
        new_list = []
        for i in range(len(li1)):
            length = len(li2)
            for j in range(length):
                if li1[i]['key'] == li2[j]['key']:
                    if li1[i]['values'] == li2[j]['values']:
                        changed.remove(li1[i])
                        new_list.append(li1[i])
                    else:
                        break
        return changed, new_list

    def merge(self, li1, li2):
        merrged = copy.deepcopy(li2)
        flag = False
        for i in range(len(li2)):
            length = len(li1)
            for j in range(length):
                if li1[i]['key'] == li2[j]['key']:
                    flag = True
                    if li1[i]['values'] == li2[j]['values']:
                        merrged.append(li1[i])
                    else:
                        merrged.append(li2[i])

                        break
                if not flag and j == length - 1:
                    merrged.append(li1[i])
        return merrged
