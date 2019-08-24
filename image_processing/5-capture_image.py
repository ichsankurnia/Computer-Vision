import cv2

face = cv2.CascadeClassifier('file-xml/face-detect.xml')

video = cv2.VideoCapture(1)

while 1:
    _,frame = video.read()

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == 32:
        cv2.imwrite('img/1.jpg', frame)
        print("Capture Success")
        break

""" Capture Head of user"""
# while 1:
#     _, frame = video.read()
#     _, img = video.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     for (x, y, w, h) in face.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),1.3,5):
#         # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         if cv2.waitKey(1) == 32:
#             # cv2.imwrite('img/userori.png', img[y: y+h, x: x+w])
#             cv2.imwrite('img/' + '.png', img[y - 75:y + h + 30, x - 10:x + w + 10])
#             print("Capture Success")
#             break
#     cv2.imshow('Face Detection', frame)

video.release()
cv2.destroyAllWindows()