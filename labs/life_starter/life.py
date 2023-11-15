#
# life.py - Game of Life lab
#
# Name: Daniel Detore
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    """ takes w and h, both integers.
    returns a board of size w * h full of live cells ("1")
    except for a 1-cell border of dead cells ("0").
    """
    L = createBoard(w, h)
    for i in range(1,w-1):
        for j in range(1,h-1):
            L[i][j] = 1
    return L

def randomCells(w,h):
    """ creates a board of random cells (except for a 1-cell border
    of dead cells) with dimensions w*h.
    """
    L = createBoard(w, h)
    for i in range(1,w-1):
        for j in range(1,h-1):
            L[i][j] = random.choice([0,1])
    return L

def copy(A):
    """ creates and returns a deep copy of board A. """
    w = len(A[0])
    h = len(A)
    L = createBoard(w, h)
    for i in range(w):
        for j in range(h):
            L[i][j] = A[i][j]
    return L

def innerReverse(A):
    """ creates a copy of board A and
    inverts the new board's inner cells.
    """
    L = copy(A)
    w = len(L[0])
    h = len(L)
    for i in range(1,w-1):
        for j in range(1,h-1):
            if L[i][j] == 0:
                L[i][j] = 1
            elif L[i][j] == 1:
                L[i][j] = 0
    return L

def next_life_generation(A):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    def countLiveNeighbors(x,y,board):
        sum = 0
        for i in range(-1,2):
            sum += board[x+i][y-1]
        for i in range(-1,2,2):
            sum += board[x+i][y]
        for i in range(-1,2):
            sum += board[x+i][y+1]
        return sum
    newA = copy(A)
    w = len(newA[0])
    h = len(newA)
    for i in range(1,w-1):
        for j in range(1,h-1):
            neighbors = countLiveNeighbors(i,j,A)
            if A[i][j] == 1:
                if neighbors < 2:
                    newA[i][j] = 0
                elif neighbors > 3:
                    newA[i][j] = 0
            elif A[i][j] == 0 and neighbors == 3:
                newA[i][j] = 1
    return newA