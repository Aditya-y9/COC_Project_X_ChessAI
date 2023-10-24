import random

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
    turnMultiplier = 1 if gs.whiteToMove else -1
    opponentMinMaxScore = float('inf')
    bestPlayerMove = None
    random.shuffle(validMoves)
    for playerMove in validMoves:
        gs.makeMove(playerMove)
        opponentMoves = gs.getValidMoves()
        opponentMaxScore = -float('inf')
        for opponentMove in opponentMoves:
            gs.makeMove(opponentMove)
            if gs.checkMate:
                score = -turnMultiplier * 10000
            elif gs.staleMate:
                score = -turnMultiplier * 5000
            else:
                score = -turnMultiplier * scoreMaterial(gs.board)
            if score > opponentMaxScore:
                opponentMaxScore = score
            gs.undoMove()
        if opponentMaxScore < opponentMinMaxScore:
            opponentMinMaxScore = opponentMaxScore
            bestPlayerMove = playerMove
        gs.undoMove()
    return bestPlayerMove
