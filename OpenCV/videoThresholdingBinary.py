# VideoThresholdingBinary

import cv2 as cv
import numpy as np



def nothing(x):
    pass


cap = cv.VideoCapture(0)
ret, frame = cap.read()
frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
th_img = np.zeros(frame.shape, dtype=np.uint8)

cv.namedWindow('th')
cv.createTrackbar('Threshold', 'th', 0, 255, nothing)
cv.createTrackbar('Switch', 'th', 0, 1, nothing)

while(True):
    ret, frame = cap.read()
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    switch = cv.getTrackbarPos('Switch', 'th')
    if (switch == 1):
        th = cv.getTrackbarPos('Threshold', 'th')
        ret, th_img = cv.threshold(img_gray, th, 255, cv.THRESH_BINARY_INV)

    cv.imshow('Frame', img_gray)
    cv.imshow('th', th_img)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
