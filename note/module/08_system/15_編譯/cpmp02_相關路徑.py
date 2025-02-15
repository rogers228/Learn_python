# https://iter01.com/219018.html

import sys

def test1():
    # python直譯器 解釋器 路徑
    print(sys.executable)

    # 模組路徑
    # C:\Python37\Lib\site-packages

    # python 搜尋模組的路徑
    print(sys.path)

if __name__ == '__main__':
    test1()