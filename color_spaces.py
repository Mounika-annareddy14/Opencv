"""COLOR SPACES: basically SPace of colors , a system of representing an array of pixels.
RGB , gray scale , hsv , lamb and many more...
opencv open imag as bgr
matplotlib does not idea on bgr hence it inverse to rgb"""

import cv2 as cv


img = cv.imread('Photos\cat.jpg')
cv.imshow('color' , img)

#bgr to gray scale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

#bgr to hsv
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)  # based on huw human thinks and conceive of color
cv.imshow('HSV' , hsv)

# bgr to l*a*b
lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
cv.imshow('lab' , lab)

#bgr to rgb
rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)
cv.imshow('RGB' , rgb)

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv , cv.COLOR_HSV2BGR)
cv.imshow('bgr' , hsv_bgr)


cv.waitKey(0)
cv.destroyAllWindows()