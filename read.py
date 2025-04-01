import cv2 as cv

# Reading images
# img = cv.imread('C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\OpenCV\\Photos\\cat_large.jpg')

# cv.imshow('cat' , img)



# Reading videos

# capture = cv.VideoCapture('C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\OpenCV\\Videos\\dog .mp4')  # giving path the video if it is 0 it is a webcam

# while True:
#     isTrue , frame = capture.read()  # reads the video frame by frame and Istrue wheather the video is there or not
#     cv.imshow('Video' , frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

#cv.waitKey(0)  # infinite time


capture = cv.VideoCapture('C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\OpenCV\\Videos\\dog .mp4')

while True:
    isTrue , frame = capture.read()

    if isTrue:
        cv.imshow('Video' , frame)

        if cv.waitKey(30) & 0xFF == ord('d'):
            break

    else:
        break

capture.release()
cv.destroyAllWindows()