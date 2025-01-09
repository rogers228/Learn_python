import PySimpleGUI as sg
import pandas as pd

# 創建一個 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 35, 22],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Teacher']
}
df = pd.DataFrame(data)

# 將 DataFrame 轉換為 PySimpleGUI 表格數據
data_for_table = df.values.tolist()  # DataFrame 中的數據轉換為列表
print(data_for_table)
header_list = df.columns.tolist()    # DataFrame 的列標題
print(header_list)

# 定義 PySimpleGUI 佈局，使用 Table 元素
layout = [
    [sg.Table(values=data_for_table, headings=header_list,
              auto_size_columns=False,
              display_row_numbers=True,
              justification='center',
              num_rows=min(25, len(data_for_table)))]
]

# 創建窗口
window = sg.Window('DataFrame in PySimpleGUI', layout)

# 事件循環
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()