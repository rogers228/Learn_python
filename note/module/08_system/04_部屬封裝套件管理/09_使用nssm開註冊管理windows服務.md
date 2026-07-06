# NSSM
NSSM（全稱 Non-Sucking Service Manager，直譯為「不爛的服務管理器」）是一個在 Windows 系統中非常知名且受歡迎的開源免費工具。

nssm install <服務名>  安裝新服務   會彈出 UI 介面供你設定程式路徑、日誌等。
nssm remove <服務名>   移除服務    徹底將該服務從 Windows 系統中刪除。
nssm edit <服務名> 修改服務    彈出 UI 介面，讓你修改現有服務的參數或路徑。
nssm start <服務名>    啟動服務    直接從命令列啟動服務。
nssm stop <服務名> 停止服務    直接從命令列停止服務。
nssm status <服務名>   查詢狀態    查看該服務目前是 Running 還是 Stopped。
nssm restart <服務名>         重新啟動

# 下載
1. https://nssm.cc/download
2. 尋找 Featured pre-release 版本 下載下來會是一個 .zip 壓縮檔，將其解壓縮

# 安裝
1. 建立資料夾 C:\nssm，找到解壓縮的資料夾win64裡面的nssm.exe 複製到此
2. 建立環境變數 Path 添加 C:\nssm
3. 開啟cmd 輸入nssm 驗證是否成功


# 建立服務

## Application 頁籤
1. 開啟 cmd 輸入 nssm install pnss2 將開啟 gui Application 頁籤，pnss2是服務名稱 自己改
2. Path是執行程式完整路徑: C:\Python37\python.exe
3. Startup directory是執行路徑：C:\Users\user\Documents\Rogers\ys_pnss2\39_flask
4. Arguments: 輸入你的啟動檔名 wsgi_server.py


## Details 頁籤
1. Display name: pnss2 Note大象記事服務
2. Description: 填寫一些描述
3. Startup type: 建議下拉選 Automatic (Delayed Start)（自動延遲啟動），這能確保開機時網路等元件都準備好後才啟動 Flask。

## I/O 頁籤（【重要】取代 CMD 視窗看 Log 的關鍵）
1. Output (stdout): 點 ... 選擇或輸入你想把平常 CMD 輸出紀錄在哪裡（例如：C:\你的專案資料夾\stdout.log）。
2. Error (stderr): 填寫與上面相同的路徑，這樣報錯與正常訊息就會寫在同一個檔案裡。

## 啟動
1. 以系統管理員開啟 cmd 輸入 nssm start pnss2

## 在 Windows 「服務」管理員中查看它
1. 按下 Win + R，輸入 services.msc 並按 Enter。