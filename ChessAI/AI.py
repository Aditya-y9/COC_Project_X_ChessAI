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

global KingNeighbourPawns
KingNeighbourPawns = 0
# to store material values of the pieces
pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

knightScores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                 [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                 [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                 [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                 [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                 [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                 [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                 [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

bishopScores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

rookScores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

queenScores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

pawnScores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
               [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
               [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
               [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
               [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
               [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

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
def findRandomMove(validMoves):
    return validMoves[random.randint(0,len(validMoves)-1)]





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
    return: bestMove: best move for the player
            bestMoveScore: best move score for the player
    '''


'''
Helper method to make the first recursive call
'''

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
            if score < minScore:
                minScore = score
                if depth == DEPTH:
                    nextMove = move
            gs.undoMove()
        return minScore

def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier):
    KingPawnShield(gs)
    # alpha beta pruning
    global counter
    counter += 1
    global nextMove
    # if we are at the depth 0
    if depth == 0:
        return turnMultiplier * ScoreBoard(gs)
    # start with worst possible score
    # algorithm will work for both white and black
    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        # for recursion
        nextMoves = gs.getvalidmoves()

        # negative sign to change the perspective
        # during recursion

                                                    # because for our opponent alpha and beta will be inverted
        score = -findMoveNegaMaxAlphaBeta(gs, nextMoves, depth - 1,-beta,-alpha,-turnMultiplier)
        # if maxScore is greater than beta
        # we will prune the tree
        # if we get better move evlauation score
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                # the opponent will make the best move
                # we will see this at the root node
                nextMove = move
        gs.undoMove()
        if maxScore > alpha:
            # pruning
            alpha = maxScore
        if alpha >= beta:
            break
        # we stop looking at the next moves
    return maxScore

def findMoveNegaMax(gs, validMoves, depth, turnMultiplier):
    global nextMove , counter
    counter += 1
    # if we are at the depth 0
    if depth == 0:
        return turnMultiplier * Score_By_Material(gs.board)
    # start with worst possible score
    # algorithm will work for both white and black
    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        # for recursion
        nextMoves = gs.getvalidmoves()

        # negative sign to change the perspective
        # during recursion
        score = -findMoveNegaMax(gs, nextMoves, depth - 1, -turnMultiplier)

        # if we get better move evlauation score
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                # the opponent will make the best move
                # we will see this at the root node
                nextMove = move
        gs.undoMove()
    return maxScore





'''
    This function will evaluate the board and give it a score
    TO check the surroundings
    Protecting and attacking pieces
    args: gs: gamestate
          validMoves: valid moves for the player
          depth: depth of the tree
          whiteToMove: boolean to check if white is to move or not

    return: bestMove: best move for the player
            bestMoveScore: best move score for the player
    '''
def ScoreBoard(gs):
    # print("king pawn shield",KingPawnShield(gs))
    
    if gs.checkmate:
        if gs.whitemove:
            return -CHECKMATE
        else:
            return CHECKMATE
    elif gs.stalemate:
        return STALEMATE

    score = 0
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            # assuming that the white pieces are primary
            square = gs.board[row][col]
            # square is the piece
            if square!='--':
                piece_position_score = 0
                if square[1] != "K":
                    piece_position_score = piecePositionScores[square][row][col]
                if square[0] == "w":
                    score += pieceScore[square[1]] + piece_position_score
                if square[0] == "b":
                    score -= pieceScore[square[1]] + piece_position_score

    return score





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

def QueenMobililty(engine):
    return len(engine.Queen_squares)

def KingPawnShield(gs):
    global KingNeighbourPawns
    KingNeighbourPawns = 0
    rows, cols = len(gs.board), len(gs.board[0])
    if gs.whitemove:
        kingRow = gs.whiteKingLocation[0]
        kingCol = gs.whiteKingLocation[1]
        directions = [(0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1)]
        for dr, dc in directions:
            new_row, new_col = kingRow + dr, kingCol + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and gs.board[new_row][new_col] == "wp":
                KingNeighbourPawns += 1
    else:
        kingRow = gs.blackKingLocation[0]
        kingCol = gs.blackKingLocation[1]
        directions = [(0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1)]
        for dr, dc in directions:
            new_row, new_col = kingRow + dr, kingCol + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and gs.board[new_row][new_col] == "bp":
                KingNeighbourPawns += 1
    return KingNeighbourPawns

def KingMobililty(engine):
    return len(engine.King_squares)

def KingCastled(gs):
    print("White King Castled",gs.wcastled)
    print("Black King Castled",gs.bcastled)

def NumberofPawns(gs):
    count =0
    for square in gs.board:
        if square[1] == "p":
            count+=1 
    return count
        