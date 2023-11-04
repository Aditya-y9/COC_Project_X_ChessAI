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
import engine
from engine import gamestate
import random

global KingNeighbourPawns
KingNeighbourPawns = 0
# to store material values of the pieces
pieceScore = {"K": 0, "Q": 911, "R": 530, "B": 374, "N": 342, "p": 80}

knightScores = [[0.0, 10.0, 20.0, 20.0, 20.0, 20.0, 10.0, 0.0],
                 [10.0, 30.0, 50.0, 50.0, 50.0, 50.0, 30.0, 10.0],
                 [20.0, 50.0, 60.0, 65.0, 65.0, 60.0, 50.0, 20.0],
                 [20.0, 55.0, 65.0, 70.0, 70.0, 65.0, 55.0, 20.0],
                 [20.0, 50.0, 65.0, 70.0, 70.0, 65.0, 50.0, 20.0],
                 [20.0, 55.0, 60.0, 65.0, 65.0, 60.0, 55.0, 20.0],
                 [10.0, 30.0, 50.0, 55.0, 55.0, 50.0, 30.0, 10.0],
                 [0.0, 10.0, 20.0, 20.0, 20.0, 20.0, 10.0, 0.0]]

bishopScores = [[0.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0.0],
                 [20.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 20.0],
                 [20.0, 40.0, 50.0, 60.0, 60.0, 50.0, 40.0, 20.0],
                 [20.0, 50.0, 50.0, 60.0, 60.0, 50.0, 50.0, 20.0],
                 [20.0, 40.0, 60.0, 60.0, 60.0, 60.0, 40.0, 20.0],
                 [20.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 20.0],
                 [20.0, 50.0, 40.0, 40.0, 40.0, 40.0, 50.0, 20.0],
                 [0.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 0.0]]

rookScores = [[25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0],
               [50.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 50.0],
               [0.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 0.0],
               [0.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 0.0],
               [0.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 0.0],
               [0.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 0.0],
               [0.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 0.0],
               [25.0, 25.0, 25.0, 50.0, 50.0, 25.0, 25.0, 25.0]]

queenScores = [[0.0, 20.0, 20.0, 30.0, 30.0, 20.0, 20.0, 0.0],
                [20.0, 40.0, 40.0, 40.0, 40.0, 40.0, 40.0, 20.0],
                [20.0, 40.0, 50.0, 50.0, 50.0, 50.0, 40.0, 20.0],
                [30.0, 40.0, 50.0, 50.0, 50.0, 50.0, 40.0, 30.0],
                [40.0, 40.0, 50.0, 50.0, 50.0, 50.0, 40.0, 30.0],
                [20.0, 50.0, 50.0, 50.0, 50.0, 50.0, 40.0, 20.0],
                [20.0, 40.0, 50.0, 40.0, 40.0, 40.0, 40.0, 20.0],
                [0.0, 20.0, 20.0, 30.0, 30.0, 20.0, 20.0, 0.0]]

pawnScores = [[80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0],
               [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0],
               [30.0, 30.0, 40.0, 50.0, 50.0, 40.0, 30.0, 30.0],
               [25.0, 25.0, 30.0, 45.0, 45.0, 30.0, 25.0, 25.0],
               [20.0, 20.0, 20.0, 40.0, 40.0, 20.0, 20.0, 20.0],
               [25.0, 15.0, 10.0, 20.0, 20.0, 10.0, 15.0, 25.0],
               [25.0, 30.0, 30.0, 0.0, 0.0, 30.0, 30.0, 25.0],
               [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]]

piecePositionScores = {"wN": knightScores,
                         "bN": knightScores[::-1],
                         "wB": bishopScores,
                         "bB": bishopScores[::-1],
                         "wQ": queenScores,
                         "bQ": queenScores[::-1],
                         "wR": rookScores,
                         "bR": rookScores[::-1],
                         "wp": pawnScores,
                         "bp": pawnScores[::-1]}
# for the position of the pieces
# improvements

# you can make an 2d array for the king positional weights by check if their are friendly pieces around the king



# High values for check, checkmate and stalemate
CHECKMATE = 1000

STALEMATE = 0

DEPTH = 2





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
def findRandomMove(validMoves,gs):
    if len(validMoves) == 0:
        if gamestate.inCheck:
            gs.checkmate = True
        else:
            gs.stalemate = True
    else:
        return validMoves[random.randint(0, len(validMoves)-1)] 





# def findBestMove1(gs, validMoves):
#     # Return a valid move that is the best move
#     # get a random move from the list of valid moves
#     # random.shuffle(validMoves)
#     # return validMoves[0]
    
#     # to be able to return the best move for both white and black
#     turnMultiplier = 1 if gs.whitemove else -1

#     # assuming the opponent make a move which makes him best
#     # opponent makes his best move
#     # we look one branch in the future to get this move
#     opponentMinMaxScore = float('inf')
#     bestPlayerMove = None
#     random.shuffle(validMoves)

#     # player is making the next move
#     # first layer
#     for playerMove in validMoves:

#         gs.makeMove(playerMove)
#         # opponent is making the next move

#         # so lets get the valid moves for the opponent
#         opponentMoves = gs.getvalidmoves()


#         if gs.checkmate:
#             # we traversed two layers
#             # so we invert the score
#             score = -CHECKMATE
#         elif gs.stalemate:
#             # minimize my opponents best move
#             score = STALEMATE
#         else:
#             opponentMaxScore = float('inf')

# FILEPATH: /c:/Users/MSHOME/Desktop/Newfolder/COC_Project_X_ChessAI/ChessAI/AI.py
#         # second layer
#             for opponentMove in opponentMoves:

#                 # make every move and check the score
#                 gs.makeMove(opponentMove)
#                 gs.getvalidmoves()
#                 if gs.checkmate:
#                     # we traversed two layers
#                     # so we invert the score
#                     score = CHECKMATE
#                 elif gs.stalemate:
#                     # minimize my opponents best move
#                     score = STALEMATE
#                 else:
#                     score = -turnMultiplier * Score_By_Material(gs.board)

#                 # while traversing store the max score
#                 if score > opponentMaxScore:
#                     opponentMaxScore = score

#                 # undo moves karo nahi toh saare moves ho jayenge!
#                 gs.undoMove()
#                 print(score)
#             if opponentMaxScore < opponentMinMaxScore:
#                 opponentMinMaxScore = opponentMaxScore
#                 bestPlayerMove = playerMove

#             # undo moves karo nahi toh saare moves ho jayenge!
#             gs.undoMove()
#     return bestPlayerMove


# method to travel tree recursively
'''
    This function will evaluate the board and give it a score
    for the opponent, the score will be negative
    args: gs: gamestate
          validMoves: valid moves for the player
          depth: depth of the tree
          whiteToMove: boolean to check if white is to move or not
'''
def ScoreBoard(gs):
        if gs.checkmate:
            return -CHECKMATE if gs.whitemove else CHECKMATE
        elif gs.stalemate:
            return STALEMATE
        score = 0
        for row, row_values in enumerate(gs.board):
            for col, square in enumerate(row_values):
                if square != '--':
                    piece_position_score = piecePositionScores[square][row][col] if square[1] != "K" else 0
                    if square[0] == "w":
                        score += pieceScore[square[1]] + piece_position_score + 60 * int(gs.wcastled) + \
                                 20 * int(freedom(gs)) + (-7) * int(doublePawns(gs)) + \
                                 3 * int(QueenMobililty(engine)) + 30 * int(countWhitePiecesOnKingSurroundingSquares(gs)) + \
                                 30 * int(KingMobililty(engine))
                    elif square[0] == "b":
                        score -= pieceScore[square[1]] + piece_position_score + 60 * int(gs.wcastled) + \
                                 20 * int(freedom(gs)) + 30 * int(KingPawnShield(gs)) + \
                                 (-7) * int(doublePawns(gs)) + 3 * int(QueenMobililty(engine)) + \
                                 30 * int(countWhitePiecesOnKingSurroundingSquares(gs)) + \
                                 30 * int(KingMobililty(engine))
        return score

def Score_By_Material(board):
        score = 0
        for row_values in board:
            for square in row_values:
                if square[0] == 'w':
                    score += pieceScore[square[1]]
                elif square[0] == 'b':
                    score -= pieceScore[square[1]]
        return score

def findMoveNegaMax(gs, validMoves, depth, turnMultiplier):
        if depth == 0 or gs.checkmate or gs.stalemate:
            return turnMultiplier * ScoreBoard(gs)
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getvalidmoves()
            score = -findMoveNegaMax(gs, nextMoves, depth - 1, -turnMultiplier)
            maxScore = max(maxScore, score)
            gs.undoMove()
        return maxScore

def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier):
        if depth == 0 or gs.checkmate or gs.stalemate:
            return turnMultiplier * ScoreBoard(gs)
        maxScore = -CHECKMATE
        for move in validMoves:
            gs.makeMove(move)
            nextMoves = gs.getvalidmoves()
            score = -findMoveNegaMaxAlphaBeta(gs, nextMoves, depth - 1, -beta, -alpha, -turnMultiplier)
            maxScore = max(maxScore, score)
            gs.undoMove()
            alpha = max(alpha, maxScore)
            if alpha >= beta:
                break
        return maxScore

def findMoveMinMax(gs, validMoves, depth, whiteToMove):
        global nextMove
        # if we are at the depth 0
        if depth == 0:
            return Score_By_Material(gs.board)
        if whiteToMove:
            # start with worst possible score
            maxScore = -CHECKMATE

            # traverse the tree
            for move in validMoves:
                gs.makeMove(move)
                nextMoves = gs.getvalidmoves()
                score = findMoveMinMax(gs, nextMoves, depth - 1, False)
                if score > maxScore:
                    maxScore = score
                    if depth == DEPTH:
                        nextMove = move
                gs.undoMove()
            return maxScore
        else:
            # start with worst possible score
            minScore = CHECKMATE
            for move in validMoves:
                gs.makeMove(move)
                nextMoves = gs.getvalidmoves()
                score = findMoveMinMax(gs, nextMoves, depth - 1, True)
                minScore = min(minScore, score)
                gs.undoMove()
            return minScore

def findBestMove(gs, validMoves):
        global nextMove , counter
        # if we dont have next move
        # we will find the next move by random
        nextMove = None
        random.shuffle(validMoves)
        counter = 0
        # findMoveNegaMax(gs, validMoves, DEPTH, 1 if gs.whitemove else -1)
        findMoveNegaMaxAlphaBeta(gs, validMoves, DEPTH,-CHECKMATE,CHECKMATE, 1 if gs.whitemove else -1)
        print(counter)
        return nextMove

def countWhitePiecesOnKingSurroundingSquares(gs):
        count = 0
        king_row, king_col = gs.blackKingLocation if gs.whitemove else gs.whiteKingLocation
        for row in range(king_row-1, king_row+2):
            for col in range(king_col-1, king_col+2):
                if isOnBoard(row, col) and gs.board[row][col][0] == 'w':
                    count += 1
        return count

def isOnBoard(row, col):
        return 0 <= row < 8 and 0 <= col < 8

def KingMobililty(engine):
        return len(engine.King_squares)

def freedom(gs):
        return len(gs.getvalidmoves())

def KingPawnShield(gs):
        count = 0
        king_row, king_col = gs.blackKingLocation if gs.whitemove else gs.whiteKingLocation
        for row in range(king_row-1, king_row+2):
            for col in range(king_col-1, king_col+2):
                if isOnBoard(row, col) and gs.board[row][col] == 'wp':
                    count += 1
        return count

def doublePawns(gs):
        count = 0
        for col in range(8):
            white_pawns = [row for row in range(8) if gs.board[row][col] == 'wp']
            if len(white_pawns) > 1 and white_pawns == sorted(white_pawns):
                count -= 1
            black_pawns = [row for row in range(8) if gs.board[row][col] == 'bp']
            if len(black_pawns) > 1 and black_pawns == sorted(black_pawns, reverse=True):
                count += 1
        return count

def QueenMobililty(engine):
        return len(engine.Queen_squares)

def bishopPair(gs):
        wbishop = sum(1 for row_values in gs.board for square in row_values if square == 'wB')
        bbishop = sum(1 for row_values in gs.board for square in row_values if square == 'bB')
        return 1 if wbishop > 1 or bbishop > 1 else 0

def rookOnSeventh(gs):
        return sum(1 for col in range(8) if gs.board[1][col] == 'wR') - \
               sum(1 for col in range(8) if gs.board[6][col] == 'bR')

def bishopOnLarge(gs):
        return sum(1 for r, c in zip(range(8), range(8)) if gs.board[r][c] == "wB") + \
               sum(1 for r, c in zip(range(8), range(8)) if gs.board[r][7-r] == "wB") - \
               sum(1 for r, c in zip(range(8), range(8)) if gs.board[r][c] == "bB") - \
               sum(1 for r, c in zip(range(8), range(8)) if gs.board[r][7-r] == "bB")

def knightSupport(gs):
        count = 0
        for r, c in [(r, c) for r in range(1, 7) for c in range(1, 7)]:
            if gs.board[r][c] == 'wN' and (gs.board[r-1][c-1] == 'wp' or gs.board[r-1][c+1] == 'wp'):
                count += 1
            elif gs.board[r][c] == 'bN' and (gs.board[r+1][c-1] == 'bp' or gs.board[r+1][c+1] == 'bp'):
                count -= 1
        return count

def centrePawnCount(gs):
        centerPawn = [(3,3),(3,4),(4,3),(4,4)]
        return sum(1 for sq in centerPawn if gs.board[sq[0]][sq[1]] == 'wp') - \
               sum(1 for sq in centerPawn if gs.board[sq[0]][sq[1]] == 'bp')

def knightPeriphery0(gs):
        kp0list = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),
                   (7,7),(6,7),(5,7),(4,7),(3,7),(2,7),(1,7),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(0,1)]
        return sum(1 for sq in kp0list if gs.board[sq[0]][sq[1]] == 'wN') - \
               sum(1 for sq in kp0list if gs.board[sq[0]][sq[1]] == 'bN')

def knightPeriphery1(gs):
        kp1list = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(6,2),(6,3),(6,4),(6,5),
                   (6,6),(5,6),(4,6),(3,6),(2,6),(1,6),(1,5),(1,4),(1,3),(1,2)]
        return sum(1 for sq in kp1list if gs.board[sq[0]][sq[1]] == 'wN') - \
               sum(1 for sq in kp1list if gs.board[sq[0]][sq[1]] == 'bN')

def knightPeriphery2(gs):
        kp2list = [(2,2),(3,2),(4,2),(5,2),(5,3),(5,4),
                   (5,5),(4,5),(3,5),(2,5),(2,4),(2,3)]
        return sum(1 for sq in kp2list if gs.board[sq[0]][sq[1]] == 'wN') - \
               sum(1 for sq in kp2list if gs.board[sq[0]][sq[1]] == 'bN')

def knightPeriphery3(gs):
        kp3list = [(3,3),(3,4),(4,3),(4,4)]
        return sum(1 for sq in kp3list if gs.board[sq[0]][sq[1]] == 'wN') - \
               sum(1 for sq in kp3list if gs.board[sq[0]][sq[1]] == 'bN')

def evaluationFunction(gs, weights):
        return sum([
            weights[0] * findMoveMinMax(gs, gs.getvalidmoves(), DEPTH, True),
            weights[1] * findMoveNegaMaxAlphaBeta(gs, gs.getvalidmoves(), DEPTH, -CHECKMATE, CHECKMATE, 1),
            weights[2] * findMoveNegaMax(gs, gs.getvalidmoves(), DEPTH, 1),
            weights[3] * ScoreBoard(gs),
            weights[4] * Score_By_Material(gs.board),
            weights[5] * countWhitePiecesOnKingSurroundingSquares(gs),
            weights[6] * KingMobililty(engine),
            weights[7] * freedom(gs),
            weights[8] * KingPawnShield(gs),
            weights[9] * doublePawns(gs),
            weights[10] * QueenMobililty(engine),
            weights[11] * bishopPair(gs),
            weights[12] * rookOnSeventh(gs),
            weights[13] * bishopOnLarge(gs),
            weights[14] * knightSupport(gs),
            weights[15] * centrePawnCount(gs),
            weights[16] * knightPeriphery0(gs),
            weights[17] * knightPeriphery1(gs),
            weights[18] * knightPeriphery2(gs),
            weights[19] * knightPeriphery3(gs)
        ])

def optimizeWeights(gs, validMoves):
    # start with some initial weights
    weights = [1] * 20
    best_score = evaluationFunction(gs, weights)
    print("Initial score:", best_score)

    # set the step size for perturbations
    step_size = 0.1

    # repeat until we reach a satisfactory result
    while True:
        # perturb the weights randomly
        new_weights = [w + random.uniform(-step_size, step_size) for w in weights]

        # evaluate the new weights
        new_score = evaluationFunction(gs, new_weights)

        # if the new score is better, accept the new weights
        if new_score > best_score:
            weights = new_weights
            best_score = new_score
            print("New best score:", best_score)
            print("New weights:", weights)

        # if the new score is worse, try again with a new perturbation
        else:
            print("Discarding new weights")
