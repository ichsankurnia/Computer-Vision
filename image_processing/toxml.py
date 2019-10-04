import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET

face_cascade = cv2.CascadeClassifier('file-xml/face-detect.xml') # ganti sama file cascade kamu

folder = 'img'  # simpan gambar dan file py ini dalam folder yg sama, cantumkan nama folder nya disini
label = 'face'  # nama objek yg pengen di detect

BASE_DIR = os.path.dirname(__file__)
image_dir = os.path.join(BASE_DIR, 'img')
print(image_dir)

for root, dirs, files in os.walk(image_dir):
    for file in files:
        # if file.endswith('jpg') or file.endswith('JPG') or file.endswith('png'):
        if file.endswith('jpg'):
            path_img = image_dir+"/"+file
            objects = []

            print(path_img)
            # print(root,dirs,file)

            image = cv2.imread(path_img)
            height, width, depth = image.shape

            print(height,width,depth)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # cvt = convert
            face = face_cascade.detectMultiScale(gray, 1.3, 5)
            min, max = [], []
            x,y,w,h = 0,0,0,0
            for x, y, w, h in face:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # cv2.putText(image, 'ini koordinat', (x+w,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)
                min.append((x, y))
                max.append((x+w, y+h))
                objects.append(label)
                print(x, y, x+w, y+h)

            cv2.imshow("img", image)
            cv2.waitKey(0)

            annotation = ET.Element('annotation')
            ET.SubElement(annotation, 'folder').text = folder
            ET.SubElement(annotation, 'filename').text = file
            ET.SubElement(annotation, 'path').text = path_img

            source = ET.SubElement(annotation, 'source')
            ET.SubElement(source, 'database').text = 'Unknown'

            size = ET.SubElement(annotation, 'size')
            ET.SubElement(size, 'width').text = str(width)
            ET.SubElement(size, 'height').text = str(height)
            ET.SubElement(size, 'depth').text = str(depth)
            ET.SubElement(annotation, 'segmented').text = '0'

            # for obj, topl, botr in zip(objects, tl, br):
            # ob = ET.SubElement(annotation, 'object')
            # ET.SubElement(ob, 'name').text = objects
            # ET.SubElement(ob, 'pose').text = 'Unspecified'
            # ET.SubElement(ob, 'truncated').text = '0'
            # ET.SubElement(ob, 'difficult').text = '0'

            # bbox = ET.SubElement(ob, 'bndbox')
            # ET.SubElement(bbox, 'xmin').text = str(x)
            # ET.SubElement(bbox, 'ymin').text = str(y)
            # ET.SubElement(bbox, 'xmax').text = str(w)
            # ET.SubElement(bbox, 'ymax').text = str(h)

            for obj, topl, botr in zip(objects, min, max):
                ob = ET.SubElement(annotation, 'object')
                ET.SubElement(ob, 'name').text = obj
                ET.SubElement(ob, 'pose').text = 'Unspecified'
                ET.SubElement(ob, 'truncated').text = '0'
                ET.SubElement(ob, 'difficult').text = '0'

                # xmin,ymin
                bbox = ET.SubElement(ob, 'bndbox')
                ET.SubElement(bbox, 'xmin').text = str(topl[0])
                ET.SubElement(bbox, 'ymin').text = str(topl[1])
                ET.SubElement(bbox, 'xmax').text = str(botr[0])
                ET.SubElement(bbox, 'ymax').text = str(botr[1])

            xml_str = ET.tostring(annotation)
            root = etree.fromstring(xml_str)
            xml_str = etree.tostring(root, pretty_print=True)
            file = str(file)
            img_name = file[:-3]
            save_path = os.path.join(folder, file.replace('jpg', 'xml'))
            with open(save_path, 'wb') as temp_xml:
                temp_xml.write(xml_str)
