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
                indices.append({'key': tuple([i,j]), 'values': [0,1]})
    return indices


# Get input
def getInput():
    row, column = input().split()
    n = int(row)
    table = []
    for i in range(n):
        table.append(input().split())

    return table, n, extractEmptySpots(table)


if __name__ == '__main__':
    puzzle, n, emptySpots = getInput()
    csp = CSP()
    csp.forward_chaining(puzzle, [], emptySpots)
# list = [1,1,0,1,0,1,0,1]
# binary_puzzle = BinaryPuzzle()
# print(binary_puzzle.constraint_equal_strings(list))
# print(binary_puzzle.constraint_repetitive_strings(list))
# print(binary_puzzle.constraint_unique_strings("row","11000110"))
# print(binary_puzzle.constraint_unique_strings("column","11000110"))
