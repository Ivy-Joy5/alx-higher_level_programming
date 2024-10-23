#!/usr/bin/python3
"""Solves the N Queens problem."""
import sys


def print_solution(solution):
    """Prints the board's solution in the required format."""
    formatted_solution = []
    for i in range(len(solution)):
        formatted_solution.append([i, solution[i]])
    print(formatted_solution)


def is_safe(board, row, col, N):
    """Checks if it's safe to place a queen at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row] == i:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i] == j:
            return False

    return True


def solve_nqueens_util(board, col, N):
    """Utilizes backtracking to find all solutions."""
    if col == N:
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i] = col
            solve_nqueens_util(board, col + 1, N)
            board[i] = -1  # Backtrack


def solve_nqueens(N):
    """Solves the N Queens problem using backtracking."""
    board = [-1] * N
    solve_nqueens_util(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
