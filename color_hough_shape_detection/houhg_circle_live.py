import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while 1:
    _, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.3, 30)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            print(x,y)
            cv2.circle(gray, (x,y), r, (0,255,0),4)
            cv2.rectangle(gray, (x-5, y-5), (x+5, y+5), (0,0,255), 3)

    cv2.imshow('output', gray)
cam.release()
cv2.destroyAllWindows()

# frame = cv2.imread('lingkaran.PNG')
#
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# cv2.imshow('frame', gray)
#
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 75)
#
# if circles is not None:
#     circles = np.round(circles[0, :]).astype("int")
#
#     for (x, y, r) in circles:
#         print(x,y)
#         cv2.circle(gray, (x,y), r, (0,255,255),4)
#         cv2.rectangle(gray, (x-5, y-5), (x+5, y+5), (0,0,255), 3)
#
# cv2.imshow('output', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
