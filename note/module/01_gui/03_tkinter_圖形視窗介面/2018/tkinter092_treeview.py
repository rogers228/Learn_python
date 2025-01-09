import tkinter as tk    
from tkinter import ttk 
from PIL import Image, ImageTk

def get_screen_size(window):    
    return window.winfo_screenwidth(),window.winfo_screenheight()    
    
def get_window_size(window):    
    return window.winfo_reqwidth(),window.winfo_reqheight()    
    
def center_window(root, width, height):    
    screenwidth = root.winfo_screenwidth()    
    screenheight = root.winfo_screenheight()    
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)    
    #print(size)    
    root.geometry(size)
    
def hello():
    print("do it")
    
def quit():                           
    print("by by") 

def mycallback(event):
    print(event)
    _iid = tree.identify_row(event.y)
    print(_iid)
    ss = tree.item(_iid, 'text') #取得該項目的打開值
    print(ss)
    
w = tk.Tk() #建立視窗
w.title('test windows') #設置標題
w.iconbitmap('Form.ico') #改變圖示
#w.resizable(0,0) #停用最大化按鈕
#w.attributes("-toolwindow", 1) #設為工具視窗

center_window(w, 300, 240) #視窗置中
#w.maxsize(600, 400) #最大size   
w.minsize(600, 400) #最小size


tree = ttk.Treeview(w)

icon1_Path = 'Form.ico'
icon1 = Image.open(icon1_Path) #讀取圖片
icon1 = ImageTk.PhotoImage(icon1) #將圖片轉換為tk專用圖片

tree.insert('', 'end', 'widgets', text='Widget Tour')
tree.insert('', 0, 'gallery', text='Applications', image = icon1)
id = tree.insert('', 'end', text='Tutorial')
tree.insert('widgets', 'end', text='Canvas')
tree.insert(id, 'end', text='Tree')

tree.item('widgets', open = True) #該項目打開
isopen = tree.item('widgets', 'open') #取得該項目的打開值

tree.insert('', 'end', text='button', tags=('ttk', 'simple')) #含有tags的項目以供
#tree.tag_configure('ttk', background='yellow') #含有'ttk' tag的都改變顏色
tree.tag_bind('ttk', '<Button-1>', mycallback) 


tree.place(x=10, y=10) #設定絕對座標
w.mainloop()
