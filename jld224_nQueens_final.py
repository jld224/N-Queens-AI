# CPSC 460/560 AI project 1 - Constrained N_Queens using backtracking
#                             Constraint: 1st queen's position is fixed
# Author: Jake Darida
#
# Do not change the following part. NO other package is allowed.
import sys
import numpy as np
import pandas as pd
# ---------------------------------------------------------------
def isSafe(board, row, col, length):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left
    for i, j in zip(range(row, length, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right
    for i, j in zip(range(row, -1, -1), range(col, length, 1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on right
    for i, j in zip(range(row, length, 1), range(col, length, 1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQueensUtil(board, row, length):
    if row == length:
        return True

    # Check if queen exists in current row
    if 1 not in board[row]:
        for col in range(length):
            if isSafe(board, row, col, length):
                board[row][col] = 1
                if solveNQueensUtil(board, row + 1, length):
                    return True
                board[row][col] = 0
    else:
        if solveNQueensUtil(board, row + 1, length):
            return True

    return False

# Complete this part; add more functions if you need
# @param: initial board with the 1st queen
# @return: solution in a pandas.DataFrame
def nQueens_solver(initialBoard):
    size = len(initialBoard)
    board = initialBoard.values.tolist()
    if not solveNQueensUtil(board, 0, size):
        return None
    return pd.DataFrame(board)


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

