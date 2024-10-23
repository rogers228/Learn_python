def msgbox(message='', title='Msgbox'):
    import PySimpleGUI as sg
    sg.theme('SystemDefault')
    n_count = message.count('\n')
    layout = [[sg.Text(message)], [sg.Button('ok', size=(10, 1), button_color=('white', 'red'), pad=((98, 0), 2))]]
    w = sg.Window(title, layout, size=(300, 60+(n_count*18)))
    while True:
        event, values = w.read()
        print(event)
        if event == sg.WIN_CLOSED or event == 'ok':
            break

def test1():
    message = 'Some text on Row 1\n1234\n1235\n1235\n1235\n1235'
    msgbox(message, 'title')

if __name__ == '__main__':
    test1()