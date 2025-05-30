import cv2 as cv

img = cv.VideoCapture(0)
while True:
    isTrue, frame =img.read()
    cv.imshow('frame',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.waitKey(0)



