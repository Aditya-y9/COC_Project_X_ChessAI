import pygame
import chess
import os
from pygame.locals import *
from sys import exit
pygame.init()
WIDTH = 512 # dimensions of the game window
HEIGHT = 512 # global declaration in caps
screen = pygame.display.set_mode((WIDTH,HEIGHT),0 ,32)
pygame.display.set_caption("Chess")
SIZE = WIDTH // 8 # dimensions of square('//8' is 8*8)
image = {} # creating dict to store the images along with some key such as its abbreviation (color_piece)
class GameState: # Designing Board, Valid Moves
    def __init__(self): #Designing the board layout by declaring a list within another list
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.whitetomove = True
        self.movelog = []
        self.whiteKingLocation = (7,4) # initial pos of white & black kings
        self.blackKingLocation = (0,4)
        self.Checkmate = False
        self.Stalemate = False
        self.enpassantPossible = () # Co-ordinates for the square an en passant pawn capture is possible
        # Takes move as a parameter and executes the move( does not work for castling,pawn promotion and en-passant pawns)
        # to keep a track of  current castling rights
        self.currentCastlingRight = CastlingRights(True,True,True,True)
        # Just to check whether any right is broken we use
        # To check whether undoing a move is changing castling rights
        self.castleRightLog = [CastlingRights(self.currentCastlingRight.wks,self.currentCastlingRight.bks,
                                              self.currentCastlingRight.wqs,self.currentCastlingRight.bqs)]
        # To update the list we instead of appending it each time will create multiple references
        # We create copy of CastlingRights in castleRightLog consists of only one reference
    def makeMove(self,move): # To make a move we create an object move of a class Move
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.piecemoved
        self.movelog.append(move) # move log so as to undo the current move
        self.whitetomove = not self.whitetomove # To swap the turn
        # updating the king's location if it is moved
        if move.piecemoved == 'wK':
            self.whiteKingLocation = (move.endrow,move.endcol)
        elif move.piecemoved == 'bK':
            self.blackKingLocation = (move.endrow,move.endcol)
        #pawn promotion

        # Enpassant
        if move.enpassantPossible:
            self.board[move.startrow][move.endcol] = '--' # capturing the pawn as both the pawns(ie wp & bp) are on same row only diff by col
        # updating enpassantPossible variable
        if move.piecemoved[1] == 'p' and abs(move.startrow - move.endrow) == 2 : # only for 2 square pawn moves
            # first co-ordinate : average of the two squares of start row and end row
            self.enpassantPossible = ((move.startrow + move.endrow)//2,move.startcol)
        else:
            self.enpassantPossible = () # Resetting it

        # Castling move
        if move.castleMove:
            if move.endcol - move.startcol == 2 : # kingside castling move
               self.board[move.endrow][move.endcol-1] = self.board[move.endrow][move.endcol+1] # makes rook move
               self.board[move.endrow][move.endcol+1] = '--' # erases old rook
            else : # queenside castling move
                self.board[move.endrow][move.endcol + 1] = self.board[move.endrow][move.endcol - 2]  # makes rook move
                self.board[move.endrow][move.endcol - 2] = '--'  # erases old rook

        # updating castling rights - whenever there is a rook or a king move
        self.updateCastleRights(move)
        self.castleRightLog.append(CastlingRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                              self.currentCastlingRight.wqs, self.currentCastlingRight.bqs))
    # Undoing the move
    def undoMove(self):
        if len(self.movelog) != 0: # checking that there is a move to undo
            move = self.movelog.pop() # removes and returns the current move from movelog
            self.board[move.startrow][move.startcol] = move.piecemoved # places the moved piece to previous position
            self.board[move.endrow][move.endcol] = move.piececaptured # places the captured piece back to its previous position
            self.whitetomove = not self.whitetomove # Switches the turn once again so player can make a move after undoing
            # update the king's position if needed
            if move.piecemoved == 'wK':
                self.whiteKingLocation = (move.endrow,move.endcol)
            elif move.piecemoved == 'bK':
                self.blackKingLocation = (move.endrow,move.endcol)
            # undoing enpassant move
            if move.enpassantPossible:
                self.board[move.endrow][move.endcol] = "--" # leaving the square we had landed on blank
                self.board[move.startrow][move.endcol] = move.piececaptured
                self.enpassantPossible = (move.endrow,move.endcol)
            # undoing 2 sq pawn advance move
            if move.piecemoved[1] =='p' and abs(move.startrow - move.endrow) == 2:
                self.enpassantPossible = ()

            # undoing castling rights
            # removing the newly added CastlingRights
            self.castleRightLog.pop()
            self.currentCastlingRight = self.castleRightLog[-1]
            # undo castle move (undoes rook castle move)
            if move.castleMove:
                if move.endcol - move.startcol == 2:  # undoes kingside castling
                    self.board[move.endrow][move.endcol + 1] = self.board[move.endrow][move.endcol - 1]  # generates old rook
                    self.board[move.endrow][move.endcol - 1] = '--'  # erases new rook
                else:  # undoes queenside castling move
                    self.board[move.endrow][move.endcol - 2] = self.board[move.endrow][move.endcol + 1]  # generates old rook
                    self.board[move.endrow][move.endcol + 1] = '--'  # erases new rook
                self.Checkmate = False
                self.Stalemate = False
            # restoring the previously CastlingRights before undoes move
            # updating current one with the previous rights fetched

    def updateCastleRights(self,move): # checking the conditions of move and updating
        if move.piecemoved == 'wK':
            self.currentCastlingRight.wks = False
            self.currentCastlingRight.wqs = False
        elif move.piecemoved == 'bK':
            self.currentCastlingRight.bks = False
            self.currentCastlingRight.bqs = False
        elif move.piecemoved == 'wR':
            if move.startrow == 7:
                if move.startcol == 0: # (left rook)white queen side castling not possible
                    self.currentCastlingRight.wqs = False
                elif move.startcol == 7: # (right rook)white king side castling not possible
                    self.currentCastlingRight.wks = False
        elif move.piecemoved == 'bR':
            if move.startrow == 0:
                if move.startcol == 0: # (left rook)black queen side castling not possible
                    self.currentCastlingRight.bqs = False
                elif move.startcol == 7: # (right rook)black king side castling not possible
                    self.currentCastlingRight.bks = False
    def getValidMoves(self):

        tempEnpassantPossible = self.enpassantPossible # to store it temporarily
        tempCastlingRights = CastlingRights(self.currentCastlingRight.wks,self.currentCastlingRight.bks,
                                            self.currentCastlingRight.wqs,self.currentCastlingRight.bqs)
        # all moves considering the checks
        # using naive algorithm
        # 1) generate all possible moves
        moves = self.getAllPossibleMoves()
        # To avoid the recursion of castling move we add it here directly in valid move
        if self.whitetomove:
            self.getCastleMoves(self.whiteKingLocation[0],self.whiteKingLocation[1],moves)
        else:
            self.getCastleMoves(self.blackKingLocation[0], self.blackKingLocation[1],moves)
        # 2) for each move make a move
        # we will traverse the list in reverse dir using for loop as if we remove the element in this fashion none of the index will be skipped even after removal of item
        # eg. [ 1, 2 ,3 ,4] while removing 2 the index will traverse directly to the next index in reverse way even after the removal arrangement shift
        for i in range(len(moves)-1, -1, -1):
            self.makeMove(moves[i])
        # 3) generate all opponents move
        # 4) for each of your opponents move check if they attack your king
            # firstly it will swap the turn(white) to opponent(black) then it checks whether blacks king is in check ie wrong
            # Once again swap turn
            self.whitetomove = not self.whitetomove
            if self.inCheck(): # the king is attacked so remove that move
                moves.remove(moves[i]) # not a valid move
        # 5) if they attack your king not a valid move
            self.whitetomove = not self.whitetomove
            self.undoMove()
        if len(moves) == 0 : #there are no valid moves ie condition of checkmate/stalemate
            if self.inCheck(): # king has a check
                self.Checkmate = True
            else:
                self.Stalemate = True
        else : # to set the values by default to False
            self.Stalemate = False
            self.Checkmate = False

        self.enpassantPossible = tempEnpassantPossible
        self.currentCastlingRight = tempCastlingRights # making and undoing a move can change current castling rights
        return moves

    def inCheck(self): # determines whether the current player has a check
        if self.whitetomove:
            return self.squareUnderAttack(self.whiteKingLocation[0],self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0],self.blackKingLocation[1])
    def squareUnderAttack(self,r,c): # determines/checks whether the enemy can attack square r,c
        # swap the turn first
        self.whitetomove = not self.whitetomove
        oppmove = self.getAllPossibleMoves()
        self.whitetomove = not self.whitetomove # Once again return to the previous turn(switch back) so as to go sequentially
        for move in oppmove:
            if move.endrow==r and move.endcol==c: # the square is under attack
                return True
        return False # set it to default False

    #Here we consider all possible moves first and then check for valid moves acc
    def getAllPossibleMoves(self):# all possible moves without considering check cond
        possMoves = []
        for r in range(len(self.board)): # number of rows
            for c in range(len(self.board[r])): # no of col in a certain row
                color = self.board[r][c][0] # like in board[r][c] the elements are strings eg : 'bB' ie black bishop
                if (color== 'w' and self.whitetomove) or (color=='b' and not self.whitetomove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r,c,possMoves)
                    elif piece == 'R':
                        self.getRookMoves(r,c,possMoves)
                    elif piece == 'B':
                        self.getBishopMoves(r,c,possMoves)
                    elif piece == 'Q':
                        self.getQueenMoves(r,c,possMoves)
                    elif piece == 'N':
                        self.getKnightMoves(r,c,possMoves)
                    elif piece == 'K' :
                        self.getKingMoves(r, c, possMoves)
        return possMoves
    def getPawnMoves(self,r,c,possMoves):# gets all the pawn moves for the pawn located at a certain row and column and adds it to the moves[].
        if self.whitetomove: #if white to move
            if self.board[r-1][c] == "--": # if the 1 square in front of wpawn is empty it can make a 1 sq wpawn move
                possMoves.append(Move((r,c),(r-1,c),self.board))
                if r == 6 and self.board[r-2][c] == "--": # if the wpawn is on row 6 and the 2sq in its front are vacant then make a 2 sq wpawn move
                    possMoves.append(Move((r,c),(r-2,c),self.board))
            if c-1>=0: # wpawn capturing pieces in diagonally left
                if self.board[r-1][c-1][0] == 'b': # to capture black pieces
                    possMoves.append(Move((r,c),(r-1,c-1),self.board))
                elif (r,c-1) == self.enpassantPossible:
                    possMoves.append(Move((r, c), (r - 1, c - 1), self.board, enpassantPossible=True)) # usage of optional parameter
            if c+1<=7: # wpawn capturing pieces in diagonally right
                if self.board[r-1][c+1][0] == 'b': # to capture black pieces
                    possMoves.append(Move((r,c),(r-1,c+1),self.board))
                elif (r,c+1) == self.enpassantPossible:
                    possMoves.append(Move((r, c), (r - 1, c + 1), self.board, enpassantPossible=True)) # usage of optional parameter
        else: # black to move
            if self.board[r+1][c] == "--": # if the 1 square in front of bpawn is empty it can make a 1 sq bpawn move
                possMoves.append(Move((r,c),(r+1,c),self.board))
                if r == 1 and self.board[r+2][c]=="--":# if the bpawn is on row 1 and the 2sq in its front are vacant then make a 2 sq bpawn move
                    possMoves.append(Move((r,c),(r+2,c),self.board))
            if c-1>=0: # bpawn capturing pieces in diagonally left
                if self.board[r+1][c-1][0] == 'w': # to capture white pieces
                    possMoves.append(Move((r,c),(r+1,c-1),self.board))
                elif (r,c-1) == self.enpassantPossible:
                    possMoves.append(Move((r, c), (r + 1, c - 1), self.board, enpassantPossible=True)) # usage of optional parameter
            if c+1<=7: # bpawn capturing pieces in diagonally right
                if self.board[r+1][c+1][0] == 'w': # to capture white pieces
                    possMoves.append(Move((r,c),(r+1,c+1),self.board))
                elif (r,c+1) == self.enpassantPossible:
                    possMoves.append(Move((r, c), (r + 1, c + 1), self.board, enpassantPossible=True)) # usage of optional parameter
    def getRookMoves(self,r,c,possMoves):# gets all the rook moves for the rook located at a certain row and column and adds it to the list of moves.
        direction = ((-1,0),(1,0),(0,-1),(0,1))# down,up,left,right it mentions direction in which rook moves
        if self.whitetomove:
            enemypiececolor = 'b'
        else:
            enemypiececolor = 'w'
        for d in direction:
            for i in range(1,8): # as the rook will possibly make a move anywhere from the 1st square to 7th square before it
                endRow = r + d[0]*i # gives the row pos of the final rook move
                endCol = c + d[1]*i # gives the col pos of the final rook move
                if 0<=endRow<8 and 0<=endCol<8 : # this cond is within the board
                    endPiece = self.board[endRow][endCol]  # gives the info about piece present at final pos like bB,wp
                    if endPiece == "--" : # at final pos piece not exists
                        possMoves.append(Move((r,c),(endRow,endCol),self.board))
                    elif endPiece[0] == enemypiececolor : # at final pos the enemy's piece exists
                        possMoves.append(Move((r,c),(endRow,endCol),self.board))
                        break
                    else : # at final pos same color piece exists
                        break
                else: # final pos is out of board
                    break
    def getKnightMoves(self,r,c,possMoves):# gets all the knight moves for the knight located at a certain row and column and adds it to the list of moves.
        direction = ((-2, -1), (2, -1), (-2, 1),(2, 1),(-1,2),(1,2),(-1,-2),(1,-2))  # it mentions direction in which knight moves
        if self.whitetomove:
            enemypiececolor = 'b'
        else:
            enemypiececolor = 'w'
        for d in direction:
                endRow = r + d[0]  # gives the row pos of the final knight move
                endCol = c + d[1]  # gives the col pos of the final knight move
                if 0 <= endRow < 8 and 0 <= endCol < 8:  # this cond is within the board
                    endPiece = self.board[endRow][endCol]  # gives the info about piece present at final pos like bB,wp
                    if endPiece == "--" or endPiece[0] == enemypiececolor:  # at final pos piece not exists or enemy piece exists
                        possMoves.append(Move((r, c), (endRow, endCol), self.board))
    def getBishopMoves(self,r,c,possMoves):# gets all the bishop moves for the bishop located at a certain row and column and adds it to the list of moves.
        direction = ((-1,-1),(1,-1),(-1,1),(1,1))# left-up,left-down,right-up,right-down it mentions direction in which bishop moves
        if self.whitetomove:
            enemypiececolor = 'b'
        else:
            enemypiececolor = 'w'
        for d in direction:
            for i in range(1,8): # as the bishop will possibly make a move anywhere from the 1st square to 7th square lying before it
                endRow = r + d[0]*i # gives the row pos of the final bishop move
                endCol = c + d[1]*i # gives the col pos of the final bishop move
                if 0<=endRow<8 and 0<=endCol<8 : # this cond is within the board
                    endPiece = self.board[endRow][endCol]  # gives the info about piece present at final pos like bB,wp
                    if endPiece == "--" : # at final pos piece not exists
                        possMoves.append(Move((r,c),(endRow,endCol),self.board))
                    elif endPiece[0] == enemypiececolor : # at final pos the enemy's piece exists
                        possMoves.append(Move((r,c),(endRow,endCol),self.board))
                        break
                    else : # at final pos same color piece exists
                        break
                else: # final pos is out of board
                    break
    def getQueenMoves(self,r,c,possMoves):# gets all the queen moves for the queen located at a certain row and column and adds it to the list of moves.
        direction = ((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,-1),(-1,1),(1,1))# down,up,right,left,left-up,left-down,right-up,right-down it mentions direction in which queen moves
        if self.whitetomove:
            enemypiececolor = 'b'
        else:
            enemypiececolor = 'w'
        for d in direction:
            for i in range(1,8): # as the queen will possibly make a move anywhere from the 1st square to 7th square lying before it
                endRow = r + d[0]*i # gives the row pos of the final queen move
                endCol = c + d[1]*i # gives the col pos of the final queen move
                if 0<=endRow<8 and 0<=endCol<8 : # this cond is within the board
                    endPiece = self.board[endRow][endCol]  # gives the info about piece present at final pos like bB,wp
                    if endPiece == "--" : # at final pos piece not exists
                        possMoves.append(Move((r,c),(endRow,endCol),self.board))
                    elif endPiece[0] == enemypiececolor : # at final pos the enemy's piece exists
                        possMoves.append(Move((r,c),(endRow,endCol),self.board))
                        break
                    else : # at final pos same color piece exists
                        break
                else: # final pos is out of board
                    break
    def getKingMoves(self,r,c,possMoves):
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1))  # down,up,right,left,left-up,left-down,right-up,right-down it mentions direction in which king moves
        allyColor = 'w' if self.whitetomove else 'b'
        if self.whitetomove:
            enemypiececolor = 'b'
        else:
            enemypiececolor = 'w'
        for i in range(8): # we have not mentioned std cond 'for i in direction' since we are considering check conditions
            endRow = r + direction[i][0]  # gives the row pos of the final king move
            endCol = c + direction[i][1]  # gives the col pos of the final king move
            if 0 <= endRow < 8 and 0 <= endCol < 8:  # this cond is within the board
                endPiece = self.board[endRow][endCol]  # gives the info about piece present at final pos like bB,wp
                if endPiece == "--" or endPiece == enemypiececolor :  # at final pos piece not exists or enemy piece exists
                    possMoves.append(Move((r, c), (endRow, endCol), self.board))


    def getCastleMoves(self,r,c,possMoves):
        if self.squareUnderAttack(r,c):
            return # can't castle while in check
        if (self.whitetomove and self.currentCastlingRight.wks) or (not self.whitetomove and self.currentCastlingRight.bks):
            # when its w/b turn and kingside castling right is valid
            self.getKingsideCastleMoves(r,c,possMoves)
        if (self.whitetomove and self.currentCastlingRight.wqs) or (not self.whitetomove and self.currentCastlingRight.bqs):
            # when its w/b turn and queenside castling right is valid
            self.getQueensideCastleMoves(r, c, possMoves)
    # king is neither in check on both side
    # sq btwn are empty
    # neither of the empty sq are under attack
    def getKingsideCastleMoves(self,r,c,possMoves): # checks for the kingside castling moves
        if self.board[r][c+1] == '--' and self.board[r][c+2] == '--': # check that 2 sq are vacant
            if not self.squareUnderAttack(r,c+1) and not self.squareUnderAttack(r,c+2):
                possMoves.append(Move((r,c),(r,c+2),self.board,castleMove = True))

    def getQueensideCastleMoves(self,r,c,possMoves): # checks for the queenside castling moves
        if self.board[r][c-1] == '--' and self.board[r][c-2] == '--' and self.board[r][c-3] == '--': # check that 3 sq are vacant
            if not self.squareUnderAttack(r,c-1) and not self.squareUnderAttack(r,c-2) :
                possMoves.append(Move((r,c),(r,c-2),self.board,castleMove = True))



class CastlingRights(): # This class provides to store the current state of castling rights and update them when we make a move
    def __init__(self, wks, bks, wqs, bqs):
        self.wks = wks # white king side
        self.bks = bks # black king side
        self.wqs = wqs # white queen side
        self.bqs = bqs # black queen side
class Move:
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0} # Ranks represent horizontal rows(1-8)
    rowsToRanks = { v:k for k,v in ranksToRows.items()}
    filesToCols = {"h": 7, "g": 6, "f": 5, "e": 4, "d": 3, "c": 2, "b": 1, "a": 0} # Files represent vertical columns(a-h)
    colsToFiles = {v: k for k, v in filesToCols.items()}
    def __init__(self, startsq, endsq, board, enpassantPossible = False,castleMove = False): # passed as parameters
        self.startrow = startsq[0]  # enpassantPossible is an optional parameter which is not applicable to all moves
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piecemoved = board[self.startrow][self.startcol]
        self.piececaptured = board[self.endrow][self.endcol]
        #En passant
        self.enpassantPossible = enpassantPossible
        if self.enpassantPossible:
            self.piececaptured = 'wp' if self.piecemoved == 'bp' else 'bp'
        #Castling
        self.castleMove = castleMove

        self.moveId = self.startrow * 1000 + self.startcol*100 + self.endrow * 10 + self.endcol # generates a move Id which is unique for every move.
        print(self.moveId)
    def __eq__(self,other):# this is called overriding equals method it compares one object with the another
        if isinstance(other,Move):
            return self.moveId == other.moveId
    def getMoveNotation(self):
        return self.piecemoved + ' to ' + (self.getRankFile(self.startrow,self.startcol) + self.getRankFile(self.endrow,self.endcol))
    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

def load_img(): # to load all the images & access them using dict
    piece = ['bB','bK','bN','bp','bQ','bR','wK','wB','wN','wp','wQ','wR']
    for x in piece:
        image_path = os.path.join(r"C:\python\Chess\drive-download-20230913T164046Z-001", x + ".png")
        image[x] = pygame.transform.scale(pygame.image.load(image_path), (SIZE, SIZE))
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    clock = pygame.time.Clock()
    fps = 15
    obj = GameState()
    validmoves = obj.getValidMoves()
    moveMade = False # var which acts as flag var which prompts when move is made/once its done.
    load_img()
    selSq = ()  # it is tuple used to store the x and y co-ordinates of the selected square
    playerMove = []  # it is list used to store the tuple for selected square once while selecting from which sq and then while dropping to which square, ie 2 items
     # while calling the method(func) we attach the obj to that var 'board' and pass it as a parameter
    while True: # game loop
        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                col = x//SIZE
                row = y//SIZE
                if selSq == (row,col):
                    selSq = ()
                    playerMove = []
                else :
                    selSq = (row,col)
                    playerMove.append(selSq)
                    if len(playerMove) == 2 :
                        move = Move(playerMove[0],playerMove[1],obj.board)
                        print(move.getMoveNotation())
                        for i in range(len(validmoves)):# Since this is the move suggested by the chess engine
                            if move == validmoves[i]:
                                obj.makeMove(validmoves[i])
                                moveMade = True
                            # Resetting the squares selected by user
                                selSq = ()
                                playerMove = []
                        if not moveMade:
                            playerMove = [selSq]

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z: # to undo the move press 'z'
                    obj.undoMove()
                    moveMade = True
        if moveMade:
            validmoves = obj.getValidMoves() # generate valid moves for the next turn
            moveMade = False
        drawGameState(screen,obj.board)
        clock.tick(fps)
        pygame.display.update()
def drawGameState(screen,obj):
    def draw_board(screen):  # draw the 8*8 board of squares # the top left sq is white
        for r in range(0,8):  # if the sum of the row no & column no is even then its white whereas if sum is odd its black
            for c in range(0, 8):
                if (r + c) % 2 == 0:
                    pygame.draw.rect(screen, (255, 255, 255), [c * SIZE, r * SIZE, SIZE, SIZE])
                else:
                    pygame.draw.rect(screen, (128, 128, 128), [c * SIZE, r * SIZE, SIZE, SIZE])


    def draw_pieces(screen,obj):  # draw the pieces on resp sq on board & board ie list(var) is pass as a parameter to method draw_pieces
        for r in range(0, 8):
            for c in range(0, 8):
                piece = obj[r][c]
                if piece != "--":  # piece != " " it will draw the piece within req dim
                    screen.blit(image[piece],(c * SIZE, r * SIZE))
    draw_board(screen)
    draw_pieces(screen,obj)


if __name__ == "__main__": # convention of calling a main func
    main()
''' 
 Naive algorithm :
 1) generate all possible moves
 2) for each move make a move
 3) generate all opponents move
 4) for each of your opponents move check if they attack your king
 5) if they attack your king not a valid move
 Advanced algorithm :
 1) Check if the king is in check by any of the pieces traversing all the directions horizontal,vertical,diagonal
 2) Check if any of the piece is pinned to king through enemy's piece
 3) Check is there a double check
'''


