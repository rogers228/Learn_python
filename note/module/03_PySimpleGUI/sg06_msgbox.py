import PySimpleGUI as sg

def test1():
    sg.theme('SystemDefault')
    sg.popup_error('popup_error')  # Shows red error button

if __name__ == '__main__':
    test1()