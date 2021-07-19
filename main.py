"""
Binary Puzzle
:author Hedieh Pourghasem 9733015
:author Delaram Rajaei 9731084
"""
from BinaryPuzzle import BinaryPuzzle
from CSP import CSP

"""
This function create a list of lists.
Extract all the empty spots from the puzzle. Number of rows are equal to the number of spots.  
    First value: Position of the spot in puzzle.
    Second value: Domain of values.   
"""


def extractEmptySpots(table):
    indices = []
    num = 0
    for i in range(len(table)):
        for j, elem in enumerate(table[i]):
            if '-' in elem:
                indices.append({'key': tuple([i, j]), 'values': [0, 1]})

    return indices


"""
This function get the input and create the puzzle list 
Then extract all the empty spots. 
"""


def getInput():
    row, column = input().split()
    n = int(row)
    table = []
    for i in range(n):
        table.append(input().split())

    return table, n, extractEmptySpots(table)


def checkPuzzle(puzzle):
    binary_puzzle = BinaryPuzzle()
    for i in range(len(puzzle)):
        row = puzzle[i]
        column = [row[i] for row in puzzle]
        if binary_puzzle.constraint_repetitive_strings(row, emptySpots, 'row', i):
            if binary_puzzle.constraint_repetitive_strings(column, emptySpots, 'column', i):
                return False
    return True


"""
Convert string to integer
"""


def conversion(puzzle, n):
    for i in range(n):
        for j in range(n):
            if puzzle[i][j].__eq__('1'):
                puzzle[i][j] = 1
            elif puzzle[i][j].__eq__('0'):
                puzzle[i][j] = 0


"""
Prints the result of the puzzle 
"""


def print_result(puzzle, n):
    for i in range(n):
        print(puzzle[i])


if __name__ == '__main__':
    puzzle, n, emptySpots = getInput()
    conversion(puzzle, n)
    # result = checkPuzzle(puzzle)
    csp = CSP()
    answer = csp.CSP_Backtracking(puzzle, emptySpots)
    if answer is None:
        print("This puzzle can not be solved!")
    else:
        print("The answer is:")
        print_result(puzzle, n)

# list = [1,1,0,1,0,1,0,1]
# binary_puzzle = BinaryPuzzle()
# print(binary_puzzle.constraint_equal_strings(list))
# print(binary_puzzle.constraint_repetitive_strings(list))
# print(binary_puzzle.constraint_unique_strings("row","11000110"))
# print(binary_puzzle.constraint_unique_strings("column","11000110"))
