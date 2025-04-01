"""BLURRING:
blurring is used to reduce the noise and smoothing in the image
in the we have window the window size we called it as kernel size
the sourrounding pixels which are sourrounded by mid point"""
import cv2 as cv

img = cv.imread('Photos\cats.jpg')
cv.imshow('cats' , img)

# average blur
"""These techinque is the sum of sourrounding pixels and len of sourrounding pixels"""
average = cv.blur(img , (7,7))
cv.imshow('Average Blur' , average)

# Gaussian Blur 
"""this is similar to average blur but it adds some  weights to the pixels"""
gauss = cv.GaussianBlur(img , (7,7) , 1.0)
cv.imshow('Gaussain Blur' , gauss)

# median Blur
"""it takes mid value of the blurring it reduces noise more effectively than above both"""
median = cv.medianBlur(img , 7)
cv.imshow('Median Blur' , median)

# bilateral
"""Bilateral applies the bluring but it retains the edges"""
bilateral = cv.bilateralFilter(img , 3, 15 , 15)
cv.imshow('Bilateral blur' , bilateral)

cv.waitKey(0)
cv.destroyAllWindows()


