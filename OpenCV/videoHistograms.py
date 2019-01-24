# histograms

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_src = 'img/home.jpg'
cap = cv.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    #img = cv.imread(img_src, 0)
    img = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    bins = 255
    max_width = 1000
    max_height = 512
    bin_size = max_width/bins
    height_size = 5
    top_margin = 10

    BAR_COL = np.array([250, 250, 250])
    BCK_COL = [255, 255, 255]




    hist = cv.calcHist([img], [0], None, [bins + 1], [0, bins + 1])

    height = max(hist)

    if height * height_size > max_height - top_margin:
        height_size = (max_height - top_margin) / height
    if bins * bin_size > max_width:
        bin_size = 1.0 * max_width / bins
    hist_img = np.zeros((max_height, max_width, 3), dtype=np.uint8)
    hist_img[:, :] = BCK_COL

    for x in range(bins):
        value = hist[x]
        x0 = x * bin_size

        x1 = x0 + bin_size
        x0 = int(round(x0))
        x1 = int(round(x1))
        y = value * height_size

        cv.rectangle(hist_img, (x0, max_height), (x1, max_height - y), BAR_COL*x/bins, -1)
        cv.line(hist_img, (x0, max_height), (x0, max_height - y), [0, 0, 0], 1)

    cv.imshow('frame',img)
    cv.imshow('hist', hist_img)
    k = cv.waitKey(5) & 0xFF
    if( k == 27):
        break


cv.destroyAllWindows()
