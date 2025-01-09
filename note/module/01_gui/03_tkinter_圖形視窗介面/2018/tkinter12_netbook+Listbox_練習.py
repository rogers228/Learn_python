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

def get_list(event):
    index = listbox1.curselection()[0]
    seltext = listbox1.get(index)
    print(seltext)
    
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
#nb.place(x=10, y=10)
nb.grid(row=0, column=0, padx= 5, pady= 5)


listbox1 = tk.Listbox(page1, width=30, height=8)
for item in ['one', 'two', 'three', 'four','one', 'two', 'three', 'four','one', 'two', 'three', 'four']:
    listbox1.insert(tk.END, item)
listbox1.grid(row=0, column=0, padx= 0, pady= 5)
yscroll = tk.Scrollbar(page1, command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox1.config(yscrollcommand = yscroll.set)
listbox1.bind('<ButtonRelease-1>', get_list) #綁定事件



lb1 = tk.Label(page1, text='this is test:    ') #建立標籤
#lb1.place(x=10, y=10) #設定絕對座標
lb1.grid(row=0, column=2, sticky = tk.NW)


text1 = tk.Entry(page1, width = 30) #建立文字框
#text1.place(x=80, y=10) #設定絕對座標
text1.grid(row=0, column=3, sticky = tk.NW)

'''
btn1 = tk.Button(page1, text = 'do', width = 10, command=hello) #建立按鈕
btn1.place(x=60, y=120)

btn2 = tk.Button(page1, text = 'cancel', width = 10, command=quit) #建立按鈕
btn2.place(x=160, y=120)
'''
tk.mainloop()
