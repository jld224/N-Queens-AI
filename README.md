# N-Queens-AI
# N-Queens Solution Grader and Solver

## Introduction
This Python program is part of a project for CPSC460/560 AI class. The goal is to grade and solve the n-queens problem using backtracking.

## Requirements
To run the program, you will need Python 3 installed along with the pandas, numpy and sys libraries. 

## Files
* 'nQueensGrading.py' - The grading file which validates a solution for n-queens problem
* 'jld224_nQueens_final.py' - The solving file finds a solution for provided n-queens problem.

## How to use?

### Grading a solution
1. Make sure your solution .csv file and the initial board .csv file are both in the same directory as the 'nQueensGrading.py'.
2. Run the program like this: `python nQueensGrading.py [N QUEEN PROBLEM .csv FILE NAME] [SOLUTION .csv FILE NAME] `
3. Program will print the solution and check if it is valid or not, it also checks if the initial condition is met.

### Solving a problem
1. Make sure your initial board .csv file is in the same directory as the 'jld224_nQueens_final.py'.
2. Run the program like this: `python jld224_nQueens_final.py [N QUEEN PROBLEM .csv FILE NAME] `
3. If a solution is found, it is saved in the same directory as 'solution__[BOARD SIZE].csv' file.

## Program Description:
#### nQueensGrading.py
The file reads two input csv files from command line arguments which represent the board of the n-queens problem and it's solution respectively. It then checks the solution for it's validity.

#### jld224_nQueens_final.py
The file reads an input csv file from command line argument which represents the board of the n-queens problem. It uses backtracking algorithm to solve the n-queens problem and produces a valid solution. The solution is then saved in the same directory as a CSV file.

### Note:
1. The board is a square matrix storing 0s and 1s, where 1 represents the queen's position.
2. Board and Solution files are .csv formatted and do not have any headers or index. They represent the nXn board configurations.
3. Remember that the first queen's position should be fixed and is given in the problem file.