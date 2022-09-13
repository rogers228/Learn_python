import os
from PIL import Image

def test1():
    imgf = r'\\220.168.100.104\油聖油昇共用資料庫-1\0-部門間資料分享平台使用完應刪除\1-設計課\給小陸\bomcost\bmp_s'
    no = '4A611014.bmp'
    print(os.path.join(imgf, no))
    img = Image.open(os.path.join(imgf, no))
    (w, h) = img.size # width, height
    print(w, h) 

if __name__ == '__main__':
    test1()