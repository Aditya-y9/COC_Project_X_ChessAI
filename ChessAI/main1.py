import cv2
# os to create labels for our training data
# to handle file related operatons
import os
# numpy to convert python list to numpy array as 
# open cv face recognizer accepts numpy array
import numpy as np

def faceDetection(test_img):
    # convert color image to grayscale
    # as opencv face detector accept gray images

    # using opencv cvtColor function
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    # load haar classifier
    # haar classifier is a machine learning based approach
    # where a cascade function is trained from a lot of positive and negative images
    # to detect faces
    face_haar_cascade = cv2.CascadeClassifier(r"C:\Users\parab\OneDrive\Desktop\GITDEMO\COC_Project_X_ChessAI\ChessAI\haarcascade_frontalface_default.xml")
    # detect multiscale images
    # classifier is loaded and image is passed to detectMultiScale function

    # returns the rectangle values of detected faces
    # rectangle values are stored in faces
    # scale factor specifies how much the image size is reduced with each scale
    # minNeighbors specifies how many neighbors each candidate rectangle should have
    # to retain it
    # images bigger in size are likely to be not detected
    # so we reduce the size by 1.32 times
    # minNeighbors = 5 means that a rectangle should have 5 neighbors to be called a face

    # returns a list of rectangles
    # rectangles are stored in faces

    # to prevent false positives

    faces = face_haar_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)
    return faces, gray_img

def labels_for_training_data(directory):
    faces = []
    faceID = []

    # loop through each directory and read images within it
    for path,subdirnames,filenames in os.walk(directory):
        # accessing folders
        for filename in filenames:
            # accessing individual images
            if filename.startswith("."):
                print("Skipping system file")
                continue
            # loading images
            # using opencv imread function
            # imread returns a numpy array
            # numpy array is stored in img
            id = os.path.basename(path)
            img_path = os.path.join(path, filename)
            print("img_path:", img_path)
            print("id:", id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("Image not loaded properly")
                continue
            # calling faceDetection function
            # returns faces detected in particular image
            # gray image is returned
            faces_rect, gray_img = faceDetection(test_img)
            # if there is no face detected
            # it will return the same image
            # so we will ignore it

            # we need single face in image
            # to train our model
            # classifier will not be able to detect multiple faces
            # it will get confused
            # so we will ignore images with multiple faces
            if len(faces_rect) != 1:
                continue

            (x,y,w,h) = faces_rect[0]   


            # classifier takes only the region of interest
            # cropping the face part to pass it to classifier
            # classifier takes only gray image

            roi_gray = gray_img[y:y+w, x:x+h]


            # convert ot numpy array
            # classifier takes numpy array
            # converting list to numpy array
            # append the face to faces list
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces, faceID

def train_classifier(faces,faceID):
    # create object of face recognizer
    # using opencv
    # LBPH is face recognizer
    # it is fast and accurate
    # it labels the pixels of image
    # it uses local features to predict face
    # local binary patterns histogram
    # binary
    # pixels are converted to binary
    # based on central pixel



    # if neighbor pixel is greater than central pixel
    # create object of face recognizer
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    # train the face recognizer
    # using numpy array of faces and faceID
    face_recognizer.train(faces, np.array(faceID))
    return face_recognizer

def draw_rect(test_img, face):
    (x,y,w,h) = face
    # draw a rectangle around the face
    # using opencv rectangle function
    # rectangle takes 5 arguments
    # 1. image
    # 2. top left coordinates
    # 3. bottom right coordinates
    # 4. color
    # 5. thickness
    cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,102,0), thickness=2, lineType=2, shift=0)

def put_text(test_img, text, x, y):
    # put text on the image
    # using opencv putText function
    # putText takes 5 arguments
    # 1. image
    # 2. text
    # 3. coordinates
    # 4. font
    # 5. font size
    cv2.putText(test_img, text, (x,y), cv2.FONT_ITALIC, 1, (255,102,0), 2)


