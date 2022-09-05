# https://www.pythontutorial.net/tkinter/tkinter-event-binding/
import tkinter as tk
from tkinter import ttk

'''
    事件名稱  語法為 <modifier-type-detail>
    modifier 修飾符
    type 類型
    detail 細節
    詳細請參閱網址
'''
def return_pressed(event):
    print('Return key pressed.')

def log(event):
    print(event)

def test1():
    # 並非所有控制項 都有 command 屬性
    # 使用事件綁定 更加靈活
    
    root = tk.Tk()
    btn = ttk.Button(root, text='Save')
    btn.bind('<Return>', return_pressed)
    # 使用bind 預設第一個引數為事件名稱 第2個為函數名稱
    # Return 為輸入key enter 事件
    btn.pack() 
    btn.focus() # 獲得焦點  enter才有效
    root.mainloop()

def test2():
    # 使用字典改寫
    root = tk.Tk()
    btn = ttk.Button()
    btn['text']='Save'
    btn.bind('<Return>', return_pressed)
    # 使用bind 預設第一個引數為事件名稱 第2個為函數名稱
    # Return 為輸入key enter 事件
    btn.pack() 
    btn.focus() # 獲得焦點  enter才有效
    root.mainloop()

def test3():
    # 同一個事件 可以綁定多個函數 逐步執行
    root = tk.Tk()
    btn = ttk.Button(root, text='Save')
    btn.bind('<Return>', return_pressed)
    btn.bind('<Return>', log, add='+')
    btn.focus()
    btn.pack(expand=True)

    root.mainloop()

'''
    可以綁定到 主窗體, 控制項
    root.bind('<Return>', handler) # 綁定窗體
    root.bind_class('Entry', '<Control-V>', paste) # 依照類型綁定
    
    也可以取消綁定
    widget.unbind(event)
    btn.unbind('<Return>')

    綁定事件讓gui更加靈活

'''
if __name__ == '__main__':
    test2()