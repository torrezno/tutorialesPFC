#TrackColorv2

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#Roi Class definition
class Roi:
	def __init__(self):
		self.x0, self.y0, self.x1, self.y1 = -1, -1, -1, -1
		self.data = None
		self.changedFlag = True
	def setStartingPoint(self,x,y):
		self.x0 = x
		self.y0 = y
	def setEndingPoint(self,x,y):
		self.x1 = max(x,self.x0)
		self.y1 = max(y,self.y0)
		self.x0 = min(x,self.x0)
		self.y0 = min(y,self.y0)
	def getStartingPoint(self):
		return (self.x0,self.y0)
	def getEndingPoint(self):
		return (self.x1,self.y1)
	
	def refereceRoiFrom(self,target):
		self.data = target[self.y0:self.y1,self.x0:self.x1]
		self.changedFlag = True
	
	def drawRoiAreaOn(self,target,color=(255,255,255),thickness=1):
		cv.rectangle(target,self.getStartingPoint(), self.getEndingPoint(), color, thickness)
	def makeRoiMask(self,size):
		self.roiMask = np.zeros(size,dtype=np.uint8)
		self.drawRoiAreaOn(self.roiMask)
	def resetRoiMask(self):
		self.roiMask[:,:]=(0,0,0)
		
	def isRoiDef(self):
		return self.data!=None
	
	def hasChangedRoi(self):
		aux = self.changedFlag
		self.changedFlag = False
		return aux
		
	

# Constants and globals
RECTANGLE_COLOR = (255,255,255)
RECTANGLE_THICKNESS = 1
roi = Roi()

# Mouse CallBack to define ROI
roi_def_mode = False
is_roi_def = False
		
def mouseListener(event,x,y,flags,param):
	global roi_def_mode,is_roi_def
	if event == cv.EVENT_LBUTTONDOWN:#Left click (Start ROI DEF)
		roi_def_mode = True
		is_roi_def = False
		roi.resetRoiMask()
		roi.setStartingPoint(x,y)
	elif event == cv.EVENT_MOUSEMOVE:
		print (x,y)
		print 'from {}'.format(frame.shape)
		if roi_def_mode:
			is_roi_def=True
	elif event == cv.EVENT_LBUTTONUP:
		is_roi_def = True
		if roi_def_mode and is_roi_def:
			roi.setEndingPoint(x,y)
			roi_def_mode = False
			roi.drawRoiAreaOn(roi.roiMask)
			roi.refereceRoiFrom(frame)
			print 'Drawing roi from {} to {}'.format(roi.getStartingPoint(),roi.getEndingPoint())
		

# Capture definition
cap = cv.VideoCapture(0)

# Get a frame to define a mask of the same size
ret,frame = cap.read()
roi.makeRoiMask(frame.shape)

# Window and Listener Binding
cv.namedWindow('frame')
cv.setMouseCallback('frame',mouseListener)

#MainLoop
while(True):
	#Get Current Frame
	ret, frame = cap.read()
	
	frame = cv.add(frame,roi.roiMask )
	cv.imshow('frame',frame)
	cv.imshow('mask',roi.roiMask)
	if (roi.isRoiDef()):
		if (roi.hasChangedRoi()):
			cv.destroyWindow('roi')
		cv.imshow('roi',roi.data)
	
	#Escape secuence and UI Update
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break
	elif k == 104:
		hsvRoi = cv.cvtColor(roi.data,cv.COLOR_BGR2HSV)
		#TODO
		for i in range(3):
			cv.imshow('hsvroiHue',hsvRoi[:,:,1])
			plt.hist(hsvRoi[:,:,1].ravel(),256,[0,256])
			plt.show()
	else:
		print k

	