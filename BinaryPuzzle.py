class BinaryPuzzle:
    """
    This is the constructor.
    """

    def __init__(self):
        self.table_row = []
        self.table_column = []

    """
    Clear all the lists.
    """

    def clear(self):
        self.table_row.clear()
        self.table_column.clear()

    """
    Check all the constraints for rows or columns. 
    """

    def check_constraints(self, table, empty, position, number):
        # Equal number of 0 and 1
        if self.constraint_equal_strings(table, empty, position, number):
            # Repetitive of less than two, 1 or 0
            if self.constraint_repetitive_strings(table, empty, position, number):
                # Uniqueness of strings
                if self.constraint_unique_strings(table, empty, position, number):
                    return True
        return False

    """
    This constraint checks if a row or column has equal number of 1's and 0's
    :param table_list Row or column of the table of puzzle
    """

    def constraint_equal_strings(self, table_list, empty, position, number):
        count = table_list.count('-')
        count1 = table_list.count(1)
        count0 = table_list.count(0)
        if count >= 2:
            return True
        elif count == 1:
            if count0 == count1 or abs(count0 - count1) > 1:
                return False
            elif count0 - count1 > 0:
                self.remove_variable(empty, 0, position, table_list.index('-'), number)
                return True
            else:
                self.remove_variable(empty, 1, position, table_list.index('-'), number)
                return True
        elif count0 == count1:
            return True
        else:
            return False

    """
    This constraint checks if a row or column has unique string numbers.
    :param table String that shows if it is a row or column of the table of puzzle.
    :param string String number which should be checked.
    """

    def constraint_unique_strings(self, string, empty, vector_name, number):
        if vector_name == 'row':
            table_list = self.table_row
        else:
            table_list = self.table_column

        if table_list.__contains__(string):
            return False
        else:
            if not string.__contains__('-'):
                table_list.append(string)
                return True
            elif string.count('-') == 1:
                index = string.index('-')
                for i in range(len(table_list)):
                    # TODO
                    if self.is_edit_distance_one(table_list[i], string):
                        var = table_list[index]
                        self.remove_variable(empty, var, vector_name, i, number)
        return True

    """
        This constraint checks that no number repeat more than 2 times sequentially. 
        :param table_list Row or column of the table of puzzle.
    """

    def constraint_repetitive_strings(self, table_list, empty, position, number):
        count = 1
        # Avoid IndexError for  random_list[i+1]
        for i in range(len(table_list) - 1):
            # Check if the next number is consecutive
            if table_list[i] is '-':
                continue
            elif table_list[i] == table_list[i + 1]:
                count += 1
            else:
                if count > 2:
                    return False
                elif count == 2:
                    if i + 1 != len(table_list) - 1:
                        if table_list[i + 1] is '-':
                            self.remove_variable(empty, table_list[i], position, i + 1, number)
                    if i - count > 0:
                        if table_list[i - count] is '-':
                            self.remove_variable(empty, table_list[i], position, i - count, number)
                count = 1
        return True

    def check_puzzle(self, table_list):
        count = 1
        # Avoid IndexError for  random_list[i+1]
        for i in range(len(table_list) - 1):
            # Check if the next number is consecutive
            if table_list[i] is '-':
                continue
            elif table_list[i] == table_list[i + 1]:
                count += 1
            else:
                if count > 2:
                    return False
                else:
                    count = 1

        return True

    def remove_variable(self, empty, var, position, i, j):
        if position == 'row':
            row = j
            col = i
        else:
            row = i
            col = j

        for spot in range(len(empty)):
            if empty[spot]['key'] == (int(row), int(col)):
                if empty[spot]['values'].__contains__(var):
                    empty[spot]['values'].remove(var)
                    return

    def is_edit_distance_one(self, s1, s2):
        # Find lengths of given strings
        m = len(s1)
        n = len(s2)

        # If difference between lengths is more than 1,
        # then strings can't be at one distance
        if abs(m - n) > 1:
            return False

        count = 0  # Count of isEditDistanceOne

        i = 0
        j = 0
        while i < m and j < n:
            # If current characters dont match
            if s1[i] != s2[j]:
                if count == 1:
                    return False

                # If length of one string is
                # more, then only possible edit
                # is to remove a character
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:  # If lengths of both strings is same
                    i += 1
                    j += 1

                # Increment count of edits
                count += 1

            else:  # if current characters match
                i += 1
                j += 1

        # if last character is extra in any string
        if i < m or j < n:
            count += 1

        return count == 1
