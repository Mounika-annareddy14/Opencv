import cv2 as cv
import numpy as np

img1 = cv.imread('Photos\\cat.jpg')
img2 = cv.imread('Photos\\lady.jpg')

img1 = cv.resize(img1 , (400,400))
img2 = cv.resize(img2  , (400,400))

#bitwise -and --> only intersection  regions
bitwise_and = cv.bitwise_and(img1 , img2)
cv.imshow('AND' , bitwise_and)

# bitwise OR --> both intersecting and non - intersectiong regions
bitwise_or = cv.bitwise_or(img1 , img2)
cv.imshow('OR' , bitwise_or)

# bitwise XOR --> only non intersection regions
bitwise_xor = cv.bitwise_xor(img1 , img2)
cv.imshow('XOR' , bitwise_xor)

# not
bitwise_not = cv.bitwise_and(img1 , img2)
cv.imshow('NOT' , bitwise_not)


# blank = np.zeros((400,400) , dtype='uint8')

# rectangel = cv.rectangle(blank.copy() , (30,30) , (370 , 370) , 255 , -1)
# circle = cv.circle(blank.copy() , (200,200) , 200 , 255 , -1)

# # and
# bit_and = cv.bitwise_and(rectangel , circle)
# cv.imshow('AND' , bit_and)

# bit_or = cv.bitwise_or(rectangel , circle)
# cv.imshow('OR' , bit_or)

# bit_xor = cv.bitwise_xor(rectangel , circle)
# cv.imshow('XOR' , bit_xor)

# bit_not = cv.bitwise_not(rectangel , circle)
# cv.imshow('NOT' , bit_not)

cv.waitKey(0)
cv.destroyAllWindows()
