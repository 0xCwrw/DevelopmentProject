import os
import cv2
from time import sleep

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
newUser = "cameron"

def save_frame(frame, i):
    cv2.imwrite('dataset/test{}.png'.format(i), frame)

def image_collection():
    for i in range(1, 11):
        sleep(2)
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            frame = cv2.flip(frame, 0)
            gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            x = 0
            if len(faces) == 1:
                save_frame(frame, i)
                print("Face detected, sample {}/10 successful.".format(i))
                break
            elif len(faces) < 1:
                print("No faces detected, please adjust.")
            else:
                print("Too many faces detected, there should only be one person in frame.")
            # Display the resulting frame
        if cv2.waitKey(20) & 0xFF == ord('q'):
            x = 1
            print("Sample collection unsuccessful.")
            break
    if x == 0:
        print("sample collection successful...\nUser {} added to dataset.".format(newUser))
    else:
        print("\n")
# When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()