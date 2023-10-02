import PySimpleGUI as sg

def main():
    sg.theme('SystemDefault')  # 使用SystemDefault主题

    # 初始的国家和城市数据
    country_data = ['USA', 'Canada', 'UK', 'Australia']
    city_data = {
        'USA': ['New York', 'Los Angeles', 'Chicago'],
        'Canada': ['Toronto', 'Vancouver', 'Montreal'],
        'UK': ['London', 'Manchester', 'Birmingham'],
        'Australia': ['Sydney', 'Melbourne', 'Brisbane']
    }

    layout = [
        [
            sg.Listbox(values=country_data, size=(20, 12), key='-LISTBOX1-', enable_events=True),
            sg.Listbox(values=[], size=(20, 12), key='-LISTBOX2-', enable_events=True, select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED),
            sg.Button('Open')
        ],
    ]

    window = sg.Window('Country and City Selection', layout, size=(400, 225), finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-LISTBOX1-':
            selected_country = values['-LISTBOX1-'][0]
            if selected_country in city_data:
                window['-LISTBOX2-'].update(values=city_data[selected_country])
            else:
                window['-LISTBOX2-'].update(values=[])
        elif event == 'Open':  # 当点击"Show"按钮时
            if len(values['-LISTBOX1-']) > 0:
                selected_country = values['-LISTBOX1-'][0]
                selected_cities = values['-LISTBOX2-']
                sg.popup(f'Selected country: {selected_country}\nSelected cities: {", ".join(selected_cities)}')  # 显示所选国家和城市的消息框

    window.close()

if __name__ == '__main__':
    main()
