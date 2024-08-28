#!/usr/bin/python3
'''N-Queens Challenge'''

import sys


def is_safe(placed_queens, r, c):
    """Check if the position (r, c) is safe for placing a queen."""
    for row, col in placed_queens:
        if col == c or abs(col - c) == abs(row - r):
            return False
    return True


def solve_n_queens(n):
    """Solve the N-Queens problem and return all solutions."""
    solutions = []
    placed_queens = []
    r, c = 0, 0

    while r < n:
        goback = False
        while c < n:
            if is_safe(placed_queens, r, c):
                placed_queens.append([r, c])
                if r == n - 1:
                    solutions.append(placed_queens[:])
                    goback = True
                else:
                    r += 1
                    c = 0
                    break
            c += 1

        if goback or c == n:
            if not placed_queens:
                break
            r, c = placed_queens.pop()
            c += 1
            if r == 0 and c == n:
                break

    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)
