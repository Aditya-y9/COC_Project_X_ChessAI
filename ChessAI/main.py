import pygame as p
import engine , AI
# import cv2
import numpy as np
import os
# import main1 as m
# import tester as tt
# import gtts
import time

# # this function will read all persons' training images, detect face from each image
# # used to load an image from a file
# test_img = cv2.imread(r"C:\Users\MSHOME\Desktop\Newfolder\FaceRecognition\Images\Akshay.jpg")
# # vid = cv2.VideoCapture(r"C:\Users\MSHOME\Desktop\Newfolder\FaceRecognition\video\Video.mp4")
# # running = True
# # while running:
# #     success, frame = vid.read()
# #     resized_img = cv2.resize(frame, (1000,700))
# #     faces_detected, gray_img = m.faceDetection(resized_img)
# #     for(x,y,w,h) in faces_detected:
# #         cv2.rectangle(resized_img, (x,y), (x+w, y+h), (255,102,0), thickness=2, lineType=8, shift=0)
# #     cv2.imshow("face detection tutorial", resized_img)
# #     cv2.waitKey(1)

# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# # vid.release()
# # cv2.destroyAllWindows()

# # detect faces from test image

# # collect the rectangles returned by faceDetection function
# # # collect the gray image returned by faceDetection function
# faces_detected, gray_img = m.faceDetection(test_img)

# # print("faces_detected:", faces_detected)

# # for(x,y,w,h) in faces_detected:
# #     cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,102,0), thickness=2, lineType=2, shift=0

# # resized_img = cv2.resize(test_img, (1000,700))
# # cv2.imshow("face detection tutorial", resized_img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # faces, faceID = m.labels_for_training_data(r"C:\Users\MSHOME\Desktop\Newfolder\FaceRecognition\TrainingImages")
# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read(r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\trainingData2.yml")
# # face_recognizer = m.train_classifier(faces, faceID)

# # to save the trained model
# # run this only once
# # will save the trained model in trainingData.yml file
# # face_recognizer.save("trainingData2.yml")


# # face_recognizer=cv2.face.LBPHFaceRecognizer_create()
# # face_recognizer.read(r"C:\Users\MSHOME\Desktop\Newfolder\FaceRecognition\trainingData1.yml")


# name = {0:"Ranbir", 1:"Aditya", 2:"Akshay"}

# vid = cv2.VideoCapture(r"C:\Users\MSHOME\Desktop\Newfolder\FaceRecognition\video\Video.mp4")
# # vid = cv2.VideoCapture(5)

# while True:
#     ret, test_img = vid.read()
#     faces_detected, gray_img = m.faceDetection(test_img)

#     for(x,y,w,h) in faces_detected:
#         cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,102,0), thickness=2, lineType=2, shift=0)

#     resized_img = cv2.resize(test_img, (540,720))
#     cv2.imshow("face detection tutorial", resized_img)
#     cv2.waitKey(1)

#     for faces in faces_detected:
#         (x,y,w,h) = faces
#         # extracting region of interest
#         roi_gray = gray_img[y:y+h, x:x+h]
#         # predicting the label of given image
#         # confidence is the accuracy of the prediction
#         # confidence is a number between 0 and 100
#         # the lower the value, the more accurate the prediction
#         # label 0 or 1
#         # confidence value lower than its more accurate
#         # 35 is the threshold value for confidence
#         label, confidence = face_recognizer.predict(roi_gray)

#         print("confidence:", confidence)
#         print("label:", label)
#         m.draw_rect(test_img, faces)

#         # extract the name from the dictionary
#         predicted_name = name[label]
#         if(confidence>37):
#             continue


#         m.put_text(test_img, predicted_name, x, y)


#     resized_img = cv2.resize(test_img, (540,720))
#     cv2.imshow("face detection tutorial", resized_img)
#     if cv2.waitKey(10) == ord('q'):
#         break

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# square window for our game.
# can change screen size from here
screen_width = screen_height = 550
Move_log_panel_width = 250
Move_log_panel_height = screen_height
screen_caption = "ChessAI"
icon = p.image.load(
    r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\images\icon.png"
)

# rows and columns

dimensions = 8

# making sqaures in the screen to display chess board boxes
sq_size = screen_height // dimensions



fps = 30
# to pass as an argument in clock.tick
# adjust if game become laggy

images = {}

def load_images():
   
    # load all images once as it is cpu heavy task
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        image_path = (
            r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\images"
            + "\\"
            + piece
            + ".png"
        )
    
        images[piece] = p.transform.scale(
            p.image.load(image_path).convert_alpha(), (sq_size, sq_size)
        )

        # pygame.transform.scale to adjust the image


def main():
    p.init()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # initializing the pygame modules
    animate = False

    # text = (
    #     "We have detected that user"
    #     + tt.predicted_name
    #     + " is playing. Press any key to start the game"
    # )
    # language = "en"
    # myobj = gtts.gTTS(text=text, lang=language, slow=False)
    # myobj.save("welcome1.mp3")
    # Playing the converted file
    # time.sleep(4)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # os.system("welcome.mp3")

    # setting screen with sizes

    # closing our face detection window
    # cv2.destroyAllWindows()

    screen = p.display.set_mode(
        (screen_width + Move_log_panel_width, screen_height), p.HWSURFACE | p.DOUBLEBUF
    )

    # welcome = "Welcome," + tt.predicted_name + "to ChessAI"
    # language = "en"
    # myobj1 = gtts.gTTS(text=welcome, lang=language, slow=False)
    # myobj1.save("welcome.mp3")
    # # Playing the converted file
    # p.mixer.music.load("welcome.mp3")

    # invalid = "Invalid move"
    # language = "en"
    # myobj2 = gtts.gTTS(text=invalid, lang=language, slow=False)
    # myobj2.save("invalid.mp3")

    moveLogFont  = p.font.SysFont("Roboto", 14, False, False)
   
    global highlight 
    highlight = p.transform.scale(
        p.image.load(
            r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\images\Highlight.jpg"
        ).convert_alpha(),
        (sq_size, sq_size)
    )

    p.display.set_caption(screen_caption)
    p.display.set_icon(icon)
    p.display.update()
    # clock object
    clock = p.time.Clock()
    # fps change karega to limit CPU in clock.tick(15)

    screen.fill(p.Color("white"))
    # aise hi

    # creating a gamestate object joh ki constructor ko call karega apne
    # dot operator to call gamestate() in engine

    gs = engine.gamestate()

    # to store valid moves
    valid_moves = gs.getvalidmoves()

    # print(gs.board)
    move_made = False
    # to update valid moves only when a move is made

    # flag variable for when a move is made
    # loading the images "once"
    load_images()

    # running variable to check start and quit
    running = True
    # tuple to keep the last square selected
    sq_selected = ()
    # no square is selected at start
    # tuple: (row,col)
    # playerClicks = []

    # list to keep two inputs
    player_clicks = []
    # keep track of player clicks (two tuples: [(6, 4), (4, 4)])

    done = True
    try:
        p.mixer.init()
        p.mixer.music.load("welcome1.mp3")
        p.mixer.music.play()
        # time.sleep(5)
    except:
        pass
    chess = p.transform.scale_by(
        p.image.load(
            r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\Images\chess.jpg"
        ),
        0.25,
    )
    screen.fill(p.Color("black"))
    while done:
        screen.blit(
            chess, p.Rect(200 - 5 * sq_size + 180, 200 - 5 * sq_size + 200, 10, 10)
        )
        screen.blit(
            p.transform.scale_by(icon, 0.5),
            p.Rect(470 - 5 * sq_size + 15, screen_height / 2 - 270, 10, 10),
        )
        showtext(
            screen,
            "Welcome to ChessAI",
            (screen_height / 2 - 230, screen_height / 2 - 10),
            40,
        )
        showtext(
            screen,
            "Press any key to start the game",
            (screen_height / 2 - 220, screen_height / 2 + 50),
            25,
        )

        # try:
        #     showtext(
        #         screen,
        #         tt.predicted_name + " is playing",
        #         (screen_height / 2 - 111, screen_height / 2 - 240),
        #         25,
        #     )
        # except:
        #     showtext(
        #         screen,
        #         "User is playing",
        #         (screen_height / 2 - 300, screen_height / 2 - 200),
        #         25,
        #     )
        p.display.flip()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
            if event.type == p.KEYDOWN:
                try:
                    p.mixer.music.load("welcome.mp3")
                    p.mixer.music.play()
                except:
                    pass
                done = False
                # showtext(screen, predicted_name + " is playing")
    playerone = True
    playertwo = False
    # if a human is playing white then playerone = True
    # if a AI is playing white then playerone = False
    # if a human is playing black then playertwo = True
    # if a AI is playing black then playertwo = False

    # start of my gameloop



    gameOver = False

    while running:
        

        # check if human is playing white and its his turn
        # or if human is playing black and its his turn
        HumanTurn = (gs.whitemove and playerone) or (not gs.whitemove and playertwo)

        # lets keep a for loop to get events
        for event in p.event.get():
            # print(p.display.Info())
            # if the type of event is this

            if event.type == p.QUIT:
                # to exit the whileloop
                running = False
            elif event.type == p.MOUSEBUTTONDOWN:
            #   if not gameOver and HumanTurn:
                    # to check if the game is over or not
                    # to check if its the human's turn or not

                # mouse kaha h?
                mouse_location = p.mouse.get_pos()  # (x,y) location of mouse
                # get x and y from list
                column = mouse_location[0] // sq_size
                row = mouse_location[1] // sq_size

                # first click is select, second click is undo
                if sq_selected == (row, column) or column >= 8 or row >= 8:
                    # user clicks move log panel or outside the board
                    # user clicks same sqaure again
                    sq_selected = ()  # undo
                    player_clicks = []
                else:
                    # store the square selected by the user now
                    sq_selected = (row, column)
                    player_clicks.append(sq_selected)
                    # first time it will append to empty list then it appends to list[0]

                    # hume pata karna hai user ka first click hai ya second
                    if len(player_clicks) == 2:
                        # do clicks hogye toh bolenge make move
                        # so call the move class constructor
                        move = engine.Move(player_clicks[0], player_clicks[1], gs.board)
                        # print(move.getChessNotation())

                        # player_clicks[0] is our source
                        # player_clicks[1] is our piece's destination
                        for i in range(len(valid_moves)):
                            # only get valid move object
                            # so check for it

                            if move == valid_moves[i]:
                                gs.makeMove(valid_moves[i])
                                print("pawns=",AI.NumberofPawns(gs))
                                AI.KingCastled(gs)
                                # print("King castled",AI.KingCastled(gs))
                                move_made = True
                                animate = True
                                user_choice = "Q"
                                while move.pawn_promotion:
                                    p.display.set_caption(
                                        "Choose a piece to promote to"
                                    )
                                    screen.fill(p.Color("black"))
                                    screen.blit(
                                        p.transform.scale_by(
                                            p.image.load(
                                                r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\Images\PromotionMenu.jpg"
                                            ),
                                            0.2,
                                        ),
                                        p.Rect(200 - sq_size, 200 - sq_size, 10, 10),
                                    )
                                    showtext(
                                        screen,
                                        "Enter the corresponding character of the piece you want to promote to :",
                                        (200, 200),
                                        12,
                                    )
                                    p.display.flip()
                                    user_choice = ""
                                    for event in p.event.get():
                                        if event.type == p.KEYDOWN:
                                            if event.key == p.K_q:
                                                gs.makePawnPromotion(move, "Q")
                                                move.pawn_promotion = False

                                            elif event.key == p.K_r:
                                                gs.makePawnPromotion(move, "R")
                                                move.pawn_promotion = False

                                            elif event.key == p.K_b:
                                                gs.makePawnPromotion(move, "B")
                                                move.pawn_promotion = False
                                            elif event.key == p.K_n:
                                                gs.makePawnPromotion(move, "N")
                                                move.pawn_promotion = False
                                            else:
                                                gs.makePawnPromotion(move, "Q")
                                                move.pawn_promotion = False
                                            p.display.set_caption("ChessAI")

                                # argument to makemove is generated by the engine

                                move_made = True

                                sq_selected = ()  # reset user clicks
                                player_clicks = []

                                # reset the user clicks after making the move each time
                        if not move_made:
                            player_clicks = [sq_selected]

                        # gs.makeMove(move)
                        # to make the move

            elif event.type == p.KEYDOWN:

                if event.key == p.K_z:
                    gs.undoMove()
                    move_made = True
                    animate = False
                    gameOver = False
                    # when the user undoes a move the valid moves change
                    # so change the flag variable to true

                    # to update the valid moves


                


                if event.key == p.K_r:
                    gs = engine.gamestate()
                    valid_moves = gs.getvalidmoves()
                    sq_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False
                    gameOver = False

        if not gameOver and not HumanTurn:
            # generate and store the AI move
            print("Queen",AI.QueenMobililty(engine))
            print("King",AI.KingMobililty(engine))
            print("King castled",AI.KingCastled(gs))
            print("King Neighbour Pawns",AI.KingPawnShield(gs))
            print("AI's turn")
            AIMove = AI.findBestMove(gs, valid_moves)
            if AIMove is None:
                # if the AI has no valid moves
                # certain engines make random moves then
                # checkmate and stalemate will be handled by the engine
                AIMove = AI.findRandomMove(valid_moves)
            # give it to our engine
            gs.makeMove(AIMove)
            move_made = True
            animate = True
        if move_made:
            if animate:
                animateMove(gs.moveLog[-1], screen, gs.board, clock, gs,moveLogFont)
            valid_moves = gs.getvalidmoves()
            move_made = False
            animate = False

        # calling the draw boardand pieces fn
        draw_game_state(screen, gs, valid_moves, sq_selected, moveLogFont)
        if gs.checkmate:
            gameOver = True
            if gs.whitemove:
                showtext(screen, "Black wins by checkmate", (screen_width / 2 - 100, screen_height / 2 - 10), 25)
            else:
                showtext(screen, "White wins by checkmate", (screen_width / 2 - 100, screen_height / 2 - 10), 25)
        elif gs.stalemate:
            gameOver = True
            showtext(screen, "Stalemate", (screen_width / 2 - 100, screen_height / 2 - 10), 25)
        clock.tick(fps)
        p.display.flip()
        AI.KingNeighbourPawns=0
        # to update the display


def HighlightSquares(screen, gs, valid_moves, sq_selected, moveLog):
    # to highlight the square selected by the user
    # to highlight the last move made by the user

    # highlight karne ke liye square h na?
    # toh select kiya ki nahi check karna padega
    if sq_selected != ():
        # get row column from tuple
        row, column = sq_selected

        # so if it is white's turn and the piece selected by the user is white
        # then first element of the piece is w
        # else the first element of the piece is b  
        if gs.board[row][column][0] == ("w" if gs.whitemove else "b"):
            # if the piece selected by the user is of the same color as the player's turn
            # then highlight the square

            # surface takes a (x,y) tuple
            s = p.Surface((sq_size, sq_size))

            s.set_alpha(100)  # transparency value --> 0 is transparent, 255 is opaque
            s.fill(p.Color("blue"))
            screen.blit(s, (column * sq_size, row * sq_size))
            # highlight the moves from that square
            s.fill(p.Color("yellow"))

            # highlight all the valid moves from that square
            for moves in valid_moves:
                # move start square se start hota hai
                if moves.startRow == row and moves.startCol == column:
                    # toh end square ko highlight karenge
                    highlight.set_alpha(220)
                    screen.blit(highlight, (moves.endCol * sq_size, moves.endRow * sq_size))

    # highlight the last move made by the user
    if len(gs.moveLog) > 0:
        # so if the moveLog is not empty
        # then highlight the last move made by the user
        # get the last move from the moveLog
        move = gs.moveLog[-1]
        # now we have the move
        # now we have to highlight the move
        # so we will highlight the start square and the end square
        # so we will highlight the start square and the end square
        # surface takes a (x,y) tuple
        s = p.Surface((sq_size, sq_size))

        s.set_alpha(150)  # transparency value --> 0 is transparent, 255 is opaque
        s.fill(p.Color(255, 255, 0))
        screen.blit(s, (move.startCol * sq_size, move.startRow * sq_size))
        # highlight the moves from that square
        s.fill(p.Color(0, 255, 0))
        screen.blit(s, (move.endCol * sq_size, move.endRow * sq_size))


# method to draw sqs on board and graphics of a current gamestate
def draw_game_state(screen, gs, valid_moves, sq_selected, moveLogFont):

    # to draw squares on the board
    drawboard(screen)

    # board-->pieces order ofc matter karega nhi toh pieces piche chip jayenge

    # to highlight the squares
    HighlightSquares(screen, gs, valid_moves, sq_selected, moveLog=gs.moveLog)

    # uske pehle ya baad bhi kar sakte hai
    # to draw pieces
    drawpieces(
        screen, gs.board
    )  # board from engine gamestate ka object gs , isliye dot

    drawMoveLog(screen, gs, moveLogFont)

def animateMove(move, screen, board, clock,gs,moveLogFont):
    global colors
    colors = [p.Color("white"), p.Color("dark gray")]
    # colors = [p.Color("white"), p.Color("dark gray")]
    # colors = [p.Color("white"), p.Color("dark gray")]
    coords = []  # to store the coordinates of the move

    # change in row and column
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol


    # frames per square
    framesPerSquare = 10
    animationTime = 2  # in seconds
    # animation speed control karega


    # toh hume 10 frames me move karna hai
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    speed = 1 / frameCount  # speed of animation
    for frame in range(frameCount + 1):
        # toh hume 10 frames me move karna hai
        # so 10 baar loop chalayenge
        # so hume 10 baar move karna hai
        r, c = (move.startRow + dR * frame / frameCount, move.startCol + dC * frame / frameCount)
        drawboard(screen)
        drawpieces(screen, board)
        drawMoveLog(screen, gs,moveLogFont)
        # erase the piece moved from its ending square
        # print(images)
        # image = images[(move.endRow + move.endCol) % 2]

        endSquare = p.Rect(move.endCol * sq_size, move.endRow * sq_size, sq_size, sq_size)
        p.draw.rect(screen, (255,255,0,20), endSquare)
        # screen.blit(image, endSquare)
        # draw captured piece onto rectangle
        if move.pieceCaptured != "--":
            if move.isEnpassantMove:
                enpassantRow = move.endRow + 1 if move.pieceCaptured[0] == "b" else move.endRow - 1
                endSquare = p.Rect(move.endCol * sq_size, enpassantRow * sq_size, sq_size, sq_size)
            screen.blit(
                images[move.pieceCaptured],
                p.Rect(move.endCol * sq_size, move.endRow * sq_size, sq_size, sq_size),
            )
        # draw moving piece
        screen.blit(
            images[move.pieceMoved],
            p.Rect(c * sq_size, r * sq_size, sq_size, sq_size),
        )
        p.display.flip()
        clock.tick(60)


def drawboard(screen):
    # lets draw squares
    # white and grey alternate
    # make list to store white and grey switch karna easy hoga
    # colors = [p.Color("white"), p.Color("dark gray")]
    images = [
        p.image.load(
            r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\images\ltb.jpg"
        ).convert_alpha(),
        p.image.load(
            r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\images\dtb.jpg"
        ).convert_alpha(),
    ]

    for rows in range(dimensions):
        for columns in range(dimensions):
            # [00,10,20,30,40,50,60,70]
            # [01,11,21,31,41,51,61,71]
            # [02,12,22,32,42,52,62,72]
            # [03,13,23,33,43,53,63,73]
            # [04,14,24,34,44,54,64,74]
            # [05,15,25,35,45,55,65,75]
            # [06,16,26,36,46,56,66,76]
            # [07,17,27,37,47,57,67,77]

            # trend we see here is that if we add rows and columns
            # dark sqaures are odd
            # light sqaures are even

            # color = colors[(rows+columns)%2]
            image = images[(rows + columns) % 2]
            # even --> colors[0] --> white
            # odd --> colors[1] --> black

            # smpart

            # just draw rectangle (surface,color,)
            custom_img = p.Surface((sq_size, sq_size))
            screen.blit(
                image, p.Rect(columns * sq_size, rows * sq_size, sq_size, sq_size)
            )

            # p.draw.rect(screen, color, p.Rect(columns*sq_size,rows*sq_size, sq_size, sq_size))


def drawpieces(screen, board):
    for rows in range(dimensions):
        for columns in range(dimensions):
            pieces = board[rows][columns]
            if pieces != "--":
                screen.blit(
                    images[pieces],
                    p.Rect(columns * sq_size, rows * sq_size, sq_size, sq_size),
                )
            # accessing our gs.board multi dim list by using [][]
            # to assign each square a piece

def drawMoveLog(screen, gs, font):
    moveLogRect = p.Rect(550, 0, 250, 550)
    p.draw.rect(screen, p.Color("black"), moveLogRect)
    moveLog = gs.moveLog
    moveTexts = gs.moveLog
    padding = 5
    textY = padding

    for i in range(len(moveTexts)):
        text = moveTexts[i].getChessNotation()
        textObject = font.render(text, True, p.Color("white"))
        textLocation = moveLogRect.move(padding, textY)
        screen.blit(textObject, textLocation)
        textY += textObject.get_height() + padding * 2
# function to show a menu an ask the user the piece to promote to in pawn promotion


def showtext(screen, text, location, fontsize):
    font = p.font.SysFont("Copperplate gothic", fontsize, True, False)
    textObject = font.render(text, False, p.Color("White"))
    location1 = p.Rect(location, location)
    screen.blit(textObject, location1)


# if we import something in the main code we need to do this cause it wont run otherwise
# THIS CODE WE HAVE TO RUN AS THIS IS OUR MAIN CODE AND WE IMPORT OTHER MODULES IN THIS CODE
# SO WE WRITE THIS
# The if __name__ == "__main__": construct is used to
# ensure that a specific block of code only runs when the Python script is executed directly,
# not when it's imported as a module in another script.
if __name__ == "__main__":
    main()
