import numpy as np
import cv2 as cv

#https://docs.opencv.org/4.0.1/dc/d2e/tutorial_py_image_display.html

img = cv.imread('./img/messi5.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF
if k == 27: #If ESC exit (It exits on every key press, in theory it shouldn't)
	cv.destroyAllWindows()
elif k == ord('s'): #If 's' save
	cv.imwrite('./img/messigray.png',img)
	cv.destroyAllWindows()