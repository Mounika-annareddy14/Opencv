"""MASKING: certainily allows us to focus on certain parts that we would like to focus on"""
import numpy as np
import cv2 as cv

img = cv.imread('Photos\cats 2.jpg')
cv.imshow('Cats' , img)

blank = np.zeros(img.shape[:2] , dtype='uint8')
cv.imshow('Blank image' , blank)

circle = cv.circle(blank.copy() , (img.shape[1]//2, img.shape[0]//2) , 200 , 255 ,  -1)
rectangle = cv.rectangle(blank.copy() , (40,40) , (470 , 470) , 255 , -1)
weird_shape = cv.bitwise_and(circle , rectangle)

masked_image = cv.bitwise_and(img , img, mask=weird_shape)
cv.imshow('Masked Image' , masked_image)

cv.waitKey(0)
cv.destroyAllWindows()