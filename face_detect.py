import cv2 as cv

img = cv.imread('Photos\group 1.jpg')
cv.imshow('Img' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

haar_cascade = cv.CascadeClassifier('harrcade.xml')

faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors=3)
print(f"Number of faces found {len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img , (x,y) , (x+w , y+h) , 0 , 2)

cv.imshow('Deteced faces' , img)

cv.waitKey(0)
cv.destroyAllWindows()