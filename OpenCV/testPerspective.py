import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('img/sudoku.png')
rows,cols,ch = img.shape
pts1 = np.float32([[72,86],[488,70],[38,511],[520,520]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
cv.imshow('img',img)
cv.imshow('dest',dst)
cv.waitKey(0)
plt.show()