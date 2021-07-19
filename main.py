"""
Binary Puzzle
:author Hedieh Pourghasem 9733015
:author Delaram Rajaei 9731084
"""
from CSP import CSP
from DrawPuzzle import DrawPuzzle
import time

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
    start = time.time()
    puzzle, n, empty_spot = getInput()
    conversion(puzzle, n)
    forwardChecking = False
    csp = CSP(forwardChecking)
    if forwardChecking:
        csp.forward_checking(puzzle, empty_spot)
    else:
        flag, empty_spot = csp.MAC(puzzle, empty_spot)
    answer = csp.CSP_Backtracking(puzzle, empty_spot)
    if answer is None:
        print("This puzzle can not be solved!")
    else:
        print("The answer is:")
        print_result(answer, n)
    end = time.time()
    time = end - start
    print(time)
    draw = DrawPuzzle(n, csp.stages)
    draw.draw()
