import cv2

video = cv2.VideoCapture(0) #bisa menggunakan video jadi 'video.mp4'
while True:
    _, frame = video.read()
    _, img = video.read()

    edge = cv2.Canny(frame, 50, 50)
    # frame=cv2.resize(frame, (2000,1000))
    h, w = frame.shape[0:2]
    print(w,h)

    rect = frame[int(h/2)-75:int(h/2)+75, int(w/2)-100:int(w/2)+100] # roi dari rectangle di tengah

    cv2.line(frame,(0,int(h/2)),(w,int(h/2)), (0,255,255),2)
    cv2.line(frame, (int(w/2), 0), (int(w/2), h), (0, 255, 255), 2)
    cv2.rectangle(frame,(int(w/2)-100, int(h/2)-75), (int(w/2)+100, int(h/2)+75), (255,255,255),2 )

    cv2.imshow('Edge Detect Live Video', edge)
    cv2.imshow('Original Live Video', frame)

    if cv2.waitKey(1)== 32: # SPACE Button for capture box rectangle image
        # cv2.imwrite('img/test.jpg', rect)
        cv2.imwrite('img/test.jpg', img)

    exit = cv2.waitKey(1) & 0xff
    if exit == ord('x'):
        break


cv2.destroyAllWindows()
video.release()