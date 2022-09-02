import tkinter as tk    
from tkinter import ttk

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
    
w = tk.Tk() #建立視窗
w.title('test windows')    
center_window(w, 600, 400)    
#w.maxsize(600, 400) #最大size   
w.minsize(600, 400) #最小size
universal_height =300

nb = ttk.Notebook(w)
page1 = ttk.Frame(nb, width= 500,height = universal_height)
page2 = ttk.Frame(nb,width = 500,height = universal_height)
nb.add(page1, text='公司設定')
nb.add(page2, text='人員設定')
nb.place(x=10, y=10)

'''
day_label = tk.Label(page1, text="Day1:")
day_label.pack()
day_label.place(x=10, y=10)


'''
lb1 = tk.Label(page1, text='this is test:') #建立標籤
lb1.place(x=10, y=10) #設定絕對座標

text1 = tk.Entry(page1, width = 30) #建立文字框
text1.place(x=80, y=10) #設定絕對座標

btn1 = tk.Button(page1, text = 'do', width = 10, command=hello) #建立按鈕
btn1.place(x=60, y=120)

btn2 = tk.Button(page1, text = 'cancel', width = 10, command=quit) #建立按鈕
btn2.place(x=160, y=120)

tk.mainloop()
