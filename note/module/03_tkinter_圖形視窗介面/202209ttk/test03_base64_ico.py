import base64
from PIL import Image as pil_image
from io import BytesIO
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

def test1():
    print('test1')
    with open("Form.ico", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    print('ico_base64:')
    print(encoded_string)
    img = pil_image.open(BytesIO(base64.b64decode(encoded_string)))
    img.show()

def test2():
    ico_base64 =  b'AAABAAEAEBAQAAAAAAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAwAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAACAAACAAAAAgIAAgAAAAIAAgACAgAAAwMDAAICAgAAAAP8AAP8AAAD//wD/AAAA/wD/AP//AAD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAB/CIAAAAB///8IiAAA/////wAAAAD/////AAAAAP////8AAAAA////dwAAAAD/d3cAAAAAAHcAAO4AAAAAAO7uAAAAAADuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD////////////D///8Af//4AD//+AH///gB///4Af//+AH///gB///4Af//+AH///gP///4///////////////'
    img = pil_image.open(BytesIO(base64.b64decode(ico_base64)))
    img.show()

def test3():
    root = Tk()
    root.title('Tkinter Window Demo')
    # 視窗居中
    window_width = 600
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # https://www.motobit.com/util/base64-decoder-encoder.asp
    # 網頁服務轉換
    icon = """
    ���������(�����(������ ���������À������������������������€��€���€€�€���€�€�€€��ÀÀÀ�€€€���ÿ��ÿ���ÿÿ�ÿ���ÿ�ÿ�ÿÿ��ÿÿÿ�����������������������������€���ÿÿˆ��ÿÿÿÿ����ÿÿÿÿ����ÿÿÿÿ����ÿÿÿw����ÿww�����w��î�����îî�����î�����������������������������ÿÿÿÿÿÿÿÿÿÃÿÿüÿÿà�ÿÿàÿÿàÿÿàÿÿàÿÿàÿÿàÿÿàÿÿà?ÿÿãÿÿÿÿÿÿÿÿÿÿÿ
    """
    img= base64.b64decode(icon)
    # img=PhotoImage(data=icon) 

    root.mainloop()

if __name__ == '__main__':
    test3()