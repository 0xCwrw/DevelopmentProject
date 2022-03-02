import cv2
import numpy as np

video=cv2.VideoCapture(0)
a=0
while True:
    a=a+1
    check, frame= video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_flip = cv2.flip(gray, 0)

    cv2.imshow("say cheese ..", gray_flip)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break
print(a)

video.release()
cv2.destroyAllWindows