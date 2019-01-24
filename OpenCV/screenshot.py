#screenshot

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	cv.imshow('frame',frame)
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		cv.imwrite('img/screenshot.png',frame)
		break
