import os
os.getcwd()
collection = "img/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("img/" + filename, "img/" + 'rename ' + str(i) + ".bmp")