import cv2

face = cv2.CascadeClassifier('file-xml/face-detect.xml')
eye = cv2.CascadeClassifier('file-xml/eye-detect.xml')
smile = cv2.CascadeClassifier('file-xml/smile-detect.xml')

""" Face Eye Smile Detection"""
img = cv2.imread('img/mut_ndah.jpg')
img = cv2.resize(img,(640,480))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvt = convert
muka = face.detectMultiScale(gray, 1.3, 4) # 1.4, 4

for (x, y, w, h) in muka:       #sumbu x dan y, sdgkan w & h = lebar dan tinggi muka
    # membuat kotak pada wajah gambar img mulai dari kordinat (x, y) sampai kodrdinat (x+w, y+h) dengan warna hijau(0,255,0) tebal garis 5px
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Region of Image (ROI) untuk mata
    roi_warna = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]

    # h,w = roi_warna.shape[:2]
    # print(w,h)
    # if w > 200:
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # else:
    #     pass
    # print(x,y)

    mata = eye.detectMultiScale(roi_gray, 1.3, 2)
    senyum = smile.detectMultiScale(roi_gray, 1.9, 8)

    for (mx, my, mw, mh) in mata:
        roi_mata = mata[my:my+mh, mx:mx+mw]
        h,w = roi_mata.shape[:2]
        # cv2.rectangle(roi_warna, (mx, my), (mx + mw, my + mh), (0, 255, 255), 1)
        if mw > 21:
            cv2.rectangle(roi_warna, (mx, my), (mx + mw, my + mh), (0, 255, 255), 1)
        else:
            pass
            # cv2.rectangle(roi_warna, (mx, my), (mx + mw, my + mh), (255, 0, 0), 1)
        print(mw,mh)

    for (sx, sy, sw, sh) in senyum:
        cv2.rectangle(roi_warna, (sx, sy), (sx + sw, sy + sh), (255, 255, 0), 1)

cv2.imshow('face eye smile detection', img)

"""Face Smile Detection"""
img = cv2.imread('img/studek.JPG')
img = cv2.resize(img,(640,480))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvt = convert
muka = face.detectMultiScale(gray, 1.3, 4) # 1.4, 4

for (x, y, w, h) in muka:
    # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Region of Image (ROI) untuk mata
    roi_warna = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]

    h,w = roi_warna.shape[:2]
    # print(w,h)
    if w > 56:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print(x,y,w,h)
    else:
        pass
    # print(x,y)

    mata = eye.detectMultiScale(roi_gray, 1.01, 1)
    senyum = smile.detectMultiScale(roi_gray, 1.2, 1)

    for (mx, my, mw, mh) in mata:
        roi_mata = mata[my:my+mh, mx:mx+mw]
        # cv2.rectangle(roi_warna, (mx, my), (mx + mw, my + mh), (0, 255, 255), 1)
        # h,w = roi_mata.shape[:2]
        # if mw > 21:
        #     cv2.rectangle(roi_warna, (mx, my), (mx + mw, my + mh), (0, 255, 255), 1)
        # else:
        #     pass
            # cv2.rectangle(roi_warna, (mx, my), (mx + mw, my + mh), (255, 0, 0), 1)
        # print(mw,mh)

    for (sx, sy, sw, sh) in senyum:
        roi_mata = mata[sy:sy + sh, sx:sx + sw]
        if w > 74:
            if sw == 37:
                cv2.rectangle(roi_warna, (sx, sy), (sx + sw, sy + sh), (255, 255, 0), 1)
        else:
            cv2.rectangle(roi_warna, (sx, sy), (sx + sw, sy + sh), (255, 255, 0), 1)

cv2.imshow('Face and Smile Detection', img)

cv2.waitKey(0)
cv2.destroyAllWindows()