import pandas as pd
import PySimpleGUI as sg
# https://www.pysimplegui.org/en/latest/call%20reference/#table-element

def testfunc():
    print('test')

def test1():
    lis = [
            ['Rogers',32,'A'],
            ['Allen',5,'A'],
            ['Jessis',28,'B'],
            ['Jay',18,'O'],
            ]
    col_s = ['Name','Age','Bud']
    df = pd.DataFrame(lis, columns = col_s) # 建立 DataFrame

    # gui
    headers = {'Name':[], 'Arg':[], 'Bud':[]}
    table = df
    sg.theme("SystemDefault")
    # sg.set_options(font=("Courier New", 12))
    sg.set_options(font=("新細明體", 12))

    headings = list(headers)
    data_values = table.values.tolist()
    gridview = sg.Table(values = data_values, headings = headings,
        visible_column_map = None,
        auto_size_columns= False, # 不要自動調整欄寬 
        col_widths=list(map(lambda x:len(x)+3, headings)), # 欄寬
        display_row_numbers = True, # 顯示row號
        num_rows = 25, # 行數
        row_height = 20, # 行高
        alternating_row_color = 'gainsboro', # 交替顏色
        justification = 'left', # 對齊方式 left center right
        enable_events = True, # 啟用事件
        key='_rowselected_', # 事件名稱 (event)
        )

    layout = [[gridview]]

    # popup menu
    menu = sg.Menu(gridview, tearoff=0)
    menu.add_command(label="Copy", command=testfunc)

    window = sg.Window('Sample excel file',  layout)



    while True:
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == '_rowselected_':
            print(values['_rowselected_'][0])

if __name__ == '__main__':
    test1()
