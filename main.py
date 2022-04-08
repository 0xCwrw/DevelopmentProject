import cv2 as cv
import numpy as np
import cv2

img = cv.imread('test.jpeg')
cv.imshow('Adam Price', img)

# Converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
#Get user supplied values
imagePath = "test.jpeg"
cascPath = "cascades/haarcascade_frontalface_default.xml"


#Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

#Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30,30),
    flags= cv2.CASCADE_SCALE_IMAGE
)

print("Hey dude, found {0} faces in that image :)".format(len(faces)))

#draws a rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0) 