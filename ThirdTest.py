# CPSC 460/560 AI project 1 - Constrained N_Queens using backtracking
# Constraint: 1st queen's position is fixed
# Author: your name
#
# Do not change the following part. NO other package is allowed.
import sys
import numpy as np
import pandas as pd

# ---------------------------------------------------------------


def promise(board, row, col):
    for i in range(row-1, -1, -1):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return False
    return True


def lcv(board, row):
    n = len(board)
    constraining_values = []
    for col in range(n):
        if promise(board, row, col):
            board[row] = col
            count = sum(not promise(board, row + 1, i) for i in range(n))
            constraining_values.append((count, col))
            board[row] = 0

    constraining_values.sort()
    return [col for _, col in constraining_values]


def solve(board, row, size, fixed_pos):
    if row == size:
        return True

    if row == fixed_pos[0]:  # If the row is the row of the fixed queen
        if promise(board, row, fixed_pos[1]):
            board[row] = fixed_pos[1]
            if solve(board, row + 1, size, fixed_pos):
                return True
            board[row] = 0
    else:
        for col in lcv(board, row):
            if promise(board, row, col):
                board[row] = col
                if solve(board, row + 1, size, fixed_pos):
                    return True
                board[row] = 0
    return False


def nQueens_solver(initialBoard):
    initial_position = initialBoard.values
    row, col = np.where(initial_position == 1)
    initial_pos = (row[0], col[0])
    board_size = len(initialBoard)
    board = [0] * board_size
    board[initial_pos[0]] = initial_pos[1]

    if not solve(board, 0, board_size, initial_pos):
        return None  # No solution case

    solution_array = np.zeros((board_size, board_size), int)
    for i in range(board_size):
        solution_array[i][board[i]] = 1

    solution = pd.DataFrame(solution_array)
    return solution

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

