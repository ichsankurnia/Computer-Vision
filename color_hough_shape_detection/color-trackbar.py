import cv2
import numpy as np
import imutils

def kamera(x):
    pass

cam = cv2.VideoCapture(0)
cv2.namedWindow('HSV')
# kernel = np.ones((5, 5), np.uint8)

# easy assigments
hh = 'Hue High'
hl = 'Hue Low'
sh = 'Saturation High'
sl = 'Saturation Low'
vh = 'Value High'
vl = 'Value Low'

# Begin Creating trackbars for each
cv2.createTrackbar(hl, 'HSV', 0, 180, kamera)
cv2.createTrackbar(hh, 'HSV', 0, 180, kamera)
cv2.createTrackbar(sl, 'HSV', 0, 255, kamera)
cv2.createTrackbar(sh, 'HSV', 0, 255, kamera)
cv2.createTrackbar(vl, 'HSV', 0, 255, kamera)
cv2.createTrackbar(vh, 'HSV', 0, 255, kamera)

while 1:
    _, frame = cam.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    # convert to HSV from BGR
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # read trackbar positions for all
    hul = cv2.getTrackbarPos(hl, 'HSV')
    huh = cv2.getTrackbarPos(hh, 'HSV')
    sal = cv2.getTrackbarPos(sl, 'HSV')
    sah = cv2.getTrackbarPos(sh, 'HSV')
    val = cv2.getTrackbarPos(vl, 'HSV')
    vah = cv2.getTrackbarPos(vh, 'HSV')
    # make array for final values
    HSVLOW = np.array([hul, sal, val])
    HSVHIGH = np.array([huh, sah, vah])

    # apply the range on a mask
    kernel = np.ones((9, 9), np.uint8)
    mask = cv2.inRange(hsv, HSVLOW, HSVHIGH)
    mask1 = cv2.erode(mask, kernel)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        # print(center)   # (259, 103)

        if radius > 0.5:
            cv2.circle(frame, (int(x), int(y)), int(radius), (huh,sah,vah), 2)
            cv2.circle(frame, (int(x), int(y)), 2, (0, 0, 255), 3)
            print(int(x),int(y)) # 258.0 163.40261840820312

    cv2.imshow('HSV', res)
    cv2.imshow('mask', mask1)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(5) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
