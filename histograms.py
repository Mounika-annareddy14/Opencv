"""Histograms: allows us to visualize the distribution of pixel intensities in an image"""
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos\cat.jpg')
cv.imshow('img' , img)

blank = np.zeros(img.shape[:2] , dtype = 'uint8')

circle = cv.circle(blank , (img.shape[1]//2 , img.shape[0]//2) , 100 , 2)

# to grayscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)
mask = cv.bitwise_and(gray , gray , mask = circle)
# histogram plot
gray_hist = cv.calcHist([gray] , [0] , mask , [256] , [0-256])

plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('bins')
plt.ylabel('# no of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()