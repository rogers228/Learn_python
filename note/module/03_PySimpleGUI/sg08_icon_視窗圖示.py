import PySimpleGUI as sg

sg.theme('SystemDefault')

# 定义窗口图标文件的路径
icon_path = 'test.ico'  # 替换为你的图标文件路径

layout = [
    [sg.Text('Hello, World!')],
    [sg.Button('Exit')]
]

# 设置窗口的图标
window = sg.Window('My Window', layout, icon=icon_path)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()