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
    
class form(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.setapp() #設定
        self.createControls() #建立控制項
        self.mainloop()
        
    def setapp(self):
        self.master.title('salary 2020') #設置標題
        # self.master.iconbitmap(r'D:\06Python\test\91_icon_圖示\20180303\if_quora_1632524.ico') #改變圖示
        self.master.resizable(0,0) #停用最大化
        self.master.minsize(600, 400) #設定最小size
        center_window(self.master, 600, 400) #視窗置中

    def createControls(self):
        self.icon1_Path = r'D:\06Python\test\91_icon_圖示\20180303\25.bmp'
        self.icon1 = Image.open(self.icon1_Path) #讀取圖片
        self.icon1 = ImageTk.PhotoImage(self.icon1) #將圖片轉換為tk專用圖片

        self.icon2_Path = r'D:\06Python\test\91_icon_圖示\20180303\26.bmp'
        self.icon2 = Image.open(self.icon2_Path) #讀取圖片
        self.icon2 = ImageTk.PhotoImage(self.icon2) #將圖片轉換為tk專用圖片

        self.icon3_Path = r'D:\06Python\test\91_icon_圖示\20180303\27.bmp'
        self.icon3 = Image.open(self.icon3_Path) #讀取圖片
        self.icon3 = ImageTk.PhotoImage(self.icon3) #將圖片轉換為tk專用圖片
        
        tree = ttk.Treeview(self.master)
        tree.insert('', 0, 'app', text='YEOSHE HR人事薪資系統', open = True)
        tree.insert('app', 'end', 'dir1', text='基本設定', open = True, image = self.icon1)
        tree.insert('dir1', 'end', 'system', text='系統設定', image = self.icon2)
        tree.insert('dir1', 'end', 'compaany', text='公司設定', image = self.icon2)
        tree.insert('dir1', 'end', 'person', text='人員設定', image = self.icon2)
        tree.insert('app', 'end', 'dir2', text='薪資計算', open = True, image = self.icon1)
        tree.insert('app', 'end', 'dir3', text='查詢', open = True)
        tree.insert('dir3', 'end', 'work', text='目前出勤狀況', image = self.icon3)
        tree.insert('app', 'end', 'dir4', text='各式報表', open = True)
        tree.insert('dir4', 'end', 'xls_1', text='薪資單', image = self.icon3)
        tree.insert('dir4', 'end', 'xls_2', text='匯款明細表', image = self.icon3)
        tree.insert('dir4', 'end', 'xls_3', text='薪資統計表', image = self.icon3)
        tree.place(x=10, y=10 ,h=350) #設定絕對座標

if __name__=='__main__':
    app = form()
    app.mainloop()
