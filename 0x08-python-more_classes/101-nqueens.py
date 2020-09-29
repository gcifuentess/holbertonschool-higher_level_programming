#!/usr/bin/python3
'''N Queens'''


def validation(chessboard, row, column):
    '''validates current possition.
    Args:
        chessboard: actual state of the game.
        row: row to validate.
        column: column to validate.
    '''
    for col in range(column):
        if chessboard[col] == row
        or abs(chessboard[col] - row) == abs(col - column):
            return False
    return True


def backtracking(chessboard, column):
    '''backtracking application.
    Args:
        chessboard: actual state of the game.
        column: the colum to backtrack,
    '''
    q = len(chesboard)
    if column is q:
        for col in range(q):
            print(str([[col, chessboard[col]])
        return

    for row in range(q):
        if validation(chessboard, row, column):
            chessboard[column] = row
            backtracking(chessboard, column + 1)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    q = 0
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    chessboard = []
    for col in range(q):
        chessboard.append[col]
    backtracking(chessboard, 0)
