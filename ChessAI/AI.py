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
import time
import random
import engine
from engine import gamestate
import numpy as np

global KingNeighbourPawns
KingNeighbourPawns = 0
# to store material values of the pieces
pieceScore = {"K": 0, "Q": 1200, "R": 500, "B": 400, "N": 400, "p": 82}


# improvements

# you can make an 2d array for the king positional weights by check if their are friendly pieces around the king

# High values for check, checkmate and stalemate
CHECKMATE = 100000

STALEMATE = 0

DEPTH = 2
# initial depth can be zero but we get the depth from the user


# to store the positional weights of the pieces
# include the following positional weights
# embed many parameters in them such as
# piece map
# central control
# pawn structure
# diagonal control
# rook row column control
knightScores = np.array(
    [
        [-167, -89, -34, -49, 61, -97, -15, -107],
        [-73, -41, 72, 36, 23, 62, 7, -17],
        [-47, 60, 37, 65, 84, 129, 73, 44],
        [-9, 17, 19, 53, 37, 69, 18, 22],
        [-13, 4, 16, 13, 28, 19, 21, -8],
        [-23, -9, 12, 10, 19, 17, 25, -16],
        [-29, -53, -12, -3, -1, 18, -14, -19],
        [-105, -21, -58, -33, -17, -28, -19, -23],
    ]
)

bishopScores = np.array(
    [
        [-29, 4, -82, -37, -25, -42, 7, -8],
        [-26, 16, -18, -13, 30, 59, 18, -47],
        [-16, 37, 43, 40, 35, 50, 37, -2],
        [-4, 16, 13, 28, 19, 47, 15, -14],
        [-6, 5, 13, 13, 13, 12, 4, -9],
        [0, 15, 15, 15, 14, 27, 18, -18],
        [-4, 15, 14, 15, 14, 15, 10, -18],
        [-19, 7, -8, -19, -11, -16, 7, -26],
    ]
)


rookScores = np.array(
    [
        [32, 42, 32, 51, 63, 9, 31, 43],
        [27, 32, 58, 62, 80, 67, 26, 44],
        [-5, 19, 26, 36, 17, 45, 61, 16],
        [-24, -11, 7, 26, 24, 35, -8, -20],
        [-36, -26, -12, -1, 9, -7, 6, -23],
        [-45, -25, -16, -17, 3, 0, -5, -33],
        [-44, -16, -20, -9, -1, 11, -6, -71],
        [-19, -13, 1, 17, 16, 7, -37, -26],
    ]
)

queenScores = np.array(
    [
        [-28, 0, 29, 12, 59, 44, 43, 45],
        [-24, -39, -5, 1, -16, 57, 28, 54],
        [-13, -17, 7, 8, 29, 56, 47, 57],
        [-27, -27, -16, -16, -1, 17, -2, 1],
        [-9, -26, -9, -10, -2, -4, 3, -3],
        [-14, 2, -11, -2, -5, 2, 14, 5],
        [-35, -8, 11, 2, 8, 15, -3, 1],
        [-1, -18, -9, 10, -15, -25, -31, -50],
    ]
)

pawnScores = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [98, 134, 61, 95, 68, 126, 34, -11],
        [-6, 7, 26, 31, 65, 56, 25, -20],
        [-14, 13, 6, 21, 23, 12, 17, -23],
        [-27, -2, -5, 12, 17, 6, 10, -25],
        [-26, -4, -4, -10, 3, 3, 33, -12],
        [-35, -1, -20, -23, -15, 24, 38, -22],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
)

piecePositionScores = {
    "wN": knightScores,
    "bN": knightScores[::-1],
    "wB": bishopScores,
    "bB": bishopScores[::-1],
    "wQ": queenScores,
    "bQ": queenScores[::-1],
    "wR": rookScores,
    "bR": rookScores[::-1],
    "wp": pawnScores,
    "bp": pawnScores[::-1],
}


def findRandomMove(validMoves, gs):
    """
    pick a random valid move
    Args:
        validMoves: list of valid moves
    Return:
        a random valid move
    """
    if len(validMoves) == 0:
        if gamestate.inCheck:
            gs.checkmate = True
        else:
            gs.stalemate = True
    else:
        return validMoves[random.randint(0, len(validMoves) - 1)]


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
"""
    This function will evaluate the board and give it a score
    for the opponent, the score will be negative
    args: gs: gamestate
          validMoves: valid moves for the player
          depth: depth of the tree
          whiteToMove: boolean to check if white is to move or not
    return: bestMove: best move for the player
            bestMoveScore: best move score for the player
    """


"""
Helper method to make the first recursive call
"""


def findBestMove(gs, validMoves):
    """
    to find the best move using Negamax algorithm
    (NegaMax is a variant form of the minimax algorithm for binary game trees with a
    constant branching factor b. It was developed independently by Alexander Brudno and
    W. Wesley Peterson in 1967, and rediscovered by Tartakower's student Zvonimir Janović
    in 1970. It is mathematically equivalent to minimax, but it uses only one recursive
    call instead of two.)
    gs: gamestate
    validMoves: valid moves for the player

    return: bestMove: best move for the player

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
    
    """
    start = time.time()
    global nextMove, counter
    # if we dont have next move
    # we will find the next move by random
    nextMove = None
    random.shuffle(validMoves)
    counter = 0
    # findMoveNegaMax(gs, validMoves, DEPTH, 1 if gs.whitemove else -1)
    findMoveNegaMaxAlphaBeta(
        gs, validMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whitemove else -1, start
    )
    print(counter)
    return nextMove


def findMoveMinMax(gs, validMoves, depth, whiteToMove):
    """
    to find the best move using MinMax algorithm
    gs: gamestate
    validMoves: valid moves for the player
    depth: depth of the tree
    whiteToMove: boolean to check if white is to move or not

    return: bestMove: best move for the player
    """
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


def findMoveNegaMaxAlphaBeta(gs, validMoves, depth, alpha, beta, turnMultiplier, start):
    """
    to find the best move using Negamax algorithm
    Negamax works on the principle that the value of a position is the negative of the value of its mirror image.
    Negamax is a variant form of the minimax algorithm for binary game trees with a constant branching factor b.

    ALPHA BETA PRUNING
    IS A SEARCH ALGORITHM THAT SEARCHES THROUGH THE BEST MOVES OF A GAME
    WHILE PRUNING NODES THAT CANNOT IMPROVE THE FINAL DECISION
    BUT IT DOES LESSEN THE TIME COMPLEXITY

    gs: gamestate
    validMoves: valid moves for the player
    depth: depth of the tree
    alpha: alpha value
    beta: beta value
    turnMultiplier: to check if white is to move or not
    start: start time

    return: bestMove: best move for the player


    """
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
        score = -findMoveNegaMaxAlphaBeta(
            gs, nextMoves, depth - 1, -beta, -alpha, -turnMultiplier, start
        )
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
        # if time.time() - start > 6:
        #     break
        # we stop looking at the next moves
    return maxScore


def findMoveNegaMax(gs, validMoves, depth, turnMultiplier):
    """
    This function will evaluate the board and give it a score
    TO check the surroundings
    Protecting and attacking pieces
    args: gs: gamestate
          validMoves: valid moves for the player
          depth: depth of the tree
          whiteToMove: boolean to check if white is to move or not

    return: bestMove: best move for the player
            bestMoveScore: best move score for the player
    """

    global nextMove, counter
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


def ScoreBoard(gs):
    """
    To score the board based on the material
    and positional standpoint and various other factors as defined in AI module.
    gs: gamestate
    return: score: score of the board
    """
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
            if square != "--":
                piece_position_score = 0
                if square[1] != "K":
                    piece_position_score = piecePositionScores[square][row][col]
                if square[0] == "w":
                    score += (
                        pieceScore[square[1]]
                        + piece_position_score
                        + 15 * int(gs.wcastled)
                        + 10 * int(len(gs.getvalidmoves()))
                        + 15 * int(KingPawnShield(gs))
                        + (-35) * int(doublePawns(gs))
                        + 40 * int(len(engine.Queen_squares))
                        + 20 *
                        int(countWhitePiecesOnKingSurroundingSquares(gs))
                        + 15 * int(len(engine.King_squares))
                        + 10 * int(knightSupport(gs))
                    )
                if square[0] == "b":
                    score -= (
                        pieceScore[square[1]]
                        + piece_position_score
                        + 15 * int(gs.bcastled)
                        + 10 * int(len(gs.getvalidmoves()))
                        + 15 * int(KingPawnShield(gs))
                        + (-35) * int(doublePawns(gs))
                        + 40 * int(len(engine.Queen_squares))
                        + 20 *
                        int(countWhitePiecesOnKingSurroundingSquares(gs))
                        + 15 * int(len(engine.King_squares))
                        + 10 * int(knightSupport(gs))
                    )

    return score


def Score_By_Material(board):
    """
    To score the board based on the material
    and positional standpoint
    board: gamestate
    return: score: score of the board
    """
    score = 0
    for row in board:
        for square in row:
            # assuming that the white pieces are primary
            if square[0] == "w":
                score += pieceScore[square[1]]
            elif square[0] == "b":
                score -= pieceScore[square[1]]
    return score


# def QueenMobililty(engine):
#     return len(engine.Queen_squares)


def countWhitePiecesOnKingSurroundingSquares(gs):
    """
    To count the number of white pieces on the king surrounding squares
    gs: gamestate
    return: count: number of white pieces on the king surrounding squares
    """
    count = 0

    # get the king's position
    if gs.whitemove:
        king_row, king_col = gs.blackKingLocation
    else:
        king_row, king_col = gs.whiteKingLocation

    # check the 8 surrounding squares
    for row in range(king_row - 1, king_row + 2):
        for col in range(king_col - 1, king_col + 2):
            if isOnBoard(row, col):
                piece = gs.board[row][col]
                if piece[0] == "w":
                    count += 1
    # print("White pieces on king surrounding squares",count)
    return count


def isOnBoard(row, col):
    """
    To check if the row and col are on the board
    This is to avoid index out of range error
    row: row number
    col: col number
    """
    return row >= 0 and row < 8 and col >= 0 and col < 8


# def KingMobililty(engine):
#     return len(engine.King_squares)

# def KingCastled(gs):
# print("White King Castled",gs.wcastled)
# print("Black King Castled",gs.bcastled)

# def freedom(gs):
#     # if gs.whitemove:
#     #     return len(gs.getvalidmoves())
#     # else:
#         return len(gs.getvalidmoves())


def KingPawnShield(gs):
    """
    To check if the king has a pawn shield
    gs: gamestate
    return: True if the king has a pawn shield
            False if the king does not have a pawn shield
    """
    global KingNeighbourPawns
    KingNeighbourPawns = 0
    # get the king's position
    if gs.whitemove:
        king_row, king_col = gs.blackKingLocation
    else:
        king_row, king_col = gs.whiteKingLocation

    # check the 8 surrounding squares
    for row in range(king_row - 1, king_row + 2):
        for col in range(king_col - 1, king_col + 2):
            if isOnBoard(row, col):
                piece = gs.board[row][col]
                if piece[0] == "w" and piece[1] == "p":
                    KingNeighbourPawns += 1
    # print("King Neighbour Pawns",KingNeighbourPawns)
    return KingNeighbourPawns


# determines the centre-pawn count at sq e4,d4,e5,d5
def centrePawnCount(gs):
    """
    To count the number of centre pawns
    gs: gamestate
    return: pawn: number of centre pawns
    """
    pawn = 0
    centerPawn = [
        (3, 3),
        (3, 4),
        (4, 3),
        (4, 4),
    ]  # list of tuples for row-col of sq d5,e5,d4,e4 resp
    for sq in centerPawn:
        if gs.board[sq[0]][sq[1]] == "wp":
            pawn += 1
        elif gs.board[sq[0]][sq[1]] == "bp":
            pawn -= 1
    return pawn


# determines whether knight is on sq a1 to a8,a8 to h8,a1 to h1 or h1 to h8
def knightPeriphery0(gs):
    """
    To check if the knight is on the periphery
    gs: gamestate
    """
    kp0 = 0
    kp0list = np.array(
        [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (7, 1),
            (7, 2),
            (7, 3),
            (7, 4),
            (7, 5),
            (7, 6),
            (7, 7),
            (6, 7),
            (5, 7),
            (4, 7),
            (3, 7),
            (2, 7),
            (1, 7),
            (0, 7),
            (0, 6),
            (0, 5),
            (0, 4),
            (0, 3),
            (0, 2),
            (0, 1),
        ]
    )
    for sq in kp0list:
        if gs.board[sq[0]][sq[1]] == "wN":
            kp0 += 1
        elif gs.board[sq[0]][sq[1]] == "bN":
            kp0 -= 1
    return kp0


# determines whether knight is on sq b2 to b7,b7 to g7,b2 to g2,g2 to g7
def knightPeriphery1(gs):
    kp1 = 0
    kp1list = np.array(
        [
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (6, 1),
            (6, 2),
            (6, 3),
            (6, 4),
            (6, 5),
            (6, 6),
            (5, 6),
            (4, 6),
            (3, 6),
            (2, 6),
            (1, 6),
            (1, 5),
            (1, 4),
            (1, 3),
            (1, 2),
        ]
    )
    for sq in kp1list:
        if gs.board[sq[0]][sq[1]] == "wN":
            kp1 += 1
        elif gs.board[sq[0]][sq[1]] == "bN":
            kp1 -= 1
    return kp1


# determines whether knight is on sq c3 to c6,c6 to f6,c3 to f3,f3 to f6
def knightPeriphery2(gs):
    kp2 = 0
    kp2list = np.array(
        [
            (2, 2),
            (3, 2),
            (4, 2),
            (5, 2),
            (5, 3),
            (5, 4),
            (5, 5),
            (4, 5),
            (3, 5),
            (2, 5),
            (2, 4),
            (2, 3),
        ]
    )
    for sq in kp2list:
        if gs.board[sq[0]][sq[1]] == "wN":
            kp2 += 1
        elif gs.board[sq[0]][sq[1]] == "bN":
            kp2 -= 1
    return kp2


# determines whether knight is on sq e4,d4,e5,d5
def knightPeriphery3(gs):
    kp3 = 0
    kp3list = np.array(
        [(3, 3), (3, 4), (4, 3), (4, 4)]
    )  # list of tuples for row-col of sq d5,e5,d4,e4 resp
    for sq in kp3list:
        if gs.board[sq[0]][sq[1]] == "wN":
            kp3 += 1
        elif gs.board[sq[0]][sq[1]] == "bN":
            kp3 -= 1
    return kp3


def doublePawns(gs):
    doublepawn = 0
    for r in range(8):
        for c in range(8):
            piece = gs.board[r][c]
            if piece == "wp" or piece == "bp":
                for rows in range(r - 1, -1, -1) if piece == "wp" else range(r + 1, 8):
                    if gs.board[rows][c] == piece:
                        doublepawn += 1 if piece == "wp" else -1
                        break
    return doublepawn


# determines whether the bishop pair exists
def bishopPair(gs):
    wbishop = 0
    bbishop = 0
    for r in range(8):
        for c in range(8):
            if gs.board[r][c] == "wB":  # counts no. of wB
                wbishop += 1
            elif gs.board[r][c] == "bB":  # counts no. of bB
                bbishop += 1
    if wbishop > 1 or bbishop > 1:
        return 1


# determines whether rook is on Seventh rank wrt player
def rookOnSeventh(gs):
    rookSeventh = 0
    for col in range(8):
        if gs.board[1][col] == "wR":  # rank 7 for white
            rookSeventh += 1
        elif gs.board[6][col] == "bR":  # rank 2 for black
            rookSeventh -= 1
    return rookSeventh


# determines whether bishop is on large diagonal
def bishopOnLarge(gs):
    bishopLarge = 0
    for r in range(8):
        # bishop on diagonal h1-a8
        if gs.board[r][r] == "wB":
            bishopLarge += 1
        elif gs.board[r][r] == "bB":
            bishopLarge -= 1

        # bishop on diagonal a1-h8
        if gs.board[r][7 - r] == "wB":
            bishopLarge += 1
        elif gs.board[r][7 - r] == "bB":
            bishopLarge += 1
    return bishopLarge


def knightSupport(gs):
    knightsupport = 0
    for r in range(8):
        for c in range(8):
            if r > 0 and r < 7 and c > 0 and c < 7:
                if gs.board[r][c] == "wN" and (
                    gs.board[r - 1][c - 1] == "wp" or gs.board[r -
                                                               1][c + 1] == "wp"
                ):
                    knightsupport += 1
                elif gs.board[r][c] == "bN" and (
                    gs.board[r + 1][c - 1] == "bp" or gs.board[r +
                                                               1][c + 1] == "bp"
                ):
                    knightsupport -= 1
    return knightsupport
