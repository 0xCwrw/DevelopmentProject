import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
time.sleep(0.1)

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()