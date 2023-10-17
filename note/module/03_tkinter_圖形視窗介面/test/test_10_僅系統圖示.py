import tkinter as tk
from tkinter import messagebox

# 定義點擊事件
def on_tray_icon_click(event):
    messagebox.showinfo("點擊事件", "你點擊了系統托盤圖示")

# 創建視窗
root = tk.Tk()
root.withdraw()  # 隱藏視窗

# 創建系統托盤圖示
tray_icon = tk.Tk()
# tray_icon.withdraw()  # 隱藏托盤視窗
# tray_icon.iconbitmap(r'C:\Users\user\Documents\GitHub\Learn_python\note\module\03_pyqt\python_icon.ico')  # 將 "path_to_icon.ico" 替換為你自己的圖示路徑

# 創建功能表
menu = tk.Menu(tray_icon, tearoff=0)
menu.add_command(label="Open", command=lambda: print('Open'))
menu.add_command(label="Save", command=lambda: print('Save'))
menu.add_command(label="Exit", command=tray_icon.quit)

# 將功能表綁定到系統托盤圖示
tray_icon.config(menu=menu)
tray_icon.bind("<Button-1>", on_tray_icon_click)

# 進入主事件迴圈
tray_icon.mainloop()
