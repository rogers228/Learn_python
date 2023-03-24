from PIL import Image
import sys, os
from functools import partial

def compress_image(input_image_path, quality, output_image_path):
    with Image.open(input_image_path) as image:
        image.save(output_image_path, optimize=True, quality=quality)

def test1():
    this = r'C:\Users\user\Documents\GitHub\Learn_python\note\module\41_Pillow'
    this_img = partial(os.path.join, this)

    img = 'head_1.jpg'
    try:
        compress_image(this_img(img), 25, this_img(f'comp_{img}'))
    except:
        print('error')
    print('ok')

if __name__ == '__main__':
    test1()