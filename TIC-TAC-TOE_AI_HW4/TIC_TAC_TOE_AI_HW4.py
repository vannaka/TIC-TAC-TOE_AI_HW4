# Authors
#   Luke Mammen
#   Morgan Knoch
#
# Last Edited on 10-1-17

import os   # To clear screen

             #  0   1   2   3   4
startState = [['X','X',' ','X',' '],# 0
              ['X',' ',' ','X','X'],# 1
              [' ','X','X',' ','X'],# 2
              ['X','X','X',' ',' '],# 3
              [' ','X',' ','X','O'],# 4
              [' ',' ',' ',' ','O']]# 5

#--------------------------------------------------------------
#
#   main()
#       Main function
#
#--------------------------------------------------------------
def main():
    printBorad( startState )

    moves = []

    moves = checkBoard( startState, 'X' )

    print("")
    print( "2: ", end='')
    print( moves[0] )
    print( "3: " , end='')
    print( moves[1] )

    pass
# main()


#--------------------------------------------------------------
#
#   Class GameBoardState( state )
#       Represents the state of the game board between moves
#
#--------------------------------------------------------------
class GameBoardState( object ):
    def __init__( self, state ):
        self.boardState = copy.deepcopy( state )
        self.parent = None
        self.children = []
        self.moveCost = None

# Class GameBoardState()


#--------------------------------------------------------------
#
#   beginnerDecision( state )
#       Makes a random move
#
#--------------------------------------------------------------
def beginnerDecision( state ):
    
    pass
# beginnerDecision()


#--------------------------------------------------------------
#
#   checkBoard( state, player )
#       Return two lists of x,y coordinates marking the
#       location of possible moves. The first list marks the
#       empty space at the end of 2 in a rows. The second list,
#       3 in a rows.
#
#--------------------------------------------------------------
def checkBoard( board, player ):
    moves_2s = []
    moves_3s = []

    checkCols( board, player, 2, moves_2s )
    checkRows( board, player, 2, moves_2s )

    checkCols( board, player, 3, moves_3s )
    checkRows( board, player, 3, moves_3s )

    return moves_2s, moves_3s

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

def checkDiags( board, player, orig_x, orig_y, numInARow, moves ):
    pass

def addMove( moves, mov_x, mov_y ):
    if moves.count( [mov_x, mov_y] ) == 0:
        moves.append( [mov_x, mov_y] )
    


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
def printBorad( state ):
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