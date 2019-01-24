#TrackColor

import cv2 as cv
import numpy as np

#Define the button down coordinates
ix, iy = -1,-1


#define range of blue color in HSV
lo_blue = np.array([90,50,50])
hi_blue = np.array([130,255,255])	
frame_mask = None
drawing = False
roi = None
roi_def = False
valid_mask = False

def mouseListener(event,y,x,flags,param):
	global lo_blue, hi_blue,frame,ix,iy,frame_mask, drawing, roi,roi_def, valid_mask
	if event == cv.EVENT_LBUTTONDOWN:
		valid_mask = False
		drawing = True
		del roi
		roi_def = False
		frame_mask[:,:] = [0,0,0]
		ix = x
		iy = y
		print hsv[x,y]
		print 'x: {} y: {}'.format(x,y)
	elif event == cv.EVENT_LBUTTONUP:
		if valid_mask:
			drawing = False
			cv.rectangle(frame_mask,(iy,ix), (y,x), (255,255,255), 1)
			print 'ROI -> ix:{} iy: {} -> x: {} y: {}'.format(ix,iy, x,y)
			x0 = min(ix,x)
			x1 = max(ix,x)
			y0 = min(iy,y)
			y1 = max(iy,y)
			roi = hsv[x0:x1,y0:y1]
			roi_def = True
		print hsv[x,y]
	elif event == cv.EVENT_MOUSEMOVE:
		if drawing:
			valid_mask = True
			frame_mask[:,:] = [0,0,0]
			cv.rectangle(frame_mask,(iy,ix), (y,x), (255,255,255), 1)
			print hsv[x,y]
		



cv.namedWindow('frame')
cv.setMouseCallback('frame',mouseListener)

cap = cv.VideoCapture(0)


while(True):
	#Take frame
	_, frame = cap.read()
	if (frame_mask == None):
		frame_mask = np.zeros((frame.shape),np.uint8)
	else:
		frame = cv.add(frame,frame_mask)
	
	#Convert to HSV
	hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	
	auxhsv = hsv.copy()
	auxhsv[:,:,0]=100
	#auxhsv[:,:,1]=200
	auxhsv[:,:,2]=100
	frame2 = cv.cvtColor(auxhsv,cv.COLOR_HSV2BGR)
	
	
	
	
	
	# Build Binary (BW) Threshold mask
	mask = cv.inRange(hsv, lo_blue, hi_blue)
	
	# And the mask with the image
	res = cv.bitwise_and(frame,frame, mask = mask)
	
	colors = np.zeros((512,512,3),dtype=np.uint8)
	colors[0:256,:]=lo_blue
	colors[256:512,:]=hi_blue
	colorsBGR = cv.cvtColor(colors,cv.COLOR_HSV2BGR)
	cv.imshow('colors',colorsBGR)
	
	cv.imshow('frame', frame)
	cv.imshow('frame2',frame2)
	cv.imshow('mask',mask)
	cv.imshow('res', res)
	if roi_def and valid_mask:
		cv.imshow('roi',roi)
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break

cv.destroyAllWindows()