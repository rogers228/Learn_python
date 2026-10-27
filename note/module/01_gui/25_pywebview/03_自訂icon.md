## 方法一：透過 AHK 建立桌面捷徑時指定 Icon（最推薦）

你的 AHK 部署腳本在工作站建立桌面捷徑或啟動捷徑時，可以直接幫 .ico 圖標綁定上去：

```
; AHK 建立捷徑語法範例
FileCreateShortcut, "C:\python_venv_312\python.exe", "C:\Users\Desktop\我的桌面應用.lnk", "C:\YourApp", "main.py", "應用程式說明", "C:\YourApp\assets\logo.ico"
```
只要使用者是透過這個捷徑開啟應用程式，Windows 工作列與視窗就會完美顯示你的專屬 Logo！

### 1. 這行指令同時幫你完成了五件事：

指定主程式：告訴 Windows 這個捷徑要執行的本體是 python.exe。

傳遞執行參數：把 "main.py" 當作參數傳給 Python，所以點擊捷徑就等於在命令列輸入 python.exe main.py。

設定工作目錄 (Working Directory)：把執行環境鎖定在 C:\YourApp，確保你的 Python 程式去讀取 assets/ 或資料庫等相對路徑時絕對不會翻車。

指定圖標 (.ico)：這就是最關鍵的一步。 最後一個參數指定了你的專屬圖標 logo.ico 的路徑。

產生捷徑檔案：在指定的桌面或資料夾產生一個 .lnk 捷徑檔案。

### 2. 為什麼這樣就能解決 Icon 的問題？
在 Windows 系統中，如果直接雙擊執行一個解壓縮出來的 python.exe，Windows 預設會顯示 Python 官方的紅藍蛇圖標，因為作業系統不知道這個腳本在幹嘛。

但透過 AHK 幫它捏造一個專屬的桌面捷徑（.lnk）之後：

當使用者透過這個捷徑啟動應用程式時，Windows 工作列（Taskbar）會自動去讀取該捷徑身上綁定的 .ico 圖標。

於是，你的 pywebview 桌面視窗左上角以及下方工作列的圖標，就會瞬間變成你精心設計的專屬 Logo。

### 3. 這個方法的好處
零打包負擔：你完全不需要使用 PyInstaller 或 cx_Freeze 去把幾十MB的 Python 環境和依賴包編成一個巨大的 .exe。

隨時替換：如果你哪天想換 Logo，只需要把 NAS 上的 logo.ico 換掉，或者讓 AHK 重新覆蓋捷徑，圖標就更新了，極其輕量與靈活！



## 方法二：在 Python 端直接呼叫 Windows API 更改（即時生效）
如果你希望不透過捷徑，直接在 Python 程式碼啟動時強制改變當前視窗與工作列的圖標，可以利用 Windows 的 ctypes 讀取 .ico 檔案：


```py
import ctypes
import webview

def set_window_icon(window):
    # 僅限 Windows 平台透過 Win32 API 設定圖標
    if webview.platforms['windows']:
        hwnd = window.native.handle # 取得視窗原生 Handle
        # 載入本地的 .ico 檔案
        hicon = ctypes.windll.user32.LoadImageW(
            0, "assets/logo.ico", 1, 0, 0, 0x00000010 | 0x00000040
        )
        ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 0, hicon) # 設定小圖標
        ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 1, hicon) # 設定大圖標

if __name__ == '__main__':
    window = webview.create_window('我的桌面應用', 'http://localhost:5173')
    
    # 當視窗載入完成後觸發設定圖標
    window.events.loaded += lambda: set_window_icon(window)
    
    webview.start()
```