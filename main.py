import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

people = ['cam','alicia']
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

PiCam = cv.VideoCapture(0)

gray = cv.cvtColor(PiCam, cv.COLOR_BGR2GRAY)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(PiCam, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(PiCam, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', PiCam)

cv.waitKey(0)

# cascPath = "haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascPath)
# log.basicConfig(filename='webcam.log',level=log.INFO)

# video_capture = cv2.VideoCapture(0)
# anterior = 0

# while True:
#     if not video_capture.isOpened():
#         print('Unable to load camera.')
#         sleep(5)
#         pass

# #//////////////////////////////////// Gets input from webcam, frame-by-frame ////////////////////////////////////
#     ret, frame = video_capture.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# #//////////////////////////////////// Detects faces within the input ////////////////////////////////////
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.4,
#         minNeighbors=5,
#         minSize=(30, 30)
#     )

# #//////////////////////////////////// Draws a rectangle around the detected face ////////////////////////////////////
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     if anterior != len(faces):
#         anterior = len(faces)
#         log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

#     frame = cv2.flip(frame, 0) 
# #//////////////////////////////////// Displays the resulting frame including rectangle ////////////////////////////////////
#     cv2.imshow('Video', frame)


#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# #//////////////////////////////////// Stops the capture after loop is complete ////////////////////////////////////
# video_capture.release()
# cv2.destroyAllWindows()