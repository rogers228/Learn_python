import tkinter as tk
from tkinter import ttk

def button_clicked():
    print('Button clicked')
    return

def hello( args):
    print(f'hello! {args}')
    return

def test1():
    # 控制項綁定事件
    # 使用控制項的 command 屬性 實現事件綁定
    # 並非所有控制項 都有 command 屬性
    
    root = tk.Tk()
    button = ttk.Button()
    button['text']='Click Me'
    # button['command']= button_clicked # 直接呼叫
    button['command']= lambda: hello('allen') # 帶引數呼叫
    button.pack()
    root.mainloop()

if __name__ == '__main__':
    test1()