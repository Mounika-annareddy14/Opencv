import cv2 as cv

img = cv.imread('Photos\cat.jpg')
cv.imshow('Image' , img)

def RescaleFrame(frame , scale = 0.75):
    width = int(frame.shape[1] * scale)  # width = 1 
    height = int(frame.shape[0] * scale)

    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

resized_image = RescaleFrame(img)
cv.imshow('resized' , resized_image)


capture = cv.VideoCapture('C:\\Users\\Mounika Reddy\\OneDrive\\Desktop\\OpenCV\\Videos\\dog .mp4')
while True:
    isTrue , frame = capture.read()
    resized_video = RescaleFrame(frame ,scale = .2 )

    if isTrue:
        cv.imshow('Video' , frame)
        cv.imshow('Resized' , resized_video)
       
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()


