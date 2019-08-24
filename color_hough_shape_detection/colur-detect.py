import cv2
import numpy as np

# img = cv2.imread('colour.png')
#
# hav = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# lower_red = np.array([0, 50, 80])
# upper_red = np.array([20, 255, 255])
# # lower_red = np.array([178, 179, 0])
# # upper_red = np.array([255,255,255])
#
# mask = cv2.inRange(hav, lower_red, upper_red)
#
# cv2.imshow('Original', img)
# cv2.imshow('Colour Detect', mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cam = cv2.VideoCapture(0)
while 1:
    _,img = cam.read()

    hav = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 50, 80])
    upper_red = np.array([20, 255, 255])

    mask = cv2.inRange(hav, lower_red, upper_red)

    cv2.imshow('Original', img)
    cv2.imshow('Colour Detect', mask)

    if cv2.waitKey(1) & 0xff==27:
        break
cam.release()
cv2.destroyAllWindows()