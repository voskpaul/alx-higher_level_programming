#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(N):
    def backtrack(board, row):
        if row == N:
            solutions.append(["".join(["Q" if cell == 1 else "." for cell in row]) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(board, row + 1)
                board[row][col] = 0

    solutions = []
    board = [[0 for _ in range(N)] for _ in range(N)]
    backtrack(board, 0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

