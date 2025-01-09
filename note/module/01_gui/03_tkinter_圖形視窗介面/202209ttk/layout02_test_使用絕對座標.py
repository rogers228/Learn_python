# https://www.pythontutorial.net/tkinter/tkinter-ttk/
from tkinter import *
from tkinter import ttk

def test1():
    # 上下 Frame 固定上高度
    root = Tk()
    root.title("Feet to Meters")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    s = ttk.Style()
    s.configure('TFrame')
    s.configure('yellow.TFrame', background='yellow')
    s.configure('red.TFrame', background='red')
    s.configure('cyan.TFrame', background='cyan')

    # grid 跟隨母
    # configure 對子

    layout0 = ttk.Frame(root, padding=4, width=600, height=400, style='yellow.TFrame')
    layout0.place(x=0, y=0)

    layout1_top = ttk.Frame(layout0, padding=4, width=600, height=50, style='red.TFrame')
    layout1_top.place(x=0, y=0)

    layout1_bottom = ttk.Frame(layout0, padding=4, width=600, height=400-50, style='cyan.TFrame')
    layout1_bottom.place(x=0, y=50)

    # label1 = ttk.Label(layout1_top, text="查詢:", font=("Arial", 12))
    # label1.grid(column=0, row=0, sticky=W)
    # # label1.columnconfigure(0, weight=1) 

    # entry1 = ttk.Entry(layout1_top, text="", font=("Arial", 12))
    # entry1.grid(column=0, row=0, sticky=(E ))
    # entry1.columnconfigure(1, weight=1) 
    root.mainloop()

if __name__ == '__main__':
    test1()