import PySimpleGUI as sg
sg.theme('SystemDefault')

def test4():
    layout =  [ [sg.Checkbox('My first Checkbox!', default=True)],
                [sg.Text('This is what a Text Element looks like')]]
    window = sg.Window('Socket server', layout, finalize=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('event', event)
        print('values', values)
        print('You entered ', values[0])    

def test3():

    items = ['USA', 'Mexico', 'Japan', 'Korea', 'UK', 'China', 'France']
    asia_index = (2 ,3, 5)
    layout = [
        [sg.Listbox(items, size=(10, 7), key='-LISTBOX-')],
    ]
    window = sg.Window('Title', layout, finalize=True)
    listbox = window['-LISTBOX-'].Widget

    for index in asia_index:
        listbox.itemconfigure(index, bg='green', fg='white')    # set options for item in listbox
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        print(event, values)

    window.close()
def test2():
    sg.popup_yes_no('popup_yes_no\nfdfsfsdfd\ndsfsfddf')  # Shows Yes and No buttons

def test1():
    sg.theme('SystemDefault')
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('ok'), sg.Button('Cancel')] ]
    w = sg.Window('Window Title', layout, 
                    size=(500, 100),
                    resizable=True)
    while True:
        event, values = w.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('event', event)
        print('values', values)
        print('You entered ', values[0])

if __name__ == '__main__':
    test2()
    print('ok')