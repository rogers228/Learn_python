import tkinter as tk
from tkinter import filedialog

  
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
    myFormat=[('Excel 97-2003','*.xls')]
    w.fileName = filedialog.asksaveasfilename(title='匯出Excel',filetypes=myFormat)
    if len(w.fileName) > 0:
        print(w.fileName)
    
def quit():                           
    print("by by") 

#字體
#font1 = tkFont.Font(family='新細明體',size=12)

w = tk.Tk() #建立視窗
#w.filename =  filedialog.askopenfilename(initialdir = "/",title = "Selectfile",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#print (root.filename)
w.title('test windows') #設置標題
w.iconbitmap('Form.ico') #改變圖示
w.resizable(0,0) #停用最大化按鈕
#w.attributes("-toolwindow", 1) #設為工具視窗

center_window(w, 300, 240) #視窗置中
#w.maxsize(600, 400) #最大size   
w.minsize(300, 240) #最小size

lb1 = tk.Label(w, text='this is test:', font= ('新細明體',12)) #建立標籤
lb1.place(x=10, y=10) #設定絕對座標

text1 = tk.Entry(w, width = 30) #建立文字框
text1.place(x=80, y=10) #設定絕對座標

btn1 = tk.Button(w, text = 'do', width = 12, font= ('新細明體',12), command=hello)
btn1.place(x=60, y=120)

btn2 = tk.Button(w, text = 'cancel', width = 12, font= ('新細明體',12), command=quit)
btn2.place(x=160, y=120)


    
w.mainloop()

    


