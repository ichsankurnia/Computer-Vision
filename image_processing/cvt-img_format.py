import cv2
import os
from PIL import Image
from glob import glob
import cv2

path = glob('./**/*.bmp', recursive=True) # Define your ekstension image here (ex: .jpg, .png, .JPG)

for file in path:
    img = cv2.imread(file)
    # size = cv2.resize(img, (100, 100))
    # cv2.imwrite(file[:-3] + 'bmp', size)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(file[:-3] + 'jpg', gray)
    cv2.imwrite(file[:-3] + 'jpg', img) # Convert image to another format

""""
BASE_DIR = os.path.dirname(__file__)    # path project ini
image_dir = os.path.join(BASE_DIR, "img")   # path of img
print(image_dir) # D:/Ichsan/Kuliah/Python/PyCharm/Test\img

for root, dirs, files in os.walk(image_dir):
    print(root)     # D:/Ichsan/Kuliah/Python/PyCharm/Test\img
    print(dirs)     # []
    print(files)    # ['1551851669326.bmp','1551851669326.bmp', '1551851669327.bmp', '1551851669329.bmp', ....]
    for file in files:  # temukan file dalam files yg ada pada folder img tadi
        print(file) # 1551851669326.bmp      1551851669326.bmp    1551851669327.bmp     1551851669329.bmp
        with open(file, 'rb') as f:
            img = Image.load(f)
            img.save('p/'+file+'.jpg')

path = glob.glob("D:/Ichsan/Kuliah/Python/PyCharm/Test/img/*.jpg")
cv_img = []
for img in path:
    n = cv2.imread(img)
    cv_img.append(n)

for i in cv_img:
    print(i)
"""