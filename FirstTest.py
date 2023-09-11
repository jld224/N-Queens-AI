# CPSC 460/560 AI project 1 - Constrained N_Queens using backtracking
#                             Constraint: 1st queen's position is fixed
# Author: your name
#
# Do not change the following part. NO other package is allowed.
import sys
import numpy as np
import pandas as pd

# ---------------------------------------------------------------


# Helper function to check if a position is safe
def is_valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# Function that uses recursion and backtracking to solve the problem
def solve_nQueens(board, col):
    if col == len(board):
        return True

    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            if solve_nQueens(board, col + 1):
                return True
            board[i][col] = 0  # backtrack

    return False

#this is a test to test how github is working
# Complete this part; add more functions if you need
def nQueens_solver(input_df):
    initialBoard = input_df.to_numpy()
    if not solve_nQueens(initialBoard, 0):
        return None

    solution = pd.DataFrame(initialBoard)
    return solution


# No need to change the main function. Do not change output filename.
def main():
    (fileName_initial_Queen_pos,) = sys.argv[1:]
    print("input filename: " + fileName_initial_Queen_pos)
    input_df = pd.read_csv(fileName_initial_Queen_pos, header=None)
    solution_df = nQueens_solver(input_df)
    #
    if solution_df is None:
        print("No solution!")
    else:
        output_fname = "solution__" + str(solution_df.shape[0]) + ".csv"
        print("output file name: " + output_fname)
        solution_df.to_csv(output_fname, sep=",", header=None, index=False)


if __name__ == "__main__":
    main()
