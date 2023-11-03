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
                    score += pieceScore[square[1]] + piece_position_score + 0.6*int(gs.wcastled)+0.2*int(freedom(gs))+0*int(KingPawnShield(gs))+(-0.7)*int(doublePawns(gs))+0.03*int(QueenMobililty(engine))+0.3*int(countWhitePiecesOnKingSurroundingSquares(gs))+0.3*int(KingMobililty(engine))
                if square[0] == "b":
                    score -= pieceScore[square[1]] + piece_position_score +0.6*int(gs.wcastled)+0.2*int(freedom(gs))+0.3*int(KingPawnShield(gs))+(-0.7)*int(doublePawns(gs))+0.03*int(QueenMobililty(engine))+0*int(countWhitePiecesOnKingSurroundingSquares(gs))+0.3*int(KingMobililty(engine))

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

def countWhitePiecesOnKingSurroundingSquares(gs):
    count = 0
    
    # get the king's position
    if gs.whitemove:
        king_row, king_col = gs.blackKingLocation
    else:
        king_row, king_col = gs.whiteKingLocation
    
    # check the 8 surrounding squares
    for row in range(king_row-1, king_row+2):
        for col in range(king_col-1, king_col+2):
            if isOnBoard(row, col):
                piece = gs.board[row][col]
                if piece[0] == 'w':
                    count += 1
    # print("White pieces on king surrounding squares",count)
    return count

def isOnBoard(row, col):
    return row >= 0 and row < 8 and col >= 0 and col < 8

def KingMobililty(engine):
    return len(engine.King_squares)

# def KingCastled(gs):
    # print("White King Castled",gs.wcastled)
    # print("Black King Castled",gs.bcastled)

def freedom(gs):
    # if gs.whitemove:
    #     return len(gs.getvalidmoves())
    # else:
        return len(gs.getvalidmoves())

def KingPawnShield(gs):
    global KingNeighbourPawns
    KingNeighbourPawns = 0
    # get the king's position
    if gs.whitemove:
        king_row, king_col = gs.blackKingLocation
    else:
        king_row, king_col = gs.whiteKingLocation
    
    # check the 8 surrounding squares
    for row in range(king_row-1, king_row+2):
        for col in range(king_col-1, king_col+2):
            if isOnBoard(row, col):
                piece = gs.board[row][col]
                if piece[0] == 'w' and piece[1] == 'p':
                    KingNeighbourPawns += 1
    # print("King Neighbour Pawns",KingNeighbourPawns)
    return KingNeighbourPawns

# determines the centre-pawn count at sq e4,d4,e5,d5
def centrePawnCount(gs):
    pawn = 0
    centerPawn = [(3,3),(3,4),(4,3),(4,4)] # list of tuples for row-col of sq d5,e5,d4,e4 resp
    for sq in centerPawn:
        if gs.board[sq[0]][sq[1]] == 'wp' :
            pawn+=1
        elif gs.board[sq[0]][sq[1]] == "bp" :
            pawn-=1
    return pawn

# determines whether knight is on sq a1 to a8,a8 to h8,a1 to h1 or h1 to h8
def knightPeriphery0(gs):
    kp0 = 0
    kp0list = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),
               (7,7),(6,7),(5,7),(4,7),(3,7),(2,7),(1,7),(0,7),(0,6),(0,5),(0,4),(0,3),(0,2),(0,1)]
    for sq in kp0list:
        if gs.board[sq[0]][sq[1]] == 'wN' :
            kp0+=1
        elif gs.board[sq[0]][sq[1]] == "bN" :
            kp0-=1
    return kp0

# determines whether knight is on sq b2 to b7,b7 to g7,b2 to g2,g2 to g7
def knightPeriphery1(gs):
    kp1 = 0
    kp1list = [(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(6,2),(6,3),(6,4),(6,5),
               (6,6),(5,6),(4,6),(3,6),(2,6),(1,6),(1,5),(1,4),(1,3),(1,2)]
    for sq in kp1list:
        if gs.board[sq[0]][sq[1]] == 'wN' :
            kp1+=1
        elif gs.board[sq[0]][sq[1]] == "bN" :
            kp1-=1
    return kp1

# determines whether knight is on sq c3 to c6,c6 to f6,c3 to f3,f3 to f6
def knightPeriphery2(gs):
    kp2 = 0
    kp2list = [(2,2),(3,2),(4,2),(5,2),(5,3),(5,4),
               (5,5),(4,5),(3,5),(2,5),(2,4),(2,3)]
    for sq in kp2list:
        if gs.board[sq[0]][sq[1]] == 'wN' :
            kp2+=1
        elif gs.board[sq[0]][sq[1]] == "bN" :
            kp2-=1
    return kp2

# determines whether knight is on sq e4,d4,e5,d5
def knightPeriphery3(gs):
    kp3 = 0
    kp3list = [(3,3),(3,4),(4,3),(4,4)] # list of tuples for row-col of sq d5,e5,d4,e4 resp
    for sq in kp3list:
        if gs.board[sq[0]][sq[1]] == 'wN' :
            kp3+=1
        elif gs.board[sq[0]][sq[1]] == "bN" :
            kp3-=1
    return kp3

# determines existence of double pawns
def doublePawns(gs):
    doublepawn = 0
    for r in range(8):
        for c in range(8):
            if gs.board[r][c] == 'wp':
                row = r
                for rows in range(row-1,0):
                    if gs.board[rows][c] == 'wp':
                        doublepawn+=1
            elif gs.board[r][c] == 'bp':
                row = r
                for rows in range(row+1,7):
                    if gs.board[rows][c] == 'bp':
                        doublepawn-=1
    return doublepawn


# determines whether the bishop pair exists
def bishopPair(gs):
    wbishop = 0
    bbishop = 0
    for r in range(8):
        for c in range(8):
            if gs.board[r][c] == 'wB': # counts no. of wB
                wbishop+=1
            elif gs.board[r][c] == 'bB': # counts no. of bB
                bbishop+=1
    if wbishop>1 or bbishop>1:
        return 1  

# determines whether rook is on Seventh rank wrt player
def rookOnSeventh(gs):
    rookSeventh = 0
    for col in range(8):
        if gs.board[1][col] == 'wR': # rank 7 for white
            rookSeventh+=1
        elif gs.board[6][col] == 'bR': # rank 2 for black
            rookSeventh-=1
    return rookSeventh

# determines whether bishop is on large diagonal
def bishopOnLarge(gs):
    bishopLarge = 0
    for r in range(8):
        # bishop on diagonal h1-a8  
        if gs.board[r][r] == "wB": 
            bishopLarge+=1
        elif gs.board[r][r] == "bB":
            bishopLarge-=1
        
        # bishop on diagonal a1-h8
        if gs.board[r][7-r] == "wB":
            bishopLarge+=1
        elif gs.board[r][7-r] == "bB":
            bishopLarge+=1 
    return bishopLarge

# determines whether knight is supported by a pawn ahead
def knightSupport(gs):
    knightsupport = 0
    for r in range(8):
        for c in range(8):
            if r>0 and r<7 and c>0 and c<7:
                if gs.board[r][c] == 'wN' and  (gs.board[r-1][c-1] == 'wp' or gs.board[r-1][c+1] == 'wp'):
                    knightsupport+=1
                elif gs.board[r][c] == 'bN' and  (gs.board[r+1][c-1] == 'bp' or gs.board[r+1][c+1] == 'bp'):
                    knightsupport-=1
    return knightsupport

# determine the score for a gamestate/board 
# using evaluation function parameters

def evaluationFunction():
    pass
