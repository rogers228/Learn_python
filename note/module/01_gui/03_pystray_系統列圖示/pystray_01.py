import pystray
from pystray import MenuItem as item
from PIL import Image

# 定義點擊事件
def on_click(icon, item):
    print(f'Clicked {item}')

# 定義退出事件
def on_exit(icon, item):
    icon.stop()

# 創建圖示和功能表
image = Image.open(r'C:\Users\user\Documents\GitHub\Learn_python\note\module\03_pyqt\python_icon.ico')
menu = (item('Open', lambda: print('Open')),
        item('Save', lambda: print('Save')),
        item('Exit', on_exit))

# 創建圖示
icon = pystray.Icon("name", image, "Title", menu)
icon.run()
