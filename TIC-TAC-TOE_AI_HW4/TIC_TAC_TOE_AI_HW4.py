# Authors
#   Luke Mammen
#   Morgan Knoch
#
# Last Edited on 10-1-17

import os   # To clear screen
import random
import copy
import sys
import time
import pprint

#     Col: 0   1   2   3   4    Row:
board = [[' ',' ',' ',' ',' '],# 0
         [' ',' ',' ',' ',' '],# 1
         [' ',' ',' ',' ',' '],# 2
         [' ',' ',' ',' ',' '],# 3
         [' ',' ',' ',' ',' '],# 4
         [' ',' ',' ',' ',' ']]# 5
# board[Row][Col]
checkWin = 0
moveCount = 0
numNodesGen = 0
beginWins = 0
advancedWins = 0
masterWins = 0
beginvsmasterTie = 0
#--------------------------------------------------------------
#
#   Class boardNode( gameboard )
#       Represents the state of the game board between moves
#
#--------------------------------------------------------------
class boardNode(object):
    
    def __init__(self, gameboard):
        self.gameboard = copy.deepcopy(gameboard)
        self.value = 0
        self.parent = None
        self.move = None

def beginplay():
    global moveCount
    pp = pprint.PrettyPrinter()
    # Beginner is X's, User is O's
    while checkWinner(board, 'X', 'O') == 0:
        # Beginner's move
        move = beginnerDecision(board, 'X')
        board[move[1]][move[0]] = 'X'
        
        if moveCount < 8:
            pp.pprint(board)
        
        X = input('Enter the row index: ')
        Y = input('Enter the col index: ')
        
        X = int(X)
        Y = int(Y)

        # col, row
        board[X][Y] = 'O'

        if moveCount < 8:
            pp.pprint(board)
            moveCount += 1        

    pp.pprint(board)
    print('The winner is: {0}'.format(checkWinner(board, 'X', 'O')))
    

#--------------------------------------------------------------
#
#   advancedplay()
#       Main function for advanced vs. beginner
#
#--------------------------------------------------------------
def advancedplay():
    global moveCount, numNodesGen, board

    pp = pprint.PrettyPrinter()
    # Beginner is X's, User is O's
    while checkWinner(board, 'X', 'O') == 0:
        # Beginner's move
        move = beginnerDecision(board, 'X')
        board[move[1]][move[0]] = 'X'
        
        if checkWinner(board, 'X', 'O') != 0:
            break

        if moveCount < 8:
            pp.pprint(board)
        
        # Advanced's move
        numNodesGen = 0 
        start_time = time.time()
        newboard = advancedDecision( board, 'O', 'X', 2 )
        #newboard = newboard.parent
        end_time = time.time() - start_time
        end_time = end_time * 1000                # Convert time in seconds to milliseconds
        board = copy.deepcopy(newboard.gameboard)

        if moveCount < 8:
            pp.pprint(board)
            moveCount += 1   

        print('Number of nodes generated: {0}'.format(numNodesGen))
        print("CPU execution time: " + str(end_time) + " ms")    

    pp.pprint(board)

    winner = checkWinner(board, 'X', 'O')
    
    if winner == 'X':
        print_winner = 'Beginner'
    elif winner == 'O':
        print_winner = 'Advanced'

    print('The winner is: {0}'.format(print_winner))
# advancedplay()

#--------------------------------------------------------------
#
#   masterplay()
#       Main function for advanced vs. master
#
#--------------------------------------------------------------
def masterplay():
    global moveCount, numNodesGen, board

    pp = pprint.PrettyPrinter()
    # Beginner is X's, User is O's
    while checkWinner(board, 'X', 'O') == 0:
        # Advanced's move
        numNodesGen = 0 
        start_time = time.time()
        newboard = advancedDecision( board, 'X', 'O', 2 )
        end_time = time.time() - start_time
        end_time = end_time * 1000                # Convert time in seconds to milliseconds
        board = copy.deepcopy(newboard.gameboard)
        
        if checkWinner(board, 'X', 'O') != 0:
            break

        if moveCount < 8:
            pp.pprint(board)
        print('Number of nodes generated: {0}'.format(numNodesGen))
        print("CPU execution time: " + str(end_time) + " ms")  

        # Advanced's move
        numNodesGen = 0 
        start_time = time.time()
        newboard = masterDecision( board, 'O', 'X', 4 )
        newboard = newboard.parent
        newboard = newboard.parent
        end_time = time.time() - start_time
        end_time = end_time * 1000                # Convert time in seconds to milliseconds
        board = copy.deepcopy(newboard.gameboard)

        if moveCount < 8:
            pp.pprint(board)
            moveCount += 1   

        print('Number of nodes generated: {0}'.format(numNodesGen))
        print("CPU execution time: " + str(end_time) + " ms")    

    pp.pprint(board)

    winner = checkWinner(board, 'X', 'O')
    
    if winner == 'X':
        print_winner = 'Advanced'
    elif winner == 'O':
        print_winner = 'Master'

    print('The winner is: {0}'.format(print_winner))
# masterplay()


def beginnerVsAdvacedPlay():
    global moveCount, numNodesGen, board, beginWins, advancedWins, beginvsmasterTie

    board = [[' ',' ',' ',' ',' '],# 0
         [' ',' ',' ',' ',' '],# 1
         [' ',' ',' ',' ',' '],# 2
         [' ',' ',' ',' ',' '],# 3
         [' ',' ',' ',' ',' '],# 4
         [' ',' ',' ',' ',' ']]# 5

    pp = pprint.PrettyPrinter()
    # Beginner is X's, User is O's
    while checkWinner(board, 'X', 'O') == 0:
        # Beginner's move
        move = beginnerDecision(board, 'X')
        board[move[1]][move[0]] = 'X'
        
        if checkWinner(board, 'X', 'O') != 0:
            break

        # Master's move
        numNodesGen = 0 
        newboard = masterDecision( board, 'O', 'X', 2 )
        newboard = newboard.parent
        newboard = newboard.parent              # Convert time in seconds to milliseconds
        board = copy.deepcopy(newboard.gameboard)
 
        
        moves = checkBoard(board, 'X')
        if moves[3] is None:
            beginvsmasterTie += 1
            break
    pp.pprint(board)

    winner = checkWinner(board, 'X', 'O')
    
    if winner == 'X':
        print_winner = 'Beginner'
        beginWins += 1
    elif winner == 'O':
        print_winner = 'Advanced'
        masterWins +=1
    else:
        print_winner = 'Tie'

    print('The winner is: {0}'.format(print_winner))
# beginnerVsAdvacedPlay()


def advancedVsBeginnerplay():
    global moveCount, numNodesGen, board, beginWins, masterWins, beginvsmasterTie

    board = [[' ',' ',' ',' ',' '],# 0
         [' ',' ',' ',' ',' '],# 1
         [' ',' ',' ',' ',' '],# 2
         [' ',' ',' ',' ',' '],# 3
         [' ',' ',' ',' ',' '],# 4
         [' ',' ',' ',' ',' ']]# 5

    pp = pprint.PrettyPrinter()
    # Beginner is X's, User is O's
    while checkWinner(board, 'X', 'O') == 0:
        # Beginner's move

        # Advanced's move
        numNodesGen = 0 
        newboard = masterDecision( board, 'X', 'O', 2 )
        newboard = newboard.parent
        newboard = newboard.parent              # Convert time in seconds to milliseconds
        board = copy.deepcopy(newboard.gameboard)
        
        if checkWinner(board, 'X', 'O') != 0:
            break

        move = beginnerDecision(board, 'O')
        board[move[1]][move[0]] = 'O'
    
        moves = checkBoard(board, 'X')
        if moves[3] is None:
            beginvsmasterTie += 1
            break

    pp.pprint(board)

    winner = checkWinner(board, 'X', 'O')
    
    if winner == 'O':
        print_winner = 'Beginner'
        beginWins += 1
    elif winner == 'X':
        print_winner = 'Advanced'
        masterWins +=1
    else:
        print_winner = 'Tie'

    print('The winner is: {0}'.format(print_winner))
# advancedVsBeginnerplay()


def beginnervsmasterplay():
    global moveCount, numNodesGen, board, beginWins, masterWins, beginvsmasterTie

    board = [[' ',' ',' ',' ',' '],# 0
         [' ',' ',' ',' ',' '],# 1
         [' ',' ',' ',' ',' '],# 2
         [' ',' ',' ',' ',' '],# 3
         [' ',' ',' ',' ',' '],# 4
         [' ',' ',' ',' ',' ']]# 5

    pp = pprint.PrettyPrinter()
    # Beginner is X's, User is O's
    while checkWinner(board, 'X', 'O') == 0:
        # Beginner's move
        move = beginnerDecision(board, 'X')
        board[move[1]][move[0]] = 'X'
        
        if checkWinner(board, 'X', 'O') != 0:
            break

        # Master's move
        numNodesGen = 0 
        newboard = masterDecision( board, 'O', 'X', 4 )
        newboard = newboard.parent
        newboard = newboard.parent              # Convert time in seconds to milliseconds
        board = copy.deepcopy(newboard.gameboard)
 
        
        moves = checkBoard(board, 'X')
        if moves[3] is None:
            beginvsmasterTie += 1
            break
    pp.pprint(board)

    winner = checkWinner(board, 'X', 'O')
    
    if winner == 'X':
        print_winner = 'Beginner'
        beginWins += 1
    elif winner == 'O':
        print_winner = 'Master'
        masterWins +=1
    else:
        print_winner = 'Tie'

    print('The winner is: {0}'.format(print_winner))
# masterplay()

def mastervsbeginnerplay():
    global moveCount, numNodesGen, board, beginWins, masterWins, beginvsmasterTie

    board = [[' ',' ',' ',' ',' '],# 0
         [' ',' ',' ',' ',' '],# 1
         [' ',' ',' ',' ',' '],# 2
         [' ',' ',' ',' ',' '],# 3
         [' ',' ',' ',' ',' '],# 4
         [' ',' ',' ',' ',' ']]# 5

    pp = pprint.PrettyPrinter()
    # Beginner is X's, User is O's
    while checkWinner(board, 'X', 'O') == 0:
        # Beginner's move

        # Master's move
        numNodesGen = 0 
        newboard = masterDecision( board, 'X', 'O', 4 )
        newboard = newboard.parent
        newboard = newboard.parent              # Convert time in seconds to milliseconds
        board = copy.deepcopy(newboard.gameboard)
        
        if checkWinner(board, 'X', 'O') != 0:
            break

        move = beginnerDecision(board, 'O')
        board[move[1]][move[0]] = 'O'
    
        moves = checkBoard(board, 'X')
        if moves[3] is None:
            beginvsmasterTie += 1
            break

    pp.pprint(board)

    winner = checkWinner(board, 'X', 'O')
    
    if winner == 'O':
        print_winner = 'Beginner'
        beginWins += 1
    elif winner == 'X':
        print_winner = 'Master'
        masterWins +=1
    else:
        print_winner = 'Tie'

    print('The winner is: {0}'.format(print_winner))
# masterplay()



#--------------------------------------------------------------
#
#   beginnerDecision( board, letter )
#       Makes a random move
#
#--------------------------------------------------------------
def beginnerDecision( board, letter ): # Modify so that it blocks when opponent has 3 in a row
    moves = checkBoard( board, letter )

    # Choose from 3 in a row moves
    if len(moves[1]) != 0:
        choice = random.randint( 0, len( moves[1] ) - 1 )
        return moves[1].pop(choice)
    
    # Choose from 2 in a row moves
    elif len(moves[5]) != 0:
        choice = random.randint( 0, len( moves[5] ) - 1 )
        return moves[5].pop(choice)

    # Choose from rest of moves
    else:
        choice = random.randint( 0, len( moves[3] ) - 1 )
        return moves[3].pop(choice)
# beginnerDecision()

#--------------------------------------------------------------
#
#   advacedDecision( board, letter )
#       Uses min-max to make a move decision
#
#--------------------------------------------------------------
def advancedDecision( board, player1, player2, ply ):
    return minMaxDecision( board, player1, player2, ply )
# advacedDecision()

#--------------------------------------------------------------
#
#   masterDecision( board, letter )
#       Uses min-max to make a move decision
#
#--------------------------------------------------------------
def masterDecision( board, player1, player2, ply ):
    return minMaxDecision( board, player1, player2, ply )
# masterDecision()

#--------------------------------------------------------------
#
#   minMaxDecision( board, player, ply )
#       Constructs a min-max tree with the given 'ply' and
#       returns the gameboard with best move for 'player'.
#
#--------------------------------------------------------------
def minMaxDecision( board, player1, player2, ply ):
    # return the state with the maximum min value
    level = ply
    gameboard = boardNode(board)
    return max_value( level, gameboard, player1, player2)
# minMaxDecision()


#--------------------------------------------------------------
#
#   max_value(level, gameboard, player1, player2)
#       Helper function that finds the maximum nodes in the
#       minimax tree. Returns the maximum scoring gameboard 
#       object.
#
#--------------------------------------------------------------
def max_value(level, gameboard, player1, player2):
    if checkWinner(gameboard.gameboard, player1, player2) == player1:
        gameboard.value = 1000000000
    if level == 0:
        return None 
    value = -1000000000

    if gameboard is not None:
        for node in findSuccessors(gameboard, player1):
            max_node = min_value(level-1, node, player1, player2)
            if max_node is not None and value < max_node.value:            
                gameboard = max_node
                value = max_node.value
        return gameboard     
# max_value()

#--------------------------------------------------------------
#
#   min_value(level, gameboard, player1, player2)
#       Helper function that finds the minimum nodes in the
#       minimax tree. Returns the minimum scoring gameboard 
#       object.
#
#--------------------------------------------------------------
def min_value(level, gameboard, player1, player2):
    if checkWinner(gameboard.gameboard, player1, player2) != 0:
        gameboard.value = -1000000000   
    if level == 0:
        return None
    value = 1000000000
    if gameboard is not None:
        for node in findSuccessors(gameboard, player2):
            min_node = max_value(level-1, node, player1, player2)
            if min_node is not None and value > min_node.value:            
                gameboard = min_node
                value = min_node.value
        return gameboard
# min_value()

#--------------------------------------------------------------
#
#   findSuccessors(gameboard_state, player)
#       Finds all of the successors to the current game board
#       state using the empty slots. Returns the successor list.
#
#--------------------------------------------------------------
def findSuccessors(gameboard_state, player):
    global numNodesGen
    successors = []
    moves = checkBoard( gameboard_state.gameboard, player)
    for move in moves[3]:  # For all of the blank moves
        newgameboard = boardNode(gameboard_state.gameboard)
        newgameboard.gameboard[move[1]][move[0]] = player
        newgameboard.value = heuristic(newgameboard, player)
        newgameboard.move = move
        successors.append(newgameboard)
        newgameboard.parent = gameboard_state
        numNodesGen += 1
    return successors
# findSuccessors()

#--------------------------------------------------------------
#
#   heuristic(gameboard, player)
#       Produces the heuristic used in minimax algorithm
#       Returns the heuristic value
#
#--------------------------------------------------------------
def heuristic(gameboard, player):
    total = 0    
    moves = checkBoard(gameboard.gameboard, player)
    total = (3 * len(moves[0])) - (3 * len(moves[5])) + (2 * len(moves[1])) - (2* len(moves[4]))
    return total
# heuristic()   

#--------------------------------------------------------------
#
#   checkWinner( board, player1, player2, ply )
#       Checks to see if either player has won the game.
#       Returns that respective player
#
#--------------------------------------------------------------
def checkWinner( board, player1, player2):
    # return the state with the maximum min value
    moves = []
    global checkWin
    checkWin = 1
    player1_count = checkCols( board, player1, 4, moves ) + checkRows( board, player1, 4, moves ) + checkDiags( board, player1, 4, moves )
    player2_count = checkCols( board, player2, 4, moves ) + checkRows( board, player2, 4, moves ) + checkDiags( board, player2, 4, moves )
    checkWin = 0
    if player1_count != 0:
        return player1
    if player2_count != 0:
        return player2
    return 0
# checkWinner()

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
    enemy_moves_2s = []
    enemy_moves_3s = []
    emptySpaces = []
    enemy_player = None

    if player == 'O':
        enemy_player = 'X'
    else:
        enemy_player = 'O'


    # Get two in a row moves
    checkCols( board, player, 2, moves_2s )
    checkRows( board, player, 2, moves_2s )
    checkDiags( board, player, 2, moves_2s )

    # Get three in a row moves
    checkCols( board, player, 3, moves_3s )
    checkRows( board, player, 3, moves_3s )
    checkDiags( board, player, 3, moves_3s )

    # Get two in a row moves for enemy
    checkCols( board, enemy_player, 2, enemy_moves_2s )
    checkRows( board, enemy_player, 2, enemy_moves_2s )
    checkDiags( board, enemy_player, 2, enemy_moves_2s )

    # Get three in a row moves for enemy
    checkCols( board, enemy_player, 3, enemy_moves_3s )
    checkRows( board, enemy_player, 3, enemy_moves_3s )
    checkDiags( board, enemy_player, 3, enemy_moves_3s )

    # Find all empty spaces
    for x in range( 0, len( board[0] ) ):
        for y in range( 0, len( board ) ):
            if board[y][x] == ' ':
                emptySpaces.append( (x,y) )
    
    # Find all empty spots not already in moves_2s or moves_3s   ##### I NEED TO CHECK TO SEE HOW moves_others WILL BE USED IN THE ADVANCED AND MASTER PLAYERS
    moves_others = set(emptySpaces).difference(moves_2s)
    moves_others = set(emptySpaces).difference(moves_3s)
    moves_others = moves_others.difference(moves_3s)

    return moves_2s, moves_3s, list(moves_others), emptySpaces, enemy_moves_2s, enemy_moves_3s
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
    total_count = 0 # used for the minimax heuristic, #### THIS MIGHT DOUBLE COUNT 2,3,4 moves in a row

    # Loop through each column
    for col in range( 0, len(board[0]) ):
        # Check column from top to bottom
        count = 0
        for row in range( 0, len(board) ):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == ' ' and count == numInARow:
                addMove( moves, col, row)
                total_count += 1
                count = 0
            elif checkWin == 1 and count == numInARow:
                total_count += 1
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
                total_count += 1
                count = 0
            elif checkWin == 1 and count == numInARow:
                total_count += 1
                count = 0
            else:
                count = 0
    return total_count
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
    total_count = 0

    # Loop through each row
    for row in range( 0, len(board) ):
        # Check row from left to right
        count = 0
        for col in range( 0, len(board[0]) ):
            if board[row][col] == player:
                count += 1
            elif board[row][col] == ' ' and count == numInARow:
                addMove( moves, col, row)
                total_count += 1
                count = 0
            elif checkWin == 1 and count == numInARow:
                total_count += 1
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
                total_count += 1
                count = 0
            elif checkWin == 1 and count == numInARow:
                total_count += 1
                count = 0
            else:
                count = 0
    return total_count
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
    total_count = 0
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
                total_count += 1
                count = 0
            elif checkWin == 1 and count == numInARow:
                total_count += 1
                count = 0
            else:
                count = 0

            row += row_mod
            col += col_mod
    return total_count
# checkDiags()


#--------------------------------------------------------------
#
#   addMove( moves, mov_x, mov_y )
#       Adds the move to 'moves' list if it is not already in
#       the list.
#
#--------------------------------------------------------------
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
#   printBoard( state )
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
# printBoard()


# Call main function
#main()

# for playing the beginner
#beginplay()

# for playing advanced vs beginner
#advancedplay()

# for playing master vs advanced
#masterplay()


beginnervsmasterplay()
mastervsbeginnerplay()
beginnervsmasterplay()
mastervsbeginnerplay()

print('Number of beginner wins {0}'.format(beginWins))
print('Number of master wins {0}'.format(masterWins))
print('Number of ties {0}'.format(beginvsmasterTie))