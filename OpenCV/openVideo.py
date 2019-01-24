#openVideo

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('./vid/vtest.avi')

while(cap.isOpened()):
	ret, frame = cap.read()
	
	if ret == False:
		break
	
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	
	cv.imshow('frame', gray)
	if cv.waitKey(100) & 0xFF == ord('q'):
		break

cap.release()
cv.destroyAllWindows()