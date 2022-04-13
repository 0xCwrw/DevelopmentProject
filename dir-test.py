import os
import cv2
from time import sleep

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
newUser = "cameron"

def save_frame(frame):
    if len(faces) >= 1:
        cv2.imwrite('dataset/test{}.png'.format(i), frame)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # for (x, y, w, h) in faces:
    #     # print(x,y,w,h)
    #     roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
    #     roi_color = frame[y:y+h, x:x+w]
    #     color = (255, 0, 0) #BGR 0-255 
    #     stroke = 2
    #     end_cord_x = x + w
    #     end_cord_y = y + h

    #     cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    for i in range(1, 11):
        save_frame(frame)
    # print("found {0} faces!".format(len(faces)))

    # Display the resulting frame
    cv2.imshow(newUser,frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()