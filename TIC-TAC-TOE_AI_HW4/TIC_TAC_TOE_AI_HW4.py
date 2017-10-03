# Authors
#   Luke Mammen
#   Morgan Knoch
#
# Last Edited on 10-1-17

import os   # To clear screen

             #  0   1   2   3   4
startState = [['X',' ','X','X',' '],# 0
              ['X',' ','O','X','X'],# 1
              [' ','X','O',' ','X'],# 2
              [' ','X',' ','X',' '],# 3
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

    # Check for 2 in a rows
    checkCols( startState, 'O', 2, moves )

    print( moves )

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
    pass
# checkBoard()


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


def checkRows( board, player, orig_x, orig_y, numInARow, moves ):
    pass

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