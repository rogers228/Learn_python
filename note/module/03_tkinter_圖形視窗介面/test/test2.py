#https://www.pythontutorial.net/tkinter/tkinter-window/
from tkinter import *
from tkinter import ttk

def test1():
    root = Tk()
    root.title('Tkinter Window Demo')

    # Changing window size and location
    # root.geometry('600x400+100+50') # width height left top # 視窗大小

    # 視窗居中
    window_width = 600
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    mycanvas = Canvas(root, width=window_width, height=window_height)
    mycanvas.place(x=0, y=0)
    mycanvas.create_line(20, 20, 280, 20)
    mycanvas.create_rectangle(210, 10, 290, 100, fill='red')
    mycanvas.create_oval(250, 150, 300, 300, fill='red') # 圓形

    root.resizable(False, False) # 禁止 調整大小resize
    root.mainloop()

if __name__ == '__main__':
    test1()