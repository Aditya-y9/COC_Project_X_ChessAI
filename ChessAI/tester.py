import cv2
import time
import os
import numpy as np
import main1 as m

# this function will read all persons' training images, detect face from each image
# used to load an image from a file
test_img = cv2.imread(r"C:\Users\MSHOME\Desktop\Newfolder\FaceRecognition\Images\Akshay.jpg")
# vid = cv2.VideoCapture(r"C:\Users\MSHOME\Desktop\Newfolder\FaceRecognition\video\Video.mp4")
# running = True
# while running:
#     success, frame = vid.read()
#     resized_img = cv2.resize(frame, (1000,700))
#     faces_detected, gray_img = m.faceDetection(resized_img)
#     for(x,y,w,h) in faces_detected:
#         cv2.rectangle(resized_img, (x,y), (x+w, y+h), (255,102,0), thickness=2, lineType=8, shift=0)
#     cv2.imshow("face detection tutorial", resized_img)
#     cv2.waitKey(1)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# vid.release()
# cv2.destroyAllWindows()

# detect faces from test image

# collect the rectangles returned by faceDetection function
# # collect the gray image returned by faceDetection function
faces_detected, gray_img = m.faceDetection(test_img)

# print("faces_detected:", faces_detected)

# for(x,y,w,h) in faces_detected:
#     cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,102,0), thickness=2, lineType=2, shift=0

# resized_img = cv2.resize(test_img, (1000,700))
# cv2.imshow("face detection tutorial", resized_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# faces, faceID = m.labels_for_training_data(r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\TrainingImages")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read(r"C:\Users\MSHOME\Desktop\Newfolder\FaceRecognition\trainingData2.yml")
# face_recognizer = m.train_classifier(faces, faceID)

# to save the trained model
# run this only once
# will save the trained model in trainingData.yml file
# face_recognizer.save("trainingData3.yml")


# face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\trainingData3.yml")



name = {0:"Ranbir", 1:"Aditya", 2:"Akshay"}

vid = cv2.VideoCapture(r"C:\Users\MSHOME\Desktop\Newfolder\COC_Project_X_ChessAI\ChessAI\video\Video.mp4")


# vid = cv2.VideoCapture(0)


start_time = time.time()
while True:
    try:
        ret, test_img = vid.read()
        faces_detected, gray_img = m.faceDetection(test_img)

        for(x,y,w,h) in faces_detected:
            cv2.rectangle(test_img, (x,y), (x+w, y+h), (255,102,0), thickness=2, lineType=2, shift=0)

        resized_img = cv2.resize(test_img, (1080,720))
        cv2.imshow("Welcome to ChessAI", resized_img)

        cv2.waitKey(1)

        for faces in faces_detected:
            (x,y,w,h) = faces
            # extracting region of interest
            roi_gray = gray_img[y:y+h, x:x+h]
            # predicting the label of given image
            # confidence is the accuracy of the prediction
            # confidence is a number between 0 and 100
            # the lower the value, the more accurate the prediction
            # label 0 or 1
            # confidence value lower than its more accurate
            # 35 is the threshold value for confidence
            label, confidence = face_recognizer.predict(roi_gray)
            print("label:", label)
            m.draw_rect(test_img, faces)

            # extract the name from the dictionary
            predicted_name = name[label]
            # if(confidence>37):
            #     continue


            m.put_text(test_img, predicted_name, x, y)

        resized_img = cv2.resize(test_img, (1080,720))
        cv2.imshow("Welcome to ChessAI", resized_img)

        if cv2.waitKey(10) == ord('q'):
            break
            break
        if time.time() - start_time >= 1:
            break
            # break
            # break
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

    except:
        print("Video is over")
        break
# cv2.waitKey(0)
# cv2.destroyAllWindows()



