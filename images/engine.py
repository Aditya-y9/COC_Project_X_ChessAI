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
        