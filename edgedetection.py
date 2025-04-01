import numpy as np
import cv2 as cv

img = cv.imread('Photos\park.jpg')
cv.imshow('park' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

# laplacian
lap = cv.Laplacian(gray , cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian' , lap)

# sobel
sobelx = cv.Sobel(gray , cv.CV_64F , 1 , 0)
sobely = cv.Sobel(gray , cv.CV_64F , 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel' , combined_sobel)

# canny
canny = cv.Canny(gray , 150 , 170 )
cv.imshow('Canny' , canny)

cv.waitKey(0)
cv.destroyAllWindows()
