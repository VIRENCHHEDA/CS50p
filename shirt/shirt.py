import sys
import os
from PIL import Image,ImageOps

if  len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith((".jpg", ".png", ".jpeg")) or not sys.argv[2].endswith((".jpg", ".png", ".jpeg")):
    sys.exit("File does not exist")
#here double'(())' brackets are used in endswitch as per documentation so that is can detect any of the multiple values in it
else:
    # Getting the extension of the arguments:
    path_1 = os.path.splitext(sys.argv[1])
    path_2 = os.path.splitext(sys.argv[2])

if path_1[1].lower() != path_2[1].lower():
    sys.exit("Input and Output have different extensions")
else:
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as image:
            photo = ImageOps.fit(image, size=(600, 600))
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")