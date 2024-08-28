#!/usr/bin/python3
'''N-Queens Challenge'''

import sys


def is_safe(placed_queens, row, col):
    """Check if a queen can be placed at (row, col)."""
    for r, c in placed_queens:
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_n_queens(n, row, placed_queens, solutions):
    """Recursive function to solve the N-Queens problem."""
    if row == n:
        solutions.append(placed_queens[:])
        return

    for col in range(n):
        if is_safe(placed_queens, row, col):
            placed_queens.append([row, col])
            solve_n_queens(n, row + 1, placed_queens, solutions)
            placed_queens.pop()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_n_queens(N, 0, [], solutions)

    for solution in solutions:
        print(solution)
