from tkinter import *
from tkinter import ttk

def test1():
    # 單一 Frame
    root = Tk()
    root.title("Feet to Meters")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    s = ttk.Style()
    s.configure('TFrame')
    s.configure('Frame1.TFrame', background='red')

    layout0 = ttk.Frame(root, width=600, height=400, style='Frame1.TFrame')
    layout0.grid(column=0, row=0, sticky=(N, W, E, S)) # E東 W西 S南 N北
    root.mainloop()

def test2():
    # 左右 Frame
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

    layout0 = ttk.Frame(root, padding=5, width=600, height=400, style='yellow.TFrame')
    layout0.grid(column=0, row=0, sticky=(N, W, E, S)) # E東 W西 S南 N北
    layout0.columnconfigure(0, weight=1) # layout1_left
    layout0.columnconfigure(1, weight=1) # layout1_right
    layout0.rowconfigure(0, weight=1)
    
    layout1_left = ttk.Frame(layout0, width=300, height=400, style='red.TFrame')
    layout1_left.grid(column=0, row=0, sticky=(N, W, E, S))
    layout1_left.columnconfigure(0, weight=1) 

    layout1_right = ttk.Frame(layout0, width=300, style='cyan.TFrame')
    layout1_right.grid(column=1, row=0, sticky=(N, S, E, W))
    layout1_right.columnconfigure(0, weight=1) 

    root.mainloop()

def test3():
    # 左右 Frame 固定左側寬度
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

    layout0 = ttk.Frame(root, padding=5, width=600, height=400, style='yellow.TFrame')
    layout0.grid(column=0, row=0, sticky=(N, W, E, S)) # E東 W西 S南 N北
    # layout0.columnconfigure(0, weight=1) # layout1_left 不要設定左側
    layout0.columnconfigure(1, weight=1) # layout1_right
    layout0.rowconfigure(0, weight=1)
    
    layout1_left = ttk.Frame(layout0, width=200, height=400, style='red.TFrame')
    layout1_left.grid(column=0, row=0, sticky=(N, W, S))
    layout1_left.columnconfigure(0, weight=1) 

    layout1_right = ttk.Frame(layout0, width=600-200, style='cyan.TFrame')
    layout1_right.grid(column=1, row=0, sticky=(N, S, E, W))
    layout1_right.columnconfigure(0, weight=1) 

    root.mainloop()

def test4():
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

    layout0 = ttk.Frame(root, padding=5, width=600, height=400, style='yellow.TFrame')
    layout0.grid(column=0, row=0, sticky=(N, W, E, S)) # E東 W西 S南 N北
    layout0.columnconfigure(0, weight=1) 
    # layout0.rowconfigure(0, weight=1) # layout1_left 不要設定上部
    layout0.rowconfigure(1, weight=1)
    layout1_top = ttk.Frame(layout0, width=600, height=50, style='red.TFrame')
    layout1_top.grid(column=0, row=0, sticky=(N,E,W))
    layout1_top.columnconfigure(0, weight=1) 

    layout1_bottom = ttk.Frame(layout0, width=600, height=400-50, style='cyan.TFrame')
    layout1_bottom.grid(column=0, row=1, sticky=(N,E,W,S))
    layout1_bottom.columnconfigure(0, weight=1) 

    ttk.Label(layout1_top, text="feet").grid(column=0, row=0, sticky=W)

    root.mainloop()
if __name__ == '__main__':
    test4()