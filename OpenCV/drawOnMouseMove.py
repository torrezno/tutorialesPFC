#DrawCirclesAndRectanglesOnMouseMove
import numpy as np
import cv2 as cv

drawing = False # Flag to activate drawing
mode = True # if True, draw rectangle. Press 'm' to toggle to curve.

ix, iy = -1, -1
old_x, old_y = -1,-1
buffer = None


#Modified to draw continious line for circles by linear interpolation between mouse moves and to
# clear the intermediate rectangles using a buffer of the image. 

# mouse callback
def draw_circle(event, x, y, flags, param):
	global ix, iy, drawing, mode, aux, old_x, old_y, buffer,img
	
	if event == cv.EVENT_LBUTTONDOWN:
		drawing = True
		ix, iy = x, y
	
	elif event == cv.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				if buffer != None:
					img = buffer.copy()
				buffer = img.copy()
				cv.rectangle(img,(ix,iy), (x,y), (0,255,0),10)
			else:
				if old_x != -1:
					cv.line(img,(old_x,old_y),(x,y),(0,0,255),10,cv.CV_AA)
				old_x=x
				old_y=y
				cv.circle(img,(x,y),5,(0,0,255),-1)
	elif event == cv.EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			cv.rectangle(img,(ix,iy), (x,y), (0,255,0), 10)
			buffer = img.copy()
		else:
			cv.circle(img,(x,y),5,(0,0,255),-1)
			buffer = img.copy()
			old_x=-1
			old_y=-1
			
img = np.zeros((512,512,3), np.uint8)
buffer = img.copy()
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(True):
	cv.imshow('image',img)
	k = cv.waitKey(1) & 0xFF
	if k == ord('m'):
		mode = not mode
	elif k == 27:
		break
cv.destroyAllWindows()