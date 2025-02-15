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