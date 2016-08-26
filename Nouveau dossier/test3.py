from random import randint
from collections import deque

board = []

for x in range(0, 10):
    board.append(["0"] * 10)

boardI = list(board)
boardI.append([0,0])
print boardI
print board

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def test(liste, z):
	if sum([1 for piece in liste[-z:] if piece[0] == liste[-z][0] or piece[1] == liste[-z][1]]) < z:
		return True
	else:
		return False

def posBoat(x, y, ship, z, boardI):
    
    try:
        if not int(boardI[x][y]):
            boardI[x][y] = "1"
            if test(ship, z):
                ship.append([x, y])
                posBoat(x, y+1, ship, z, boardI)
                posBoat(x+1, y, ship, z, boardI)
                posBoat(x, y-1, ship, z, boardI)
                posBoat(x-1, y, ship, z, boardI)
            else:
                return
        else:
            return
    except IndexError:
        return
    return ship[-z:]
            
z=5 
ship_row = random_row(board)
ship_col = random_col(board)
boardI = board[:]
print id(board)
print id(boardI)
ship = [(nombre, nombre) for nombre in range(z)]

ship = posBoat(ship_row, ship_col, ship, z, boardI)
print boardI
print board
print id(board)
print id(boardI)
##for piece in ship:
##    board[piece[0]][piece[1]] = "X"
####print ship
##print_board(board)