#!/usr/bin/python3
"""Solves the N-Queens puzzle using a non-recursive approach."""

import sys

def print_usage_and_exit():
    """Prints the usage message and exits."""
    print('Usage: nqueens N')
    exit(1)

def is_number(n):
    """Check if n is a number."""
    try:
        int(n)
        return True
    except ValueError:
        return False

def board_column_gen(N, board=[]):
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

def new_queen_safe(board, row, col, N):
    """Checks if a queen can be placed at the given position without conflicts."""
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
        if (row - i >= 0 and col - i >= 0 and board[row - i][col - i] == 1) or \
           (row + i < N and col + i < N and board[row + i][col + i] == 1) or \
           (row - i >= 0 and col + i < N and board[row - i][col + i] == 1) or \
           (row + i < N and col - i >= 0 and board[row + i][col - i] == 1):
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

# Main program logic
if len(sys.argv) != 2:
    print_usage_and_exit()

if not is_number(sys.argv[1]):
    print('N must be a number')
    exit(1)

N = int(sys.argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)

# Initialize the candidates with the first column of zeroes
candidates = [board_column_gen(N)]

# Test column by column
for col in range(N):
    new_candidates = []
    for matrix in candidates:
        for row in range(N):
            if new_queen_safe(matrix, row, col, N):
                temp = [line[:] for line in matrix]
                add_queen(temp, row, col)
                if col < N - 1:
                    board_column_gen(N, temp)
                new_candidates.append(temp)
    candidates = new_candidates

# Print the results in the required format
for solution in coordinate_format(candidates):
    print(solution)

