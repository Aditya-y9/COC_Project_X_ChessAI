class gamestate():
    def __init__(self):
        # 2D 8x8 list, each element has 2 characters.
        # The first character represents the color of the piece
        # The second character represents the type of the piece
        # "--" represents an empty space with no piece
        # "wp" represents a white pawn
        # "bR" represents a black rook
        # "bK" represents a black king
        # "wQ" represents a white queen
        # and so on
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        
        self.whitemove=True
        self.moveLog = []
    
    

    def makeMove(self,move):
        # make the move and update the board
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        # swap turns after move
        self.whitemove = not self.whitemove
    def undoMove(self):
        # to make sure that there is a move to undo
        if len(self.moveLog) != 0:
            # pop returns and removes the last element from the list
            move = self.moveLog.pop()

            self.board[move.startRow][move.startCol] = move.pieceMoved
            # undoing the move
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            # to make sure the piece captured is not empty
            # switch turns back
            self.whitemove = not self.whitemove

    # all moves considering checks
    def getvalidmoves(self):
        return self.getAllPossibleMoves()
    
    # all moves without considering checks
    def getAllPossibleMoves(self):

        # 
        


        # empty list for storing all possible moves 
        poss_moves = []
        # loop through all the squares in the board using nested for loop
        for rows in range(len(self.board)):
            for columns in range(len(self.board[rows])):

                # checking the first char of pieces
                # assigning moves to pieces according to their color
                turn = self.board[rows][columns][0]
                if (turn == 'w' and self.whitemove) or (turn == 'b' and not self.whitemove):
                    # if the piece is a pawn
                    # because each piece has its own set of rules
                    if self.board[rows][columns][1] == 'p':
                        self.getPawnMoves(rows,columns,poss_moves)
        return poss_moves

    def getPawnMoves(self,rows,columns,poss_moves):
        # if white pawn
        #
        if self.whitemove:
            # if the square in front of the pawn is empty
            if self.board[rows-1][columns] == "--":
                # going a row ahead not diagonal so column reamins the same
                poss_moves.append(Move((rows,columns),(rows-1,columns),self.board))

                # if the pawn is in its starting position
                # for pawns first move
                # we can move two squares ahead
                # so append move rows-2
                if rows == 6 and self.board[rows-2][columns] == "--":
                    poss_moves.append(Move((rows,columns),(rows-2,columns),self.board))
                    # mark this square by photo

            if columns-1 >= 0:
                if self.board[rows-1][columns-1][0] == 'b':
                    poss_moves.append(Move((rows,columns),(rows-1,columns-1),self.board))
            if columns+1 <= 7:
                if self.board[rows-1][columns+1][0] == 'b':
                    poss_moves.append(Move((rows,columns),(rows-1,columns+1),self.board))


class Move():
    # map position from rows and columns to ranks and files in chess


    # so using dictionaries to map
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,
                     "5":3,"6":2,"7":1,"8":0}
    
    # reversing the above dictionary
    rowsToRanks = {v:k for k,v in ranksToRows.items()}


    # using for converting columns to files
    filesToCols = {"a":0,"b":1,"c":2,"d":3,
                        "e":4,"f":5,"g":6,"h":7}
    colsToFiles = {v:k for k,v in filesToCols.items()}



    def __init__(self,start_sq,end_sq,board):
        # start_sq
        # source

        # end_sq
        # destination

        # board state passed to validate the move and store information about the move
        # what piece was captured? --> information

        # for first tuple that is sq_selected in player_clicks
        self.startRow = start_sq[0]
        self.startCol = start_sq[1]

        # for second tuple that is sq_selected in player_clicks
        self.endRow = end_sq[0]
        self.endCol = end_sq[1]

        # refers to pos in board
        self.pieceMoved = board[self.startRow][self.startCol] # piece moved
        
        # refers to pos in board
        self.pieceCaptured = board[self.endRow][self.endCol] # piece captured
        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
        print(self.moveID)
    

    def __eq__(self, other):
        # comparing this object to another object

        # to ensure that we are comparing two move objects and not some other class object
        if isinstance(other,Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        # you can add to make this like real chess notation
        return self.getRankFile(self.startRow,self.startCol) + self.getRankFile(self.endRow,self.endCol)
    
    def getRankFile(self,rows,columns):
        return self.colsToFiles[columns] + self.rowsToRanks[rows]