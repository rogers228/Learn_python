# Python與JS結合：使用 pywebview 打造現代桌面應用

## 1. 什麼是 pywebview？
`pywebview` 是一個輕量級的 Python 套件，允許開發者使用網頁技術（HTML, CSS, JavaScript）來建構桌面應用程式的圖形介面（GUI）。它不需要龐大的瀏覽器核心（如 Electron），而是直接呼叫作業系統原生內建的 WebView 引擎（如 Windows 上的 WebView2、macOS 上的 WebKit）。

## 2. 主要功能與解決的問題
* **極小體積與高效能**：省去打包專屬瀏覽器的肥大體積，記憶體佔用極低。
* **擺脫傳統 GUI 框架的束縛**：告別樣式難寫、介面過時的傳統工具（如 PyQt、Tkinter），讓開發者能直接使用現代前端技術（如 SvelteKit、Tailwind CSS）。
* **Python 與 JS 雙向通訊**：原生支援 JS API 綁定，讓網頁前端能夠順暢地呼叫本地的 Python 函數。

## 3. 經典架構：遠端 Web Server + 本地能力 CLI 呼叫
這是一種結合雲端與地端優勢的混合式架構：
* **前端與業務邏輯**：部署在遠端主機（例如 SvelteKit 遠端 Server），免去客戶端頻繁更新的困擾。
* **本地系統能力**：透過 `pywebview` 作為輕量外殼，當網頁需要操作本機檔案、調用 CLI 或執行 Python 腳本時，直接透過雙向通訊呼叫本地端資源（例如直接開啟 NAS 上的 Excel 檔案）。

## 4. 簡短範例
以下是一個簡單的 `pywebview` 結合本地 API 的程式碼範例：

```python
import webview
import subprocess

class NativeAPI:
    def run_local_script(self):
        # 執行本地端指令或 Python 腳本
        result = subprocess.run(["python", "--version"], capture_output=True, text=True)
        return {"output": result.stdout}

if __name__ == '__main__':
    api = NativeAPI()
    # 建立視窗並指向遠端網址，同時注入本地 API
    window = webview.create_window(
        'Cloud Hybrid App', 
        'https://your-remote-server.com', 
        js_api=api,
        width=1024, 
        height=768
    )
    webview.start()
```

前端網頁即可透過 `window.pywebview.api.run_local_script()` 輕鬆喚醒本地端能力！