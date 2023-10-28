# implement AI part in chess to find the best move
import random
import engine

# dic to assign piece values to all pieces except king as can't captured
pieceScore = {'K':0,'Q':10,'R':5,'B':3,'N':3,'p':1}


# parameters that influence positional chess
# achieved using 2d arrays
# mapping these positional scores with the respective pieces using dict

# for knights --> knights at centre are better than those at corners/edges
# attacking sq increases
# AI analyses it as better position 
knightScore = [[1,1,1,1,1,1,1,1],
               [1,2,2,2,2,2,2,1],
               [1,2,3,3,3,3,2,1],
               [1,2,3,4,4,3,2,1],
               [1,2,3,4,4,3,2,1],
               [1,2,3,3,3,3,2,1],
               [1,2,2,2,2,2,2,1],
               [1,1,1,1,1,1,1,1]]

# for bishops --> to get onto major diagonal better attacker
bishopScore = [[4,3,2,1,1,2,3,4],
               [3,4,3,2,2,3,4,3],
               [2,3,4,3,3,4,3,2],
               [1,2,3,4,4,3,2,1],
               [1,2,3,4,4,3,2,1],
               [2,3,4,3,3,4,3,2],
               [3,4,3,2,2,3,4,3],
               [4,3,2,1,1,2,3,4]]

# for queens(its not symmetrical) --> centralizing it quite good 
# queens moving directly diagonally from original pos
# to row 2 & 5 are more efficient(large influence)
queenScore =  [[1,1,1,3,1,1,1,1],
               [1,2,3,3,3,1,1,1],
               [1,4,3,3,3,4,2,1],
               [1,2,3,3,3,2,2,1],
               [1,2,3,3,3,2,2,1],
               [1,4,3,3,3,4,2,1],
               [1,1,2,3,3,1,1,1],
               [1,1,1,3,1,1,1,1]]

# for rooks --> rooks rather better on back ranks & row 1 & 6 
# quite active if centralized
rookScore =   [[4,3,4,4,4,4,3,4],
               [4,4,4,4,4,4,4,4],
               [1,1,2,3,3,2,1,1],
               [1,2,3,4,4,3,2,1],
               [1,2,3,4,4,3,2,1],
               [1,1,2,3,3,2,1,1],
               [4,4,4,4,4,4,4,4],
               [4,3,4,4,4,4,3,4]]

# for pawns --> it will work separately for w & b
# for wp --> moving towards row 0 is good & at also centralized are efficient
# for bp --> moving towards row 7 is good & at also centralized are efficient
# d ane e pawns ie col 3 & 4 should get centralized compulsory
# otherwise they act like just extra pawns
whitePawnScore = [[8,8,8,8,8,8,8,8],
                  [8,8,8,8,8,8,8,8],
                  [5,6,6,7,7,6,6,5],
                  [2,3,3,5,5,3,3,2],
                  [1,2,3,4,4,3,2,1],
                  [1,1,2,3,3,2,1,1],
                  [1,1,1,0,0,1,1,1],
                  [0,0,0,0,0,0,0,0]]

blackPawnScore = [[0,0,0,0,0,0,0,0],
                  [1,1,1,0,0,1,1,1],
                  [1,1,2,3,3,2,1,1],
                  [1,2,3,4,4,3,2,1],
                  [2,3,3,5,5,3,3,2],
                  [5,6,6,7,7,6,6,5],
                  [8,8,8,8,8,8,8,8],
                  [8,8,8,8,8,8,8,8]]



piecePositionScores = {'N':knightScore,'B':bishopScore, 'Q' :queenScore, 'R':rookScore,'bp': blackPawnScore,'wp':whitePawnScore}

# Assigning highest value to checkmate(desire)
CHECKMATE = 1000
# Assigning least value to stalemate(not desire)
STALEMATE = 0

DEPTH = 3 # depth of game tree

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


def findBestNegaMax(gs,valid_moves):

    # helper method used to make the initial(first) recursive call

    global nextMove,counter
    nextMove = None

    random.shuffle(valid_moves)
    counter = 0 # counts number of times method is called(gamestate)
    findMoveNegaMaxAlphaBeta(gs,valid_moves,DEPTH,-CHECKMATE, CHECKMATE, 1 if gs.whitemove else -1)
    # if white turn turnMultiplier --> 1
    # if black turn turnMultiplier --> -1
    # since alpha is technically max value
    # we initialize it to min value
    # since beta is technically min value
    # we initialize it to max value

    # And whenever both of these cross cond each other it breaks
    # cross the cond ie break case alpha>=beta
    print(counter)
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


def findMoveNegaMax(gs,valid_moves,depth,turnMultiplier):
    
    # Here instead of whiteMove boolean var
    # use turnMultiplier to identify the turn :
    # +1 --> white turn to move
    # -1 --> black turn to move
    # always select max value & multiply by turnMultiplier(ie -1 --> black)

    global nextMove
    if depth==0:
        return turnMultiplier*scoreBoard(gs)
    
    # using only 1 for loop and if statement
    # No need to check whose turn it is 
    # Algorithm works the same
    # call method recursively
    maxScore = -CHECKMATE
    for move in valid_moves:
        gs.makeMove(move)
        # generate next set of values
        nextMove = gs.getvalidmoves()

        # calc score
        score = -findMoveNegaMax(gs,nextMove,depth-1,-turnMultiplier)

        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move

        # call this method for opponent
        # so whatever their best score is that will be our worst score
        # -ve sign highlights switching from ply to ply

        gs.undoMove()
    return maxScore



def findMoveNegaMaxAlphaBeta(gs,valid_moves,depth,alpha,beta,turnMultiplier):
    
    # Here instead of whiteMove boolean var
    # use turnMultiplier to identify the turn :
    # +1 --> white turn to move
    # -1 --> black turn to move
    # always select max value & multiply by turnMultiplier(ie -1 --> black)

    
    # ****// ALPHA BETA PRUNING //*****
    # alpha --> upper bound val ie max possible score overall
    # beta --> lower bound val ie min possible score overall
    # if maxScore > alpha ---> alpha = maxScore
    # if at any pt alpha >= beta --> break out of tree
    # found a score that is better 
    # than any possible game state at that position we get 

    # to perform alpha beta pruning efficiently
    # use move ordering
    # want to evaluate best move first
    # then by knowing this we avoid looking into worst branches
    # move ordering - implement later

    global nextMove,counter
    counter+=1
    if depth==0:
        return turnMultiplier*scoreBoard(gs)
    
    # using only 1 for loop and if statement
    # No need to check whose turn it is 
    # Algorithm works the same
    # call method recursively
    maxScore = -CHECKMATE
    for playerMove in valid_moves:
        gs.makeMove(playerMove)
        # generate next set of values
        nextMove = gs.getvalidmoves()

        # calc score
        score = -findMoveNegaMaxAlphaBeta(gs,nextMove,depth-1,-beta,-alpha,-turnMultiplier)
        
        # switch alpha & beta through each frame
        # -ve beta becomes new alpha(max)
        # -ve alpha becomes new beta(min)
        # it is min that becomes opponents new max
        # it is max that becomes opponents new min
        # max & min passed lvl by lvl

        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = playerMove
                print(playerMove,score)

        # call this method for opponent
        # so whatever their best score is that will be our worst score
        # -ve sign highlights switching from ply to ply

        gs.undoMove()

        # actual pruning happens
        if maxScore > alpha:
            alpha = maxScore
        if alpha >= beta: 
            # break case no need to evaluate further
            # it isimpossible or the worst case
            break

    return maxScore






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
    for r in range(len(gs.board)): # r : 0 --> 8
        for c in range(len(gs.board[r])): # c : 0 --> 8
            square = gs.board[r][c]
            # piece & its color

            if square != '--': # if sq consists of piece
                
                # scoring positionally ie weights
                # significance of weights should be determined by own
                # finding piece and mapping with its positional score by dict & r,c
                piecePositionScore = 0
                if square[1] != 'K': # pieces other than king for position score
                    if square[1] == 'p': # for pawn position score
                        piecePositionScore = piecePositionScores[square][r][c]
                    else : # for other pieces position score
                        piecePositionScore = piecePositionScores[square[1]][r][c]
                if square[0] == 'w':
                    score += pieceScore[square[1]] + piecePositionScore*0.1
                    # sq has white piece add pieceScore 
                elif square[0] == 'b':
                    score -= pieceScore[square[1]] + piecePositionScore*0.1
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