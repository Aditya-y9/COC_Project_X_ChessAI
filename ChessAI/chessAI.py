# implement AI part in chess to find the best move
import random

# dic to assign piece values to all pieces except king as can't captured
pieceScore = {'K':0,'Q':10,'R':5,'B':3,'N':3,'p':1}

# Assigning highest value to checkmate(desire)
CHECKMATE = 1000
# Assigning least value to stalemate(not desire)
STALEMATE = 0

DEPTH = 2 # depth of game tree

# Goal to find best move
# So wrt white jyada se jyada +ve score --> best
# wrt black jyada se jyada -ve score --> best


# firstly to find a random move

def findRandomMove(valid_moves):
    return valid_moves[random.randint(0,len(valid_moves)-1)]
    # to access valid move
    # random.randint(a,b) : includes even b as well
    # index should range 1 less than list len

# to find best move based on material alone
def findBestMove(gs,valid_moves):
    # follows greedy algorithm thinking best for us only 
    # looks for one move ahead 
    # not thinking of the opponents move at our turn
    # dominate kaise karte hain by capturing pieces and having piece value
    
    # if considering black as an AI
    # for b start with worst possible score(ie +ve CHECKMATE) as maxscore
    # finally continue upto best possible score for b(ie -ve CHECKMATE)
    # to deal with turn ie w and b as per above convention of + & -
    # introduce turn multiplier


    turnMultiplier = 1 if gs.whitemove else -1 
    # initialize maxscore = -CHECKMATE
    # to co-relate for both w & b to obtain highest score(not +/-)


    # ****  consider player as an AI  ****

    opponentMinMaxScore = CHECKMATE
    # initialize opponentMinMaxScore to max value
    # we have to minimise this opponentMinMaxScore  
    bestPlayerMove = None

    random.shuffle(valid_moves)
    # shuffle the players move since if there is no capture move possible
    # it will take move from valid_moves lisT
    # it will repeat certain move for each turn of AI until there is a chance of capture
    # shuffling avoids this


    for playerMove in valid_moves:
        gs.makeMove(playerMove)

        # for each of players move get the opponents moves
        opponentMoves = gs.getvalidmoves()

        # if move played by AI(player) leads to stalemate
        # no opponent moves 
        # no need to calc the score
        if gs.stalemate:
            opponentsMaxScore = STALEMATE

        # if move played by AI(player) leads to checkmate
        # no opponent moves 
        # no need to calc the score
        elif gs.checkmate:
            opponentsMaxScore = -CHECKMATE

        # else option
        # if move played by AI(player) dont leads to stale/checkmate
        else:
            # for opponents move
            opponentsMaxScore = -CHECKMATE
            # we initialize opponentsMaxScore with a very -ve score
            # getting opponents best move 
            # from the state of move we have given
            for opponentMove in opponentMoves:
                gs.makeMove(opponentMove)
                # after making a move we check for board's score
                # compare with maxscore
                if gs.checkmate:
                    score = CHECKMATE # consider checkmate
                elif gs.stalemate:
                    score = STALEMATE # consider stalemate
                else:
                    score = -turnMultiplier*scoreMaterial(gs.board)
                if score > opponentsMaxScore:
                    opponentsMaxScore = score # updates score
                gs.undoMove()
                # undo the opponents move
                # joh line 86 pe kiya hain
                # goes through all opponents move 
                # finds best opp move & highest score obtained for it
        if opponentsMaxScore < opponentMinMaxScore :
            # minimising opponents score 
            
            # */*/*/*/*/*/*/*/*
            # here we only check for depth == 2 
            # ie only 2 moves ahead
            # inner for loop :
            # hum log opp move lete hain 
            # set karte hain low value ko
            # sabse high value move find karte hain
            # aur vo opponentsMaxScore se jyada ho toh replace karte
            # outer for loop :
            # toh abhi hum apne moves check karte hain
            # apne har move ke liye opponent ka max response kya hain dekhte
            # agar opponentsMaxScore, opponentMinMaxScore se less hain
            # so minimising opponents score
            # toh hum opponentMinMaxScore ko replace karte hain by opponentsMaxScore
            # aur apne ko best minimised move mil jaata hain
            opponentMinMaxScore = opponentsMaxScore
            bestPlayerMove = playerMove
        # before making best move undo previously made players move
        # joh line 60 pe kiya hain
        gs.undoMove()

    return bestPlayerMove
    # playermove is the current players move
    # opponentmove is the other players move


def findBestMoveMinMax(gs,valid_moves):

    # helper method used to make the initial(first) recursive call

    global nextMove
    nextMove = None
    findMoveMinMax(gs,valid_moves,DEPTH,gs.whitemove)
    return nextMove


def findMoveMinMax(gs,valid_moves,depth,whitemove):

    # using MinMax algorithm Recursively
    # here we can check for depth upto which we want 
    # as we mention value to DEPTH var

    # depth : how deep u want to go before it closes
    # how many moves deep we go into the game tree
    # before returning best move

    # boolean var to say which players turn
    # if player 1 turn --> True
    # if player 2 turn --> False
    
    # as we are going to call function recursively
    # use global variables 

    # to declare global variable
    global nextMove

    # if we reach depth zero or
    # if we reach state of the board ie check/stalemate
    # Terminal node is reached & at that pt, return score
    if depth == 0:
        return scoreMaterial(gs.board)

    # one if for player 1 another if for player 2 
    # generally white tries to maximize score
    # black tries to minimize score

    if whitemove:
        maxScore = -CHECKMATE 
        # start with worst(min) score possible & then maximize
        for move in valid_moves:
            gs.makeMove(move)
            nextMove = gs.getvalidmoves()
            score = findMoveMinMax(gs,nextMove,depth-1,False) # whitemove == False
            
            # maximising the score :
            if score > maxScore:
                maxScore = score

                # if at the uppermost depth
                # at the top call ie first call(actual set of moves)
                # to come back by calc score to the best move up
                if depth == DEPTH:
                # searched all possibilities below it of tree
                # find best score for that branch & becomes nextMove
                # better score in another branch then it becomes nextMove
                    nextMove = move
            gs.undoMove()
            # undo the move made previously
        return maxScore    

    else:
        minScore = CHECKMATE
        # start with (max) score possible & then minimize
        for move in valid_moves:
            gs.makeMove(move)
            nextMove = gs.getvalidmoves()
            score = findMoveMinMax(gs,nextMove,depth-1,True) # whitemove == True

            # minimising the score :
            if score < minScore:
                minScore = score

                # if at the uppermost depth
                # at the top call ie first call(actual set of moves)
                # to come back by calc score to the best move up
                if depth == DEPTH:
                # searched all possibilities below it of tree
                # find best score for that branch & becomes nextMove
                # better score in another branch then it becomes nextMove
                    nextMove = move
            gs.undoMove()
            # undo the move made previously
        return minScore    



# determine score of board based on material,checkmate and stalemate cond
# +ve score good for white ; -ve score good for black

def scoreBoard(gs):
    
    # we should check for the cond of Stale/Checkmate before calc score
    if gs.checkmate:
        if gs.whitemove: 
            # if its checkmate & now its white to move so bad for white
            return -CHECKMATE # black wins
        else:
            # if its checkmate & its black to move so bad for black
            return CHECKMATE # white wins
    
    elif gs.stalemate:
        return STALEMATE

    score = 0
    for r in gs.board:
        for square in r:
            if square[0] == 'w':
                score += pieceScore[square[1]]
                # sq has white piece add pieceScore 
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
                # sq has black piece sub pieceScore
    return score





# determine score of board based on material

def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
                # sq has white piece add pieceScore 
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
                # sq has black piece sub pieceScore
    return score