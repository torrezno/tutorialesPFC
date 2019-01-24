import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./img/messi5.jpg')
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) #to hide tick values on X and Y axis
plt.show()