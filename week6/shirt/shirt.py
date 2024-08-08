
from PIL import Image, ImageOps
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            check_valid(sys.argv[1],sys.argv[2])
        except FileNotFoundError:
            sys.exit('Input does not exist')


def overlay(image,result):

    image = Image.open(image)
    shirt = Image.open('shirt.png')
    resized_image = ImageOps.fit(image, shirt.size)
    resized_image.paste(shirt, (0,0), shirt)
    resized_image.save(result)

def check_valid(a,b):

    if not( a.endswith(('.jpg','.png')) and b.endswith(('.jpg','.png'))):
        sys.exit('Invalid output')
    elif a[-3:]==b[-3:]:
        overlay(a,b)
    else: sys.exit('Input and output have different extensions')


if __name__ == "__main__":

    main()
