import cv2 as cv
import numpy as np

img = cv.imread('test.jpeg')
cv.imshow('Adam Price', img)

# Converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(0)