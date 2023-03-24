from PIL import Image
import sys, os
from functools import partial

def resize_image(input_image_path, width, output_image_path):
    with Image.open(input_image_path) as image:
        height = int((float(image.size[1]) * float(width / float(image.size[0]))))
        image = image.resize((width, height), resample=Image.LANCZOS)
        image.save(output_image_path)

def test1():
    mdhead = r'C:\Users\user\Documents\Rogers\ysmd_flask_svelte\39_flask\static\mdhead'
    mdhead_img = partial(os.path.join, mdhead)

    this = r'C:\Users\user\Documents\GitHub\Learn_python\note\module\41_Pillow'
    this_img = partial(os.path.join, this)

    img = 'head_1.jpg'
    try:
        resize_image(mdhead_img(img), 600, this_img(img))
    except:
        print(error)
    print('ok')

if __name__ == '__main__':
    test1()