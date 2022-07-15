import tkinter as tk
win = tk.Tk() #建立視窗
win.title('my first window') #設定視窗標題
#win.resizable(0,0) #設定視窗不可調整大小

lb1=tk.Label(win, text='this is test:') #建立標籤
lb1.pack() #放置標籤
lb2=tk.Label(win, text='gui test:') #建立標籤
lb2.pack() #放置標籤
btn1 = tk.Button(win, text='ok')
btn1.pack()
win.mainloop #執行視窗
