#!/usr/bin/python3
"""Solves the N-Queens puzzle using a non-recursive approach."""

from sys import argv

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)

def board_column_gen(board=[]):
    """Adds a column of zeroes to the right of the board."""
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board

def add_queen(board, row, col):
    """Places a queen (1) on the board at the given row and column."""
    board[row][col] = 1

def new_queen_safe(board, row, col):
    """Checks if a queen can be placed at the given position without conflicts."""
    for i in range(1, N):
        if (col - i) >= 0:
            if (row - i) >= 0 and board[row - i][col - i]:  # up-left diagonal
                return False
            if board[row][col - i]:  # left
                return False
            if (row + i) < N and board[row + i][col - i]:  # down-left diagonal
                return False
    return True

def coordinate_format(candidates):
    """Converts the board matrix into a list of queen positions."""
    formatted = []
    for attempt in candidates:
        result = []
        for i, row in enumerate(attempt):
            for j, col in enumerate(row):
                if col:
                    result.append([i, j])
        formatted.append(result)
    return formatted

# Initialize the candidates with the first column of zeroes
candidates = [board_column_gen()]

# Test column by column
for col in range(N):
    new_candidates = []
    for matrix in candidates:
        for row in range(N):
            if new_queen_safe(matrix, row, col):
                temp = [line[:] for line in matrix]
                add_queen(temp, row, col)
                if col < N - 1:
                    board_column_gen(temp)
                new_candidates.append(temp)
    candidates = new_candidates

# Print the results in the required format
for solution in coordinate_format(candidates):
    print(solution)

