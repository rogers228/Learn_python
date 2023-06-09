from captcha.image import ImageCaptcha
from PIL import Image

def test1():
    # 創建 ImageCaptcha 實例
    s = 36 # font_height
    captcha = ImageCaptcha(height=int(1.3*s), font_sizes=(int(0.9*s), s))
    # 生成圖片，並保存到指定路徑
    image = captcha.generate('yG73sU') # data
    image = Image.open(image) # image object
    image.save('captcha.png')

if __name__ == '__main__':
    test1()

