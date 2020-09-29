#!/usr/bin/python3
'''N Queens'''


def validation(chessboard, row, column):
    '''validates current position.
    Args:
        chessboard: actual state of the game.
        row: row to validate.
        column: column to validate.
    '''
    for col in range(column):
        if (chessboard[col] == row or
                abs(chessboard[col] - row) == abs(col - column)):
            return False
    return True


def backtracking(chessboard, column):
    '''backtracking application.
    Args:
        chessboard: actual state of the game.
        column: the colum to backtrack,
    '''
    q = len(chessboard)
    if column == q:
        solution = []
        for col in range(q):
            solution.append([col, chessboard[col]])
        print(solution)
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
        q = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if q < 4:
        print("N must be at least 4")
        sys.exit(1)
    chessboard = []
    for col in range(q):
        chessboard.append(col)
    backtracking(chessboard, 0)
