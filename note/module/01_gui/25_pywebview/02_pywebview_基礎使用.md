# pywebview_基礎使用

```py
import webview

class Api:
    """用來給前端 JS 呼叫的 Python 類別"""
    def say_hello(self, name):
        return f"Hello from Python, {name}!"

if __name__ == '__main__':
    # 1. 建立 API 實例
    api = Api()

    # 2. 建立視窗（可以載入遠端網址，也可以載入本地 SvelteKit 開發伺服器）
    window = webview.create_window(
        title='我的現代桌面應用',
        url='http://localhost:5173', # 或是打包後的本地 index.html 路徑
        width=1200,
        height=800,
        js_api=api # 將 Python API 注入前端
    )

    # 3. 啟動 GUI 迴圈
    webview.start(debug=True) # debug=True 可以直接在視窗內按 F12 打開開發者工具
```

## create_window() 的核心選項參數
參數名稱    類型  預設值 說明
title   str 'pywebview'        視窗標題列的文字。
url     str 'https://pywebview.flowrl.com/'    要載入的網址，可以是遠端 URL (http://...) 或本地 HTML 檔案路徑。
width   int   800 視窗初始寬度（像素）。
height  int   600 視窗初始高度（像素）。
resizable   bool    True    視窗是否允許使用者調整大小。
frameless   bool    False   無邊框模式。設為 True會拔掉作業系統原生的標題列與縮放按鈕，讓你能在網頁前端自己刻一個精美的高質感自訂標題列。
min_size    tuple   (200, 100)  視窗允許被縮小的最小寬高限制（例如 (800, 600)）。
background_color    str '#FFFFFF'   網頁載入前的背景顏色（防止在載入網頁時閃爍白屏）。
js_api  object  None    前後端溝通的靈魂。傳入一個 Python 類別實例，前端網頁就能透過 window.pywebview.api 呼叫該類別裡的所有方法。


## webview.start() 的重要參數

debug=True：
開啟開發者模式。在 Windows (WebView2) 上，這會允許你直接在網頁畫面中按滑鼠右鍵點擊 "Inspect"（檢查），打開熟悉的 Chrome DevTools 來進行前端 JS/CSS 除錯，這在開發階段極為重要。

gui：
通常讓 pywebview 自動偵測即可（Windows 自動用 webview2，Mac 用 cocoa）。但你也可以手動強制指定（例如 gui='edgechromium'）。

