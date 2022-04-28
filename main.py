import numpy as np
import cv2
import pickle
import time

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
recogniser = cv2.face.LBPHFaceRecognizer_create()
recogniser.read("recognisers/face-trainner.yml")

labels = {"person_name": 1}
with open("identities/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
time.sleep(0.1)

USER = "user zero two"
detected = 1
while detected <= 10:
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 0)
        gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            # print(x,y,w,h)
            roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
            roi_color = frame[y:y+h, x:x+w]
            #After prediction of ROI (Region of interest) computation is focused in that area.
            id_, conf = recogniser.predict(roi_gray)
            if conf>=40 and conf <= 80:
                name = labels[id_]
                name = name.replace("-", " ")
                USER = USER.lower()
                if name == USER:
                    print(F'{USER} detected.')
                    detected +=1
           
        cv2.imshow('Face detection',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
        break
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()