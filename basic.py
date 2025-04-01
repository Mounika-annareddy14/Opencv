import cv2 as cv

img = cv.imread('Photos\cat.jpg')
cv.imshow('img' , img)

# converting into gray
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('img1' , gray)

# converting intto blur
blur = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT) # blurness depends on kernel size
cv.imshow('blur' , blur)

# edge cascade
edge = cv.Canny(img , 125 , 175)
cv.imshow('edge' , edge)

#dilating the image
dilated = cv.dilate(edge , (7,7) , iterations=3)
cv.imshow('dilated' , dilated)

# eroding
erode = cv.erode(dilated , (7,7) , iterations=3)
cv.imshow('Erode' , erode)

#resize 
resized = cv.resize(img , (500 , 500) , interpolation=cv.INTER_CUBIC)
cv.imshow('resized' , resized)

# cropping
crop = img[50:200 , 200:300]
cv.imshow('cropped' , crop)

cv.waitKey(0)
cv.destroyAllWindows()
