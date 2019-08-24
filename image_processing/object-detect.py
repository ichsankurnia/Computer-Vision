import cv2

video = cv2.VideoCapture(0) #bisa menggunakan video jadi 'video.mp4'
face = cv2.CascadeClassifier('ball2.xml')

while True:
    _, frame = video.read()

    edge = cv2.Canny(frame, 70, 70)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # cvt = convert
    muka = face.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in muka:  # sumbu x dan y, sdgkan w & h = lebar dan tinggi muka
        # membuat kotak pada wajah gambar img mulai dari kordinat (x, y) sampai kodrdinat (x+w, y+h) dengan warna hijau(0,255,0) tebal garis 4px
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Region of Image (ROI) untuk mata
        roi_warna = frame[y:y + h, x:x + w]
        roi_gray = gray[y:y + h, x:x + w]   #matrix wajah

    cv2.imshow('Face & Eye Detection Live Video', frame)
    cv2.imshow('Edge', edge)

    exit = cv2.waitKey(1) & 0xff #waitKey(1) exit menggunakan perintah kwyboard
    if exit == 27: # esc
        break

cv2.destroyAllWindows()
video.release()