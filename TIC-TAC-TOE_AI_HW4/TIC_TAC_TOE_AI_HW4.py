# Authors
#   Luke Mammen
#   Morgan Knoch
#
# Last Edited on 10-1-17

startState = [['','','','',''],
              ['','','','',''],
              ['','','','',''],
              ['','','','',''],
              ['','','','',''],
              ['','','','','']]

#--------------------------------------------------------------
#
#   main()
#       Main function
#
#--------------------------------------------------------------
def main():
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

# Call main function
main()