"""Contours:Contours are basically boundaries of object
,the line or that curve joins the continuous points along the boundary of an object.
Contours are useful tools when we are get into shape analysis and object detection and recognition"""
import cv2 as cv
import numpy as np

img = cv.imread('Photos\lady.jpg')
cv.imshow('Lady' , img)

blank = np.zeros(img.shape , dtype='uint8')
cv.imshow('blank' , blank)

# converting into gray
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

# blur
blur = cv.GaussianBlur(gray , (3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur' , blur)

# edge
canny = cv.Canny(blur , 120,170)
cv.imshow('Canny' , canny)

# tresholding--> convertng in binary size
# ret , thresh = cv.threshold(gray , 125 , 255 , type=cv.THRESH_BINARY)
# cv.imshow('Thresh' , thresh)

#contours
contours , hierarchies = cv.findContours(canny,cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours are found!')

cv.drawContours(blank , contours , -1 , (255,255,255) , 1)
cv.imshow('blank' , blank)

cv.waitKey(0)
cv.destroyAllWindows()
