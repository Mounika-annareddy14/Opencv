"""BASIC IMAGE TRANSFORMATIONS
RESIZING , CLIPPING , CROPPING TRANSLATION,ROTATION"""
import cv2 as cv
import numpy as np

#translation
"""Translation is basically shifting an image along x and y axis
--> -x = left
--> -y = up
-->  x = right
-->  y = down"""
img = cv.imread('Photos\park.jpg')
cv.imshow("Lady" , img)

# translating the image
def translate(img , x , y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1] , img.shape[0] )
    return cv.warpAffine(img , transMat , dimensions)

translated = translate(img , -100,100)
cv.imshow('Translated' , translated)

# rotation
"""Define by itself rotating a image with some angle"""
def  rotate(img , angle , rotPoint = None):
    (height , width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2 , height//2) # here if rotate point is none then it would be in center

    rotMat = cv.getRotationMatrix2D(rotPoint,angle , 1.0)
    dimensions = (width , height)

    return cv.warpAffine(img , rotMat , dimensions)

rotatated = rotate(img , 100)
cv.imshow('rotated' , rotatated)

# rotating rotataed image
rotatated_img = rotate(rotatated , -45)
cv.imshow("Rotated_2" , rotatated_img)

# resizing
resized = cv.resize(img , (20,20) , interpolation = cv.INTER_CUBIC)
cv.imshow("Resized" , resized)

#flipping
"""0 - vertically
1 - horizontally
-1 - both vertically and horizontally
"""
flip = cv.flip(img , -1)
cv.imshow("Flip" , flip)

# cropped
cropped = img[200:300 , 400:500]
cv.imshow("Cropped" , cropped)




cv.waitKey(0)
cv.destroyAllWindows()

