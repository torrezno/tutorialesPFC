# captureVideoFromCamera

import cv2 as cv

cap = cv.VideoCapture(0)

while(not cap.isOpened()):
    cap.open()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our Operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
