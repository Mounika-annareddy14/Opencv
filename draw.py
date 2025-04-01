import cv2 as cv
import numpy as np

blank = np.zeros((500,500 , 3) , dtype='uint8')
cv.imshow('image' , blank)

#painting the image
# blank[200:300 , 300:400] = 0,255,255
# cv.imshow('image' , blank)

# drawing the rectangle
#cv.rectangle(blank , (0,0) , (250,500) , (0,255,0) , thickness=1)
# cv.rectangle(blank , (0,0) , (blank.shape[1]//2 , blank.shape[0] // 2) ,  (0,255,0) , thickness=-1)
# cv.imshow('rectangle' , blank)

# # drawing a circle
# cv.circle(blank , (blank.shape[1]//2 , blank.shape[0]//2) , 40 , (0,255,255) , thickness=3)
# cv.imshow('Circle' , blank)

# # drawing a line
# cv.line(blank , (0,0) , (blank.shape[1]//2 , blank.shape[0] // 2) ,  (255,255,255) , thickness=3)
# cv.imshow('Line' , blank)

# putting a text
cv.putText(blank , 'Hey Ed Mubbarak To All!' ,  (0 , 200) , cv.FONT_HERSHEY_TRIPLEX , 1.0 , (255,255, 255) , 2)
cv.imshow('Text' , blank)

cv.waitKey(0)
cv.destroyAllWindows() # used to remove a image in window by using any keyboard letter