import cv2

face = cv2.CascadeClassifier('file-xml/face-detect.xml')
eye = cv2.CascadeClassifier('file-xml/eye-detect.xml')

cam = cv2.VideoCapture(0)
while 1:
    _, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvt = convert
    muka = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in muka:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

        # Region of Image (ROI) untuk mata
        roi_warna = img[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        mata = eye.detectMultiScale(roi_gray, 1.3, 3)

        for (mx, my, mw, mh) in mata:
            cv2.rectangle(roi_warna, (mx, my), (mx + mw, my + mh), (255, 255, 0), 1)

    cv2.imshow('face and eye detection', img)
    if cv2.waitKey(1) == 27: # press ESC to exit
        break

cam.release()
cv2.destroyAllWindows()
