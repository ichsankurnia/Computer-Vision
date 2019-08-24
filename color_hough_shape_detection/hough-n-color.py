import cv2
import imutils
import numpy as np

orangeLower = (0, 50, 80)
orangeUpper = (20, 255, 255)

cam = cv2.VideoCapture(0)
while 1:
    _, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.1, 75)

    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, orangeLower, orangeUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # only proceed if the radius meets a minimum size
            if radius > 5:
                #for x,y,r in circles: # Berdasarkan bentuk
                for i in circles:
                    print(x, y)
                    # cv2.circle(gray, (i[0], i[1]), i[2], (0, 255, 0), 4) # bentuk
                    # cv2.circle(gray, (i[0], i[1]), 2, (0, 0, 255), 3) # bentuk
                    cv2.circle(gray, (int(x), int(y)), int(radius), (0, 255, 0), 4) # warna
                    cv2.circle(gray, (int(x), int(y)), 2, (0, 0, 255), 3)   #
                    cv2.imshow("hough & colour", gray)

    else:
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # only proceed if the radius meets a minimum size
            if radius > 5:
                cv2.circle(frame, (int(x), int(y)), int(radius), orangeUpper, 2)
                cv2.circle(frame, (int(x), int(y)), 2, (0, 0, 255), 3)
                print(x,y)

            cv2.imshow("colour", frame)

    if cv2.waitKey(1) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()