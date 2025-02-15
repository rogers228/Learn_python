import sys
sys.path.append(r'C:\python37_lib') #使用者模組資料夾路徑
# 第三方模組需另外安裝
# 可從開發環境 C:\Python37\Lib\site-packages 將模組複製

import os
import PySimpleGUI as sg

def test1():
    sg.theme('SystemDefault')
    layout = [  [sg.Text('Computer Name')],
                [sg.InputText(os.getenv('COMPUTERNAME'))],
                [sg.Text('')],
                [sg.Button('ok')] ]
    w = sg.Window('Python', layout, 
                    size=(400, 120),
                    resizable=True)
    while True:
        event, values = w.read()
        if event == sg.WIN_CLOSED or event == 'ok': # if user closes window or clicks cancel
            break

if __name__ == '__main__':
    test1()

# 編譯單個py檔案
# cmd
# python -m main.py
# python main.cpython-37.pyc