from glob import glob
import cv2

path = glob('./**/*.bmp', recursive=True) # Define your ekstension Image here (ex: .jpg, .png, .JPG)

id = 0

for file in path:
    img = cv2.imread(file)
    h, w = img.shape[0:2]
    print(w,h)

    if w > h:
        x = (w-h)/2
        w = h
        roi = img[0:h, int(x):int(x+w)]
    elif w < h:
        y = (h-w)/2
        h = w
        roi = img[int(y):int(y+h), 0:w]
    else:
        roi = img[0:h, 0:w]

    print(w, h)
    cv2.imwrite('crop/img_' + str(id) + '.bmp', roi)
    id +=1
    # if id == count(file):
    #     #     break