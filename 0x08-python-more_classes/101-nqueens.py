#!/usr/bin/python3
"""
N-Queens problem solver using backtracking.
This program finds and prints all possible solutions to the
N-Queens problem.
"""


import sys


if __name__ == "__main__":
    queens = []
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)

    num = int(sys.argv[1])
    if num < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the queens list with empty positions
    for i in range(num):
        queens.append([i, None])

    def queen_exist(col_y):
        """
        Check if a queen exists in the same column (col_y) on the board.

        Args:
            col_y (int): The row number (column) to check.

        Returns:
            bool: True if a queen exists in the same column, False otherwise.
        """
        for i in range(num):
            if col_y == queens[i][1]:
                return True
        return False

    def reject_solution(row_x, col_y):
        """
        Determine whether to reject a solution based on the placemen
        of a queen.

        Args:
            row_x (int): The row where we want to place the queen.
            col_y (int): The column where we want to place the queen.

        Returns:
            bool: True if the solution is valid,
            False if it conflicts with existing queens.
        """
        if queen_exist(col_y):
            return False
        i = 0
        while i < row_x:
            if abs(queens[i][1] - col_y) == abs(i - row_x):
                return False
            i += 1
        return True

    def clear_solution(row_x):
        """
        Clear the answers from the point of failure (backtrack).

        Args:
            row_x (int): The row from which to clear the solutions.
        """
        for i in range(row_x, num):
            queens[i][1] = None

    def nqueens(row_x):
        """
        Recursively find and print all possible solutions to the
        N-Queens problem.

        Args:
            row_x (int): The current row being considered.
        """
        for i in range(num):
            clear_solution(row_x)
            if reject_solution(row_x, i):
                queens[row_x][1] = i
                if row_x == num - 1:
                    print(queens)
                else:
                    nqueens(row_x + 1)

    # Start the recursive process with the initial row (0).
    nqueens(0)
