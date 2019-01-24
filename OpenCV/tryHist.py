
import numpy as np
import cv2 as cv
import aux_coord as coord

nBins = 256
max_height = 512
max_width = 1024
innerTopMargin = 10
Lmargin = 50
Rmargin = 10
Tmargin = 10
Bmargin = 20
BColor = [255, 255, 255]
Color = [20, 20, 100]
SColor = [0, 0, 0]

img = cv.imread('img/wiki.jpg', 0)

hist, bins = np.histogram(img.flatten(), nBins, [0, 256])

manualHist = np.zeros((max_height, max_width, 3), dtype=np.uint8)
manualHist[:, :] = BColor

max_value = max(hist)
size = (max_width, max_height)


height_step = (1.0 * max_height - Tmargin -
               Bmargin - innerTopMargin) / max_value
width_step = (1.0 * max_width - Lmargin - Rmargin) / (nBins + 1)
print '{} - {} - {} / {}'.format(max_height, Tmargin, Bmargin, max_value)
print 'height_step = {}'.format(height_step)
print '{} - {} - {} / {}'.format(max_width, Lmargin, Rmargin, nBins + 1)
print 'width_step = {}'.format(width_step)


for i in range(len(hist)):
    x0 = int(i * width_step + Lmargin)
    x1 = int((i + 1) * width_step + Lmargin)
    y0 = int(0 + Bmargin)
    y1 = int(height_step * hist[i] + Bmargin)
    c00 = coord.toCV((x0, y0), size)
    c11 = coord.toCV((x1, y1), size)
    c01 = coord.toCV((x0, y1), size)
    print('Drawing rectangle {}, {} for bin {} with value {} in color {}'.format(
        c00, c11, i, hist[i], Color))
    cv.rectangle(manualHist, c00, c11, Color, -1)
    cv.line(manualHist, c00, c01, SColor, 1)


#Axis and Legends
SHOW_GRID = True
font = cv.FONT_HERSHEY_PLAIN
fontScale = 0.75
fontColor = (0, 0, 0)
lineType = cv.CV_EPNP
AtextPos = (0, 0)

xGridDivisions = 20
yGridDivisions = 5

yAdjustText = 15
xAdjustText = 10
xAdjustTextOnYaxis = 40

axisX0 = Lmargin
axisY0 = Bmargin
axisX1 = max_width - Rmargin
axisY1 = max_height - Tmargin

c00 = coord.toCV((axisX0, axisY0), size)
c01 = coord.toCV((axisX0, axisY1), size)
c10 = coord.toCV((axisX1, axisY0), size)
c11 = coord.toCV((axisX1, axisY1), size)
cv.line(manualHist, c00, c01, [0, 0, 0], 1)
cv.line(manualHist, c00, c10, [0, 0, 0], 1)
cv.line(manualHist, c11, c01, [0, 0, 0], 1)
cv.line(manualHist, c11, c10, [0, 0, 0], 1)

xGridStep = (axisX1 - axisX0) / xGridDivisions
xValueStep = nBins / xGridDivisions
textPos = (axisX0 - xAdjustText, axisY0 - yAdjustText)
linePos = (axisX0, axisY0)
if SHOW_GRID:
    halfTick = max(max_height, max_width)
else:
    halfTick = 3
value = 0
for x in range(xGridDivisions):
    textPos = (textPos[0] + xGridStep, textPos[1])
    linePos = (linePos[0] + xGridStep, linePos[1])
    linePos0 = coord.toCV((linePos[0], linePos[1] - halfTick), size)
    linePos1 = coord.toCV((linePos[0], linePos[1] + halfTick), size)
    value = value + xValueStep

    cv.line(manualHist, linePos0, linePos1, [0, 0, 0], 1)
    cv.putText(manualHist, "{}".format(value), coord.toCV(
        textPos, size), font, fontScale, fontColor, lineType)


textPos = (axisX0 - xAdjustTextOnYaxis, axisY0 - 5)
linePos = (axisX0, axisY0)
yGridStep = (axisY1 - axisY0) / yGridDivisions
yValueStep = max_value / xGridDivisions
value = 0
for y in range(yGridDivisions):
    linePos = (linePos[0], linePos[1] + yGridStep)
    linePos0 = coord.toCV((linePos[0] - halfTick, linePos[1]), size)
    linePos1 = coord.toCV((linePos[0] + halfTick, linePos[1]), size)
    cv.line(manualHist, linePos0, linePos1, [0, 0, 0], 1)
    value = value + yValueStep
    textPos = (textPos[0], textPos[1] + yGridStep)
    cv.putText(manualHist, "{}".format(value), coord.toCV(
        textPos, size), font, fontScale, fontColor, lineType)


cv.imshow('manualHist', manualHist)
cv.waitKey(0)
cv.destroyAllWindows()
