#draw logo

import numpy as np
import cv2 as cv

#Create a black image
img = np.zeros((512,512,3), np.uint8)

#step = 32
#for x in range(0,512,step):
#	cv.line(img,(x,0),(x,512),(255,255,255),1)
#	cv.line(img,(0,x),(512,x),(255,255,255),1)
	
center_red = (256,144)
center_green = (144,352)
center_blue = (368,352)
r = 100
ri= 50
black = (0,0,0)
red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
fill = -1
start_angle= 0
end_angle = 300
tilt_red = 120
tilt_green = 120
tilt_blue = 120


#Elipse sin llenar no tiene los cortes rectos sino curvados
cv.ellipse(img,center_red, (r,r),120,start_angle,end_angle,red,fill)
cv.circle(img,center_red,ri,black,fill)
cv.ellipse(img,center_green, (r,r),360,start_angle,end_angle,green,fill)
cv.circle(img,center_green,ri,black,fill)
cv.ellipse(img,center_blue, (r,r),300,start_angle,end_angle,blue,fill)
cv.circle(img,center_blue,ri,black,fill)


while(True):
	cv.imshow('image',img)
	k = cv.waitKey(0) & 0xFF
	if k == 27: #If ESC exit (It exits on every key press, in theory it shouldn't)
		cv.destroyAllWindows()
		break
