# 2DHist

import numpy as np
import cv2 as cv
import myLib as aux

# Some Constants
H = 0
S = 1
V = 2
B = 0
G = 1
R = 2
H_MAX = 180
S_MAX = 256
H_MIN = 0
S_MIN = 0
scale = 3
# If th = -1 it uses as V the count of pixels.
# if th = -2 it uses a reescaled count of pixels as V
# Else its the threhold over that is 255 and under 0 for v
threshold = 10
capVideo=True

toShow = []

cap = cv.VideoCapture(0)
while(True):
    if capVideo:
        ret,img_src = cap.read()
    else:
        img_src = cv.imread('img/home.jpg')

    toShow.append(['img_src', img_src])

    hsv_src = cv.cvtColor(img_src, cv.COLOR_BGR2HSV)
    #toShow.append(['hsv_src', hsv_src])

    t_h0 = cv.getTickCount()
    hist = cv.calcHist([hsv_src], [H, S], None,
                       [H_MAX, S_MAX], [H_MIN, H_MAX, S_MIN, S_MAX])
    t_h1 = cv.getTickCount()
    histMod = np.zeros((scale * H_MAX, scale * S_MAX, 3), dtype=np.uint8)

    hist_max = hist.max()
    hist_avg = np.mean(hist)
    hist_std = np.std(hist)
    clip_max = min(hist_avg + 2 * hist_std, hist_max)
    clip_min = max(hist_avg - 2 * hist_std, 0)

    #print 'Hist max={} avg={} std={} clip_min={} clip_max={}'.format(hist_max, hist_avg, hist_std, clip_min, clip_max)

    t_b0 = cv.getTickCount()

    for h in range(H_MAX):
        for s in range(S_MAX):
            binValue = hist[h, s]
            h0 =  h * scale
            h1 =  h0 + scale
            s0 = s * scale
            s1 = s0 + scale
            histMod[h0:h1, s0:s1, H] = h
            histMod[h0:h1, s0:s1, S] = s
            if (threshold == -2):
                if binValue == 0:
                    binValueCliped = 0
                elif binValue <= clip_min:
                    binValueCliped = clip_min
                elif binValue >= clip_max:
                    binValueCliped = clip_max
                else:
                    binValueCliped = binValue
                # Llamamos a rescale2 porque empaquetar y desmpaquetar y llamar a la 
                # funcion le cuesta bastante
                vfloat = aux.rescale2(binValueCliped, clip_min, clip_max, 0, 255)
                v = int(vfloat)
            elif threshold == -1:
                v = binValue
            else:
                if (binValue < threshold):
                    v = 0
                else:
                    v = 255
            histMod[h * scale:(h + 1) * scale, s * scale:(s + 1) * scale, V] = v
    t_b1 = cv.getTickCount()

    histMod = cv.cvtColor(histMod, cv.COLOR_HSV2BGR)


    toShow.append(['histMod', histMod])
    toShow.append(['hist', hist])



    for t in toShow:
        cv.imshow(t[0], t[1])

    if capVideo:
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
    else:
        cv.waitKey(0)
        break
t_b = (t_b1 - t_b0)/cv.getTickFrequency()
t_h = (t_h1 - t_h0)/cv.getTickFrequency()
print "Bucle took : {}ms Hist {}ms".format(t_b, t_h)
print img_src.shape
cv.destroyAllWindows()
