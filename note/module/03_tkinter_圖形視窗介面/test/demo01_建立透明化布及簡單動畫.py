# from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
import win32gui
import win32con
import win32api

class TEST_G():
    def __init__(self):
        self.dic = {
            'element_count': 0,
            'elenent_name': [],
        }        
        self.lis_x = [0,20,40,60,90,125,160,200,240,290,350]
        self.y = 200
        self.load()
        self.root.mainloop()

    def load(self):
        self.root = tk.Tk(); w = self.root
        w.title('Tkinter Window Demo')
        window_width = 600
        window_height = 400
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        w.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        w.resizable(False, False) # 禁止 調整大小resize
        self.create_line()
        self.create_canvas()

        # 重複顯示動畫
        i = 0
        while True:
            self.show_element(i)
            self.root.update()
            time.sleep(0.1)
            i += 1
            if i > len(self.lis_x)-1: i = 0


    def create_line(self):
        canvas = tk.Canvas(self.root, width=600, height=400, bd=0, bg='#ff00ff')
        # canvas transparent
        hwnd = canvas.winfo_id()
        colorkey = win32api.RGB(255,0,255) #full black in COLORREF structure
        wnd_exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        new_exstyle = wnd_exstyle | win32con.WS_EX_LAYERED
        win32gui.SetWindowLong(hwnd,win32con.GWL_EXSTYLE,new_exstyle)
        win32gui.SetLayeredWindowAttributes(hwnd,colorkey,255,win32con.LWA_COLORKEY)

        canvas.create_line(0, 200, 600, 200, dash=(4, 4))
        canvas.place(x=0, y=0)

    def create_canvas(self):
        self.canvas_1 = tk.Canvas(self.root, width = 600, height = 400, bd=0, bg='#ff00ff')
        hwnd = self.canvas_1.winfo_id()
        colorkey = win32api.RGB(255,0,255) #full black in COLORREF structure
        wnd_exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        new_exstyle = wnd_exstyle | win32con.WS_EX_LAYERED
        win32gui.SetWindowLong(hwnd,win32con.GWL_EXSTYLE,new_exstyle)
        win32gui.SetLayeredWindowAttributes(hwnd,colorkey,255,win32con.LWA_COLORKEY)

        # self.canvas_1.create_rectangle(245,50,345,150, fill='red')
        radius = 10; r=radius
        lis_x = self.lis_x        
        self.canvas_1.place(x=0, y=0)

    def show_element(self, index):
        radius = 10; r=radius
        lis_x = self.lis_x
        self.canvas_1.delete("all") # clear
        self.canvas_1.create_oval(0+lis_x[index],200-r,2*r+lis_x[index],2*r+200-r)



def test1():
    TEST_G()
    # print('test1')

if __name__ == '__main__':
    test1()