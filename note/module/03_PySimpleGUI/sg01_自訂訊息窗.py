import PySimpleGUI as sg
def test1():
    sg.theme('SystemDefault')
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Text('')],
                [sg.Button('ok'), sg.Button('Cancel')] ]
    w = sg.Window('Window Title', layout, 
                    size=(500, 120),
                    resizable=True)
    while True:
        event, values = w.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
            
        print('event', event)
        print('values', values)
        print('You entered ', values[0])

if __name__ == '__main__':
    test1()