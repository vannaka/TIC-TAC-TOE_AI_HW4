# Authors
#   Luke Mammen
#   Morgan Knoch
#
# Last Edited on 10-1-17

import os   # To clear screen
import random

#     Col: 0   1   2   3   4    Row:
board = [[' ',' ',' ',' ',' '],# 0
         ['X','X','X','X','X'],# 1
         [' ',' ',' ',' ',' '],# 2
         ['X','X','X','X','X'],# 3
         [' ',' ',' ',' ',' '],# 4
         ['X','X','x','X','X']]# 5
# board[Row][Col]

#--------------------------------------------------------------
#
#   main()
#       Main function
#
#--------------------------------------------------------------
def main():

    printBoard( board )

    move = beginnerDecision( board, 'X' )
    print( move )

    #moves = []
    #moves = checkBoard( board, 'X' )

    #print("")
    #print("2's: ", end='')
    #print(moves[0])

    #print("3's: ", end='')
    #print(moves[1])

    #print("other's: ", end='')
    #print(moves[2])
# main()


#--------------------------------------------------------------
#
#   beginnerDecision( state )
#       Makes a random move
#
#--------------------------------------------------------------
def beginnerDecision( board, letter ):
    moves = checkBoard( board, letter )

    # Choose from 3 in a row moves
    if len(moves[1]) != 0:
        choice = random.randint( 0, len( moves[1] ) - 1 )
        return moves[1].pop(choice)
    
    # Choose from 2 in a row moves
    elif len(moves[0]) != 0:
        choice = random.randint( 0, len( moves[0] ) - 1 )
        return moves[0].pop(choice)

    # Choose from rest of moves
    else:
        choice = random.randint( 0, len( moves[2] ) - 1 )
        return moves[2].pop(choice)
# beginnerDecision()


#--------------------------------------------------------------
#
#   Class GameBoardState( state )
#       Represents the state of the game board between moves
#
#--------------------------------------------------------------
class GameBoardState( object ):
    def __init__( self, board ):
        self.board = copy.deepcopy( board )
        self.parent = None
        self.children = []
        self.minMaxVal = None
# Class GameBoardState()


#--------------------------------------------------------------
#
#   checkBoard( state, player )
#       Return three lists of x,y coordinates marking the
#       location of possible moves. The first list marks the
#       empty space at the end of 2 in a rows. The second list,
#       3 in a rows. The third list contains emptys spots not
#       in the first two lists.
#
#--------------------------------------------------------------
def checkBoard( board, player ):
    moves_2s = []
    moves_3s = []
    emptySpaces = []

    # Get two in a row moves
    checkCols( board, player, 2, moves_2s )
    checkRows( board, player, 2, moves_2s )
    checkDiags( board, player, 2, moves_2s )

    # Get three in a row moves
    checkCols( board, player, 3, moves_3s )
    checkRows( board, player, 3, moves_3s )
    checkDiags( board, player, 3, moves_3s )

    # Find all empty spaces
    for x in range( 0, len( board[0] ) ):
        for y in range( 0, len( board ) ):
            if board[y][x] == ' ':
                emptySpaces.append( (x,y) )
    
    # Find all empty spots not already in moves_2s or moves_3s
    moves_others = set(emptySpaces).difference(moves_2s)
    moves_others = moves_others.difference(moves_3s)

    return moves_2s, moves_3s, list(moves_others)
# checkBoard()


#--------------------------------------------------------------
#
#   checkCols( board, player, numInARow, moves )
#       Adds x,y pairs to the 'moves' list for empty spots at
#       the end of 'numInARow' of 'player' in the columns.
#
#--------------------------------------------------------------
def checkCols( board, player, numInARow, moves ):
    # Locals
    count = 0

    # Loop through each column
    for col in range( 0, len(board[0]) ):
        # Check column from top to bottom
        count = 0
        for row in range( 0, len(board) ):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == ' ' and count == numInARow:
                addMove( moves, col, row)
                count = 0
            else:
                count = 0

        # Check column from bottom to top
        count = 0
        for row in range( len(board) - 1, -1, -1 ):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == ' ' and count == numInARow:
                addMove( moves, col, row)
                count = 0
            else:
                count = 0
# checkCols()


#--------------------------------------------------------------
#
#   checkRows( board, player, numInARow, moves )
#       Adds x,y pairs to the 'moves' list for empty spots at
#       the end of 'numInARow' of 'player' in the rows.
#
#--------------------------------------------------------------
def checkRows( board, player, numInARow, moves ):
    # Locals
    count = 0

    # Loop through each row
    for row in range( 0, len(board) ):
        # Check row from left to right
        count = 0
        for col in range( 0, len(board[0]) ):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == ' ' and count == numInARow:
                addMove( moves, col, row)
                count = 0
            else:
                count = 0

        # Check row from right to left
        count = 0
        for col in range( len(board[0]) - 1, -1, -1 ):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == ' ' and count == numInARow:
                addMove( moves, col, row)
                count = 0
            else:
                count = 0
# checkRows()


#--------------------------------------------------------------
#
#   checkDiags( board, player, numInARow, moves )
#       Adds x,y pairs to the 'moves' list for empty spots at
#       the end of 'numInARow' of 'player' in the diaganols.
#
#--------------------------------------------------------------
def checkDiags( board, player, numInARow, moves ):
    # Locals
    count = 0
    offset = 0
    # start coordinates for the diaganols containing at least 4 spots
    # [col, row, col_mod, row_mod]
    diags_coord = [[1,0,1,1], [0,0,1,1], [0,1,1,1], [0,2,1,1],          # Top-left to bottom-right
                   [4,3,-1,-1], [4,4,-1,-1], [4,5,-1,-1], [3,5,-1,-1],  # bottom-right to top-left
                   [3,0,-1,1], [4,0,-1,1], [4,1,-1,1], [4,2,-1,1],      # Top-right to bottom-left
                   [0,3,1,-1], [0,4,1,-1], [0,5,1,-1], [1,5,1,-1]]      # Bottom-left to top-right
    

    # Loop through each diag
    for diag in range( 0, len( diags_coord ) ):
        col = diags_coord[diag][0]
        row = diags_coord[diag][1]
        col_mod = diags_coord[diag][2]
        row_mod = diags_coord[diag][3]

        # Check diag
        offset = 0
        count = 0
        while col >= 0 and col < len( board[0] ) and row >= 0 and row < len( board ):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == ' ' and count == numInARow:
                addMove( moves, col, row )
                count = 0
            else:
                count = 0

            row += row_mod
            col += col_mod
# checkDiags()


def addMove( moves, mov_x, mov_y ):
    if moves.count( (mov_x, mov_y) ) == 0:
        moves.append( (mov_x, mov_y) )
# addMoves()


#--------------------------------------------------------------
#
#   makeMove( state, player, mov_x, mov_y )
#       Checks if the space at x,y is empty and valid, then
#       places 'player' char there.
#
#--------------------------------------------------------------
def makeMove( state, player, mov_x, mov_y ):
    # The x,y cordinates are outside the range of the board
    if mov_y < 0 and mov_y >= state.len() and mov_x < 0 and mov_x >= state[0].len():
        return False

    # Check that the chosen space is empty
    if state[mov_y][mov_x] == ' ':
        state[mov_y][mov_x] = player
        return True
    else:
        return False
# makeMove()


#--------------------------------------------------------------
#
#   printBorad( state )
#       Display the board
#
#--------------------------------------------------------------
def printBoard( state ):
    # Locals
    row = 0

    # Clear screen of previous board
    _=os.system("cls")

    # Print column numbers
    print(" ", end='')
    for x in range( 0, len( state[0] ) ):
        print( " " + str(x), end='')
    print("")

    # Print board
    for y in state:
        # Print row number
        print( str(row), end='' )
        row += 1

        # Print rows
        for x in y:
            print( "|" + x, end='')
        print("|")
# printBorad()

# Call main function
main()