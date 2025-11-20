# 預設模組 不需安裝
import tkinter as tk
from tkinter import messagebox

def test1():
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗
    messagebox.showinfo("訊息", "這是一般資訊")
    messagebox.showwarning("警告", "這是警告訊息")
    messagebox.showerror("錯誤", "這是錯誤訊息")
    if messagebox.askyesno("確認", "你確定嗎？"):
        print("使用者選擇 Yes")
    else:
        print("使用者選擇 No")
    root.mainloop()

if __name__ == '__main__':
    test1()
