# from tkinter import *
import tkinter as tk
from tkinter import ttk

class TEST_G():
    def __init__(self):
        self.x = 0
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
        self.create_element()
        self.redraw_element() # move!

    def create_line(self):
        mycanvas = tk.Canvas(self.root, width=600, height=400)
        mycanvas.create_line(0, 200, 600, 200, dash=(4, 4))
        mycanvas.place(x=0, y=0)

    def create_element(self):
        radius = 10; r=radius
        self.element = tk.Canvas(self.root, width = 2*r, height = 2*r)
        self.rectangle = self.element.create_oval(0+2,0+2,2*r,2*r)
        self.element.place(x=self.x-r, y=self.y-r)

    def redraw_element(self):
        self.element.delete(self.rectangle) # delete the rectangle 
        # print(self.x, self.y)
        self.x += 1
        self.y += 0
        radius = 10; r=radius
        self.rectangle = self.element.create_oval(0+2, 0+2,2*r,2*r)
        if self.x< 200:
            self.element.place(x=self.x-r, y=self.y-r)
            self.element.after(10, self.redraw_element)
        else:
            return


def test1():
    TEST_G()
    # print('test1')

if __name__ == '__main__':
    test1()