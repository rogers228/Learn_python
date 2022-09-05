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
    
    # root.resizable(False, False) # 禁止 調整大小resize
    root.minsize(200, 50)  # 最小視窗
    # root.maxsize(min_height, max_height) # 最大視窗

    # root.attributes('-alpha',0.5) # 半透明
    root.attributes('-topmost', 1) #最上層顯示
    
    # 移動圖層
    # root.lift(another_window)
    # root.lower(another_window)

    root.iconbitmap('./Form.ico') # 變更圖示
    root.mainloop()

if __name__ == '__main__':
    test1()