# Binary Puzzle
# Authors: Hedieh Pourghasem 9733015 - Delaram Rajaei 9731084

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

