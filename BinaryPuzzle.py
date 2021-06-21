class BinaryPuzzle:
    """
        This is the constructor
    """

    def __init__(self):
        self.table_row = []
        self.table_column = []

    """
    This constraint checks if a row or column has equal number of 1's and 0's
    :param table_list Row or column of the table of puzzle
    """

    def constraint_equal_strings(self, table_list=[]):
        if table_list.count(1) == table_list.count(0):
            return True
        else:
            return False

    """
        This constraint checks if a row or column has unique string numbers.
        :param table String that shows if it is a row or column of the table of puzzle.
        :param string String number which should be checked.
    """

    def constraint_unique_strings(self, table, string):
        if table == "row":
            table_list = self.table_row
        else:
            table_list = self.table_column

        if table_list.__contains__(string):
            return False
        else:
            table_list.append(string)
            return True

    """
        This constraint checks that no number repeat more than 2 times sequentially. 
        :param table_list Row or column of the table of puzzle.
    """

    def constraint_repetitive_strings(self, table_list):
        count = 1
        # Avoid IndexError for  random_list[i+1]
        for i in range(len(table_list) - 1):
            # Check if the next number is consecutive
            if table_list[i] == table_list[i + 1]:
                count += 1
            else:
                if count > 2:
                    return False
                else:
                    count = 1

        return True
