#!/Users/aecolumna908/anaconda3/bin/python

# inspired by Peter Norvig & Stuart Russel's book on Artificial Intelligence.

import sys

# Deal with input from Mathematica
args = sys.argv[1:]
astring = args[0]
slist = [int(i) for i in astring]

# Assemble into board
board = []

for i in range(0,len(slist),9):
    board.append(slist[i:i+9])

# Define Constraints
def sec_row(row):
    x = (row // 3) * 3
    assert (x <= 9), "Row is out of bounds!"
    return x
def sec_col(col):
    x = (col // 3) * 3
    assert (x <= 9), "Col is out of bounds!"
    return x
def check_section(row, col, board):
    num = board[row][col]
    assert (num != 0)

    toprow = sec_row(row)
    topcol = sec_col(col)

    for i in range(toprow, toprow + 3):
        for j in range(topcol, topcol + 3):
            if board[i][j] == num and i != row and j != col:
                return False

    return True
def check_conflicts(row, col, board):
    num = board[row][col]
    dim = len(board)

    if num == 0:
        return True

    # check row
    for j in range(dim):
        if board[row][j] == num and j != col:
            return False

    # check column
    for i in range(dim):
        if board[i][col] == num and i != row:
            return False

    # check region.
    # find closest top-left region square!
    return True if check_section(row, col, board) == True else False
def findNext(board):
    row = board[0]
    dim = len(board[0])
    
    for i in range(dim):
        for j in range(dim):
            if board[i][j] == 0:
                return i,j
    return -1,-1 # all squares filled by non-zeros
def solveSudoku(board):
    
    i, j = findNext(board)
    
    if i == -1:
        return True
    
    for val in range(1,10):
        board[i][j] = val
        if check_conflicts(i, j, board):
            if solveSudoku(board):
                return True
    else:
        board[i][j] = 0
        
    return False      
    
solveSudoku(board)

lst = []

for i in range(9):
    for j in range(9):
        lst.append(board[i][j])
  
  
print("hello, World")
lststr = str(lst)     
lststr.replace("[","{").replace("]","}")
print(lststr)




