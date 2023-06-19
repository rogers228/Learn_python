import PySimpleGUI as sg

def test1():
    sg.theme('SystemDefault')
    sg.popup_error('popup_error\nthe second')  # Shows red error button

def test2():
    sg.theme('SystemDefault')
    sg.popup('\nPart number is not exist\nplease confirm whether your product number.\n\n', title='title')

if __name__ == '__main__':
    test1()