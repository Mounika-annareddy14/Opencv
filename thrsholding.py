"""THRESHOLDING:HELPs us to convert them into binary images
simple thrsholding and
Adpative thresholding"""
import cv2 as cv

img = cv.imread('Photos\cat.jpg')
cv.imshow('img' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

threshold , thresh = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY)
cv.imshow('Simple Threshlod' , thresh)

threshold , thresh_inv = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('SImple threshlod inverse' , thresh_inv)


# adaptive thresholding
adaptive = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 11 , 3)
cv.imshow('ADaptive Threshold' , adaptive)

cv.waitKey(0)
cv.destroyAllWindows()