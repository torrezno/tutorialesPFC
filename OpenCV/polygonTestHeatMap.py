# polygonTestHeatMap

import cv2 as cv
import numpy as np

IN_COLOR_MAX = np.array([0, 0, 255])
IN_COLOR_MIN = np.array([0, 0, 0])
OUT_COLOR_MAX = np.array([255, 0, 0])
OUT_COLOR_MIN = np.array([0, 0, 0])
CONTOUR_COLOR = np.array([255, 255, 255])
LINE_WIDTH = 2


def giveColor(d, maxD):
    if d > -1 * LINE_WIDTH and d < LINE_WIDTH:
        return CONTOUR_COLOR
    else:
        if d > 0:
            return IN_COLOR_MAX - (IN_COLOR_MAX - IN_COLOR_MIN) * d / maxD
        else:
            return OUT_COLOR_MIN + (OUT_COLOR_MAX - OUT_COLOR_MIN) * d / maxD


img_src = 'img/ml.png'
img = cv.imread(img_src)
cv.imshow('src',img)
img_grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey',img_grey)
ret, thresh = cv.threshold(img_grey, 127, 255, cv.THRESH_BINARY_INV)
cv.imshow('thres',thresh)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE,
                                      1)
contours_img = np.zeros(img_grey.shape, dtype=np.uint8)
cv.drawContours(contours_img, contours, -1, (255,255,255), 3)
cv.imshow('contours', contours_img)

maxD = max(img.shape)
res = np.zeros(img.shape, dtype=np.uint8)

maxD = 0
maxInD = 0
maxOutD = 0
indMainContour = 0
maxContour = 0
for i in range(len(contours)):
    thisContour = len(contours[i])
    if thisContour > maxContour:
        maxContour = thisContour
        indMainContour = i

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        d = cv.pointPolygonTest(contours[indMainContour], (i, j), measureDist=True)
        if d >= 0:
            if d > maxInD:
                maxInD = d
        else:
            if -1 * d > maxOutD:
                maxOutD = -1 * d


for i in range(img.shape[1]):
    for j in range(img.shape[0]):
        d = cv.pointPolygonTest(contours[indMainContour], (i, j), measureDist=True)
        if d > 0:
            c = giveColor(d, maxInD)
        else:
            c = giveColor(d, maxOutD)
        res[j, i] = c

cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()
