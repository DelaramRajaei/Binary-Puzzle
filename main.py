"""
Binary Puzzle
:author Hedieh Pourghasem 9733015
:author Delaram Rajaei 9731084
"""
from BinaryPuzzle import BinaryPuzzle


# Get input
def getInput():
    row, column = input().split()
    n = int(row)
    table = []
    for i in range(n):
        table.append(input().split())
    return table, n


if __name__ == '__main__':
    puzzle, n = getInput()
    # list = [1,1,0,1,0,1,0,1]
    # binary_puzzle = BinaryPuzzle()
    # print(binary_puzzle.constraint_equal_strings(list))
    # print(binary_puzzle.constraint_repetitive_strings(list))
    # print(binary_puzzle.constraint_unique_strings("row","11000110"))
    # print(binary_puzzle.constraint_unique_strings("column","11000110"))

