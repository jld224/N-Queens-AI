# CPSC 460/560 AI project 1 - Constrained N_Queens using backtracking
# Constraint: 1st queen's position is fixed
# Author: your name
#
# Do not change the following part. NO other package is allowed.
import sys
import numpy as np
import pandas as pd
# ---------------------------------------------------------------

def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    # base case: If all queens are placed then return true
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if isSafe(board, i, col):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solveNQUtil(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution then remove queen from board[i][col]
            board[i][col] = 0

    """ If the queen can not be placed in any row in this column col then return false """
    return False

def nQueens_solver(initialBoard):
    initial_board = initialBoard.values

    if not solveNQUtil(initial_board, 1):
        return None   # Failure to find a solution
    else:
        return pd.DataFrame(initial_board)   # Return solution as DataFrame

# No need to change the main function. Do not change output filename.
def main():
    fileName_initial_Queen_pos, = sys.argv[1:]
    print('input filename: '+fileName_initial_Queen_pos)
    input_df = pd.read_csv(fileName_initial_Queen_pos, header=None)
    #
    # solution_df is the dataframe that stores your solution to the n-Queens problem (1-queen, 0-blank)
    solution_df = nQueens_solver(input_df)
    #
    if solution_df is None:
        print("No solution!")
    else:
        output_fname = 'solution__' + str(solution_df.shape[0]) + '.csv'
        print('output file name: ' + output_fname)
        solution_df.to_csv(output_fname, sep=',', header=None, index=False)

if __name__ == '__main__':
    main()