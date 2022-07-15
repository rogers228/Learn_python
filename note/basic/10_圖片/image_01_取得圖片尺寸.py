from PIL import Image
image_file = "4A309006.bmp"
img = Image.open(image_file)
width, height = img.size
print('Image size is {}, {}'.format(width, height))
