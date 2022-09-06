"""
Author: Mariam
Created on 1/19/2022 10:25 PM
"""
import numpy as np

print("Enter the entries row by row in a single line -separated by space- and zeros in the blank cells: ")
entries = list(map(int, input().split()))
sudoku = np.array(entries).reshape(9, 9)

def possible(row, column, guess):
    global sudoku
    for i in range(0, 9):
        if sudoku[row][i] == guess:
            return False
    for i in range(0, 9):
        if sudoku[i][column] == guess:
            return False
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0 + i][x0 + j] == guess:
                return False
    return True

def solve():
    global sudoku
    for row in range(0, 9):
        for column in range(0, 9):
            if sudoku[row][column] == 0:
                for guess in range(1, 10):
                    if possible(row, column, guess):
                        sudoku[row][column] = guess
                        solve()
                        sudoku[row][column] = 0
                return

    print(np.matrix(sudoku))


solve()