import cv2
import math

cap = cv2.VideoCapture('video\Video1.avi')
frameRate = cap.get(5)  # frame rate
while (cap.isOpened()):
    frameId = cap.get(1)  # current frame number
    ret, frame = cap.read()
    # frame = cv2.resize(video, (853,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Video Bola", frame)
    if (ret != True):
        break
    if frameId % math.floor(frameRate) == 0:
        filename = 'gray/img_' + str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, gray)
cap.release()
print ("Done!")