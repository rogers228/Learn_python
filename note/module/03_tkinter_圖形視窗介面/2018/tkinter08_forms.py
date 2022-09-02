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
    
class form(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.setapp() #設定
        self.createControls() #建立控制項
        self.mainloop()
        
    def setapp(self):
        self.master.title('test windows 1') #設置標題
        self.master.iconbitmap('Form.ico') #改變圖示
        self.master.resizable(0,0) #停用最大化
        self.master.minsize(300, 240) #設定最小size
        center_window(self.master, 300, 240) #視窗置中

    def createControls(self):
        lb1 = tk.Label(self.master, text='this is test:') #建立標籤
        lb1.place(x=10, y=10) #設定絕對座標    

        text1 = tk.Entry(self.master, width = 30) #建立文字框
        text1.place(x=80, y=10) #設定絕對座標

        btn1 = tk.Button(self.master, text = 'do', width = 10, command=hello)
        btn1.place(x=60, y=120)
        
        btn2 = tk.Button(self.master, text = 'cancel', width = 10, command=quit)
        btn2.place(x=160, y=120) 

if __name__ == '__main__':
    f = form()
