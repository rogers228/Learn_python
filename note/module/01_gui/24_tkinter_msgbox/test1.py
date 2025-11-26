import tkinter as tk
from tkinter import messagebox

_TK_ROOT = None # 內部全域變數，用於管理 Tkinter root 實例

def get_or_create_tk_root():
    global _TK_ROOT
    if _TK_ROOT is None:
        root = tk.Tk() # 創建 Tkinter 根視窗
        root.withdraw() # 隱藏根視窗，確保只看到彈出的訊息框
        _TK_ROOT = root
    return _TK_ROOT

def msgbox(title, message):
    root = get_or_create_tk_root()
    messagebox.showinfo(title=title, message=message)

if __name__ == '__main__':

    msgbox("環境檢查結果", "專案環境已通過檢查，點擊 OK 啟動程式。")

    # 結束 Tkinter 主迴圈
    # 雖然 messagebox.showinfo 已經處理了，但在某些環境下明確銷毀可以確保資源釋放
    if _TK_ROOT:
        _TK_ROOT.quit()