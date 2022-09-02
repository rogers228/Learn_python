import tkinter as tk    
  
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

def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    index = listbox1.curselection()[0]
    seltext = listbox1.get(index)
    print(seltext)
    
w = tk.Tk() #建立視窗
w.title('test windows') #設置標題
w.iconbitmap('Form.ico') #改變圖示
w.resizable(0,0) #停用最大化按鈕
#w.attributes("-toolwindow", 1) #設為工具視窗

center_window(w, 600, 400) #視窗置中
#w.maxsize(600, 400) #最大size   
w.minsize(600, 400) #最小size



listbox1 = tk.Listbox(w, width=30, height=8)
for item in ['one', 'two', 'three', 'four','one', 'two', 'three', 'four','one', 'two', 'three', 'four']:
    listbox1.insert(tk.END, item)

listbox1.grid(row=0, column=0)
yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox1.config(yscrollcommand = yscroll.set)
listbox1.bind('<ButtonRelease-1>', get_list) #綁定事件





lb1 = tk.Label(w, text='this is test:') #建立標籤
lb1.place(x=200, y=10) #設定絕對座標

text1 = tk.Entry(w, width = 30) #建立文字框
text1.place(x=280, y=10) #設定絕對座標

btn1 = tk.Button(w, text = 'do', width = 10, command=hello)
btn1.place(x=60, y=120)

btn2 = tk.Button(w, text = 'cancel', width = 10, command=quit)
btn2.place(x=160, y=120)

w.mainloop()
