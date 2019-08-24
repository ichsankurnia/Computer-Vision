import cv2

img = cv2.imread('img/test.jpg')

edge = cv2.Canny(img, 70, 70) # 70 70 resolusinya, makin kecil makin banyak noisenya
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Detect Edge', edge)
cv2.imshow('Detect gray', gray)
cv2.imshow('Original Image', img)

cv2.waitKey(0) # kalau 0 akan langsung mengeksekusi line yg selanjutnya tanpa keyboard
cv2.destroyAllWindows()