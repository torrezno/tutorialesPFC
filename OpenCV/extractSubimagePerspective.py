#extractSubimagePerspective
import numpy as np
import cv2 as cv


x0y0 = [0,0]
x0y1 = [0,0]
x1y0 = [0,0]
x1y1 = [0,0]

counter = 0
recording = False
sectorReady = False

FILE = 'img/sudoku.png'

def drawCross(img,x,y,color=(0,255,0),thickness=1):
	cv.line(img,(x-10,y),(x+10,y),color,thickness,cv.CV_AA)
	cv.line(img,(x,y-10),(x,y+10),color,thickness,cv.CV_AA)

def mouseListener(event,x,y,flags,param):
	global recording, counter, sectorReady,x0y0,x0y1,x1y0,x1y1,img
	if event == cv.EVENT_LBUTTONDOWN:
		if recording:
			if counter == 0:
				x0y0 = [x,y]
				drawCross(img,x,y)
				print 'counter: {} coord: {}'.format(counter,x0y0)
			elif counter == 1:
				x0y1 = [x,y]
				drawCross(img,x,y)
				print 'counter: {} coord: {}'.format(counter,x0y1)
			elif counter == 2:
				x1y0 = [x,y]
				drawCross(img,x,y)
				print 'counter: {} coord: {}'.format(counter,x1y0)
			elif counter == 3:
				x1y1 = [x,y]
				drawCross(img,x,y)
				print 'counter: {} coord: {}'.format(counter,x1y1)
				recording = False
				sectorReady = True
			counter+=1
		
			
img = cv.imread(FILE)
rows,cols,ch = img.shape
pts1 = np.float32([[0,0],[rows,0],[0,cols],[rows,cols]])

cv.namedWindow('Source')
cv.setMouseCallback('Source',mouseListener)

while(True):
	cv.imshow('Source',img)
	
	if sectorReady:
		print 'Sector ready, building perspective'
		pts2 = np.float32([x0y0,x0y1,x1y0,x1y1])
		print 'points1 {}'.format(pts1)
		print 'points2 {}'.format(pts2)
		M = cv.getPerspectiveTransform(pts2,pts1)
		sector = cv.warpPerspective(img,M,(rows,cols))
		print 'Sector: {}'.format(sector)
		cv.imshow('Sector',sector)
		sectorReady = False
	
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break
	elif k == 114:
		if recording:
			img = cv.imread(FILE)
			sectorReady = False
			counter = 0
		recording = not recording
		