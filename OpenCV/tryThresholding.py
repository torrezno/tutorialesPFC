#thresholding try

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('img/screenshot.png')

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

h = 0
s = 1
v = 2

hsvH = hsv[:,:,h]
hsvS = hsv[:,:,s]
hsvV = hsv[:,:,v]

plt.subplot(221),plt.imshow(img),plt.title('Source')
plt.subplot(222),plt.imshow(hsvH,cmap='gray'),plt.title('Canal H')
plt.subplot(223),plt.imshow(hsvS,cmap='gray'),plt.title('Canal S')
plt.subplot(224),plt.imshow(hsvV,cmap='gray'),plt.title('Canal V')
plt.show()

hlo = 90
hhi = 130

ret, th1 = cv.threshold(hsvH,hlo,255,cv.THRESH_TOZERO)
cv.imshow('loH',th1)
ret, th2 = cv.threshold(th1,hhi,255,cv.THRESH_TOZERO_INV)
cv.imshow('hiH',th2)
cv.imshow('Canal H', hsvH)
th2[th2>=250] = 0
cv.imshow('hiH2',th2)
cv.waitKey(0)

#cv.imshow('Source',img)
#cv.imshow('Canal H',hsvH)
#cv.imshow('Canal S',hsvS)
#cv.imshow('Canal V',hsvV)

#cv.waitKey(0)