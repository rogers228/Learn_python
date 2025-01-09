import tkinter as tk
import win32gui
import win32con
import win32api
        

def test1():
    root = tk.Tk()
    root.configure(bg='yellow')
    canvas = tk.Canvas(root,bg='#000000')#full black
    hwnd = canvas.winfo_id()
    colorkey = win32api.RGB(0,0,0) #full black in COLORREF structure
    wnd_exstyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    new_exstyle = wnd_exstyle | win32con.WS_EX_LAYERED
    win32gui.SetWindowLong(hwnd,win32con.GWL_EXSTYLE,new_exstyle)
    win32gui.SetLayeredWindowAttributes(hwnd,colorkey,255,win32con.LWA_COLORKEY)
    canvas.create_rectangle(50,50,100,100,fill='blue')
    # canvas.pack()
    canvas.place(x=0, y=0)

    root.mainloop()

if __name__ == '__main__':
    test1()