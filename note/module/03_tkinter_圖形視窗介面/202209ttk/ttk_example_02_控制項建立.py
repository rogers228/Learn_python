import tkinter as tk
from tkinter import ttk

def test1():
    root = tk.Tk()

    tk.Label(root, text='Classic Label').pack() # pack() 放置
    ttk.Label(root, text='Themed Label').pack()
    root.mainloop()
    # 建議統一使用ttk控制項

def test2():
    # 有三種方法可以設置控制項
    # 1. 件歷時在函數直接設定關鍵屬性
    # 2  key value 字典  中括號
    # 3  config()方法

    # 使用字典 逐步建立物件 最後放置到視窗
    # 雖然冗長 但非常好理解 而解讀立好偵錯
    root = tk.Tk()

    label1 = ttk.Label()
    label1['text'] = 'test1'
    label1.pack()

    root.mainloop()

if __name__ == '__main__':
    test2()