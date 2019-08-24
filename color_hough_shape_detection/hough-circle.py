import cv2
import numpy as np

img = cv2.imread('lingkaran.PNG',0) #img = cv2.imread('lingkaran.PNG',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=100,param2=100,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    print(i[0], i[1]) # i[0] = x, i[1] = y, i[2] = r
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,0,0),5)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cam = cv2.VideoCapture(0)
# while 1:
#     _,img = cam.read()
#     img = cv2.medianBlur(img,5)
#     cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#
#     circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=100,param2=100,minRadius=0,maxRadius=0)
#
#     circles = np.uint16(np.around(circles))
#
#     for i in circles[0,:]:
#         print(i[0], i[1]) # i[0] = x, i[1] = y, i[2] = r
#         # draw the outer circle
#         cv2.circle(cimg,(i[0],i[1]),i[2],(0,0,0),5)
#         # draw the center of the circle
#         cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
#
#     cv2.imshow('detected circles',cimg)
#     if cv2.waitKey(1) & 0xff == 27:
#         break
# cam.release()
# cv2.destroyAllWindows()