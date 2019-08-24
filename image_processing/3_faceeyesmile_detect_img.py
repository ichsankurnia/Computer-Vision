import cv2

face = cv2.CascadeClassifier('file-xml/face-detect.xml')
eye = cv2.CascadeClassifier('file-xml/eye-detect.xml')
smile = cv2.CascadeClassifier('file-xml/smile-detect.xml')

img = cv2.imread('img/mutia.JPG')
# img = cv2.imread('img/test.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvt = convert
muka = face.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in muka:       #sumbu x dan y, sdgkan w & h = lebar dan tinggi muka
    #membuat kotak pada wajah gambar img mulai dari kordinat (x, y) sampai kodrdinat (x+w, y+h) dengan warna hijau(0,255,0) tebal garis 5px
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Region of Image (ROI) untuk mata
    roi_warna = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]
    mata = eye.detectMultiScale(roi_gray, 1.3, 3)
    senyum = smile.detectMultiScale(roi_gray, 1.3, 3)

    for (mx, my, mw, mh) in mata:
        cv2.rectangle(roi_warna, (mx, my), (mx + mw, my + mh), (255, 255, 0), 1)

    for (sx, sy, sw, sh) in senyum:
        cv2.rectangle(roi_warna, (sx, sy), (sx + sw, sy + sh), (255, 255, 0), 1)

cv2.imshow('face and eye detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
#
# face = cv2.CascadeClassifier('file-xml/face-detect.xml')
# eye = cv2.CascadeClassifier('file-xml/eye-detect.xml')
# smile = cv2.CascadeClassifier('file-xml/smile-detect.xml')
#
# # img = cv2.imread('img/mutia.JPG')
# img = cv2.imread('img/test.jpg')
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvt = convert
# muka = face.detectMultiScale(gray, 1.3, 5)
#
# for (x, y, w, h) in muka:       #sumbu x dan y, sdgkan w & h = lebar dan tinggi muka
#     #membuat kotak pada wajah gambar img mulai dari kordinat (x, y) sampai kodrdinat (x+w, y+h) dengan warna hijau(0,255,0) tebal garis 5px
#     cv2.rectangle(img, (x, y), (x+w, y+h), (150, 150, 0), 3)
#
# cv2.imshow('face and eye detection', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()