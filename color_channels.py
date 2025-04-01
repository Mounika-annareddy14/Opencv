import cv2 as cv
import numpy as np

img = cv.imread('Photos\park.jpg')
cv.imshow('Park' , img)

blank = np.zeros(img.shape[:2] , dtype = 'uint8')


#splitting
b,g,r = cv.split(img)

blue = cv.merge([b,blank , blank])
green = cv.merge([blank , g , blank])
red = cv.merge([blank , blank , r])

cv.imshow('Blue' , blue)
cv.imshow('Green' , green)
cv.imshow('Red' , red)


print(blue.shape)
print(green.shape)
print(red.shape)

print(b.shape)
print(g.shape)
print(r.shape)

# merged
merged_image = cv.merge([b,g,r])
cv.imshow('Mergeed' , merged_image)

cv.waitKey(0)
cv.destroyAllWindows()