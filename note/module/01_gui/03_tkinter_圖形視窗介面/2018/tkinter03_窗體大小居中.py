import tkinter as tk    
  
def get_screen_size(window):    
    return window.winfo_screenwidth(),window.winfo_screenheight()    
    
def get_window_size(window):    
    return window.winfo_reqwidth(),window.winfo_reqheight()    
    
def center_window(root, width, height):    
    screenwidth = root.winfo_screenwidth()    
    screenheight = root.winfo_screenheight()    
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)    
    print(size)    
    root.geometry(size)    
    
w = tk.Tk() #建立視窗
w.title('test windows')    
center_window(w, 300, 240)    
#w.maxsize(600, 400) #最大size   
w.minsize(300, 240) #最小size
tk.mainloop()
