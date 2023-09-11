# CPSC 460/560 AI project 1 - Constrained N_Queens using backtracking
#                             Constraint: 1st queen's position is fixed
# Author: your name
#
# Do not change the following part. NO other package is allowed.
import sys
import numpy as np
import pandas as pd
# ---------------------------------------------------------------


# Complete this part; add more functions if you need
# @param: initial board with the 1st queen
# @return: solution in a pandas.DataFrame
def nQueens_solver(initialBoard):
    # complete this function
    # ...
    solution = pd.DataFrame(np.zeros(initialBoard.shape))  # <--- space holder
    # solution = None  # <--- space holder for no solution case
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

