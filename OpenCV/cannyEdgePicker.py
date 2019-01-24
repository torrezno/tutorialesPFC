#CannyEdge Detection Parameter Picker

import numpy as np
import cv2 as cv

def nothing(x):
	pass
	
#Create black image
src = cv.imread('img/screenshot.png')
cv.namedWindow('image')

#create trackbars
cv.createTrackbar('Th1','image',0,1000,nothing)
cv.createTrackbar('Th2','image',0,1000,nothing)

#create switch
cv.createTrackbar('switch','image',0,1,nothing)

while(True):
	#get current positions of four trackbars
	th1 = cv.getTrackbarPos('Th1','image')
	th2 = cv.getTrackbarPos('Th2','image')
	s = cv.getTrackbarPos('switch','image')
	
	if s == 0:
		img = src
	else:
		img = cv.Canny(src,th1,th2)
		
	
	cv.imshow('image',img)
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
	
	
	
	

cv.destroyAllWindows()