# material standpoint
# greedy algorithm
# minimax algorithm
# minimax with alpha beta pruning
# minimax with alpha beta pruning and move ordering


# minmax will evaluate the board and give it a score
# for the opponent, the score will be negative
# for the player, the score will be positive
# the score will be based on the material on the board
# the score will be based on the position of the pieces
# the score will be based on the number of moves available
# the score will be based on the checkmate and stalemate
# the score will be based on the check
import random

# to store material values of the pieces
pieceScore = {'K': 0, 'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'p': 1}

# High values for check, checkmate and stalemate
CHECKMATE = 1000

STALEMATE = 0

DEPTH = 3




'''
    This function will evaluate the board and give it a score
    for the opponent, the score will be negative
    for the player, the score will be positive
    for the opponent, the score will be negative
    for the player, the score will be positive
    the score will be based on the material on the board
    the score will be based on the position of the pieces
    the score will be based on the number of moves available
    the score will be based on the checkmate and stalemate
    the score will be based on the check
    
'''
def findRandomMOve(validMoves):
    # Return a random valid move
    # get an index to get a random move from the list of valid moves
    random.randint(0, len(validMoves) - 1)
    return validMoves[random.randint(0, len(validMoves) - 1)]


def findBestMove(gs, validMoves):
    # Return a valid move that is the best move
    # get a random move from the list of valid moves
    # random.shuffle(validMoves)
    # return validMoves[0]
    
    # to be able to return the best move for both white and black
    turnMultiplier = 1 if gs.whitemove else -1

    # assuming the opponent make a move which makes him best
    # opponent makes his best move
    # we look one branch in the future to get this move
    opponentMinMaxScore = float('inf')
    bestPlayerMove = None
    random.shuffle(validMoves)

    # player is making the next move
    # first layer
    for playerMove in validMoves:

        gs.makeMove(playerMove)
        # opponent is making the next move

        # so lets get the valid moves for the opponent
        opponentMoves = gs.getvalidmoves()


        opponentMaxScore = -float('inf')

        # second layer
        for opponentMove in opponentMoves:

            # make every move and check the score
            gs.makeMove(opponentMove)
            if gs.checkmate:
                # we traversed two layers
                # so we invert the score
                score = -turnMultiplier * 10000
            elif gs.stalemate:
                # minimize my opponents best move
                score = -turnMultiplier * 5000
            else:
                score = -turnMultiplier * Score_By_Material(gs.board)

            # while traversing store the max score
            if score > opponentMaxScore:
                opponentMaxScore = score

            # undo moves karo nahi toh saare moves ho jayenge!
            gs.undoMove()
            print(score)
        if opponentMaxScore < opponentMinMaxScore:
            opponentMinMaxScore = opponentMaxScore
            bestPlayerMove = playerMove

        # undo moves karo nahi toh saare moves ho jayenge!
        gs.undoMove()
    return bestPlayerMove


'''
    Score the board based on material
'''
def Score_By_Material(board):
    score = 0
    for row in board:
        for square in row:
            # assuming that the white pieces are primary
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
    return score