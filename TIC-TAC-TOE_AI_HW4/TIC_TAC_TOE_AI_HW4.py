# Authors
#   Luke Mammen
#   Morgan Knoch
#
# Last Edited on 10-1-17

import os   # To clear screen

             #  0   1   2   3   4
startState = [['X',' ',' ',' ',' '],# 0
              [' ','X',' ',' ',' '],# 1
              [' ',' ',' ',' ',' '],# 2
              [' ',' ',' ','X',' '],# 3
              [' ',' ',' ',' ','O'],# 4
              [' ',' ',' ',' ',' ']]# 5

#--------------------------------------------------------------
#
#   main()
#       Main function
#
#--------------------------------------------------------------
def main():
    printBorad( startState )
    res = makeMove( startState, 'O', 1, 1)
    printBorad( startState )
    print( res )
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