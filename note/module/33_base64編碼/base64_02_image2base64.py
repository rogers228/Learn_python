import base64
import sys, os
from functools import partial

def image2base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def test1():
    # mdhead = r'C:\Users\user\Documents\Rogers\ysmd_flask_svelte\39_flask\static\mdhead'
    mdhead = r'C:\Users\user\Documents\GitHub\Learn_python\note\module\41_Pillow'
    image = partial(os.path.join, mdhead)
    encoded_string = image2base64(image('comp_head_1.jpg'))
    print(encoded_string)

if __name__ == '__main__':
    test1()