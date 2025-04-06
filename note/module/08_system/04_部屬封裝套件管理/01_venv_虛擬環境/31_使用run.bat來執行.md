# 04_使用run.bat來執行

原來使用命令視窗，來啟動虛擬環境，

```
venv\Scripts\activate.bat
```

改為使用run.bat來執行，並啟動主程序

```bat
@echo off
REM 啟用虛擬環境並執行 main.py

REM 切到此 bat 檔所在的資料夾，保證執行正確
cd /d "%~dp0"

REM 啟動虛擬環境並執行 Python 程式
call venv\Scripts\activate.bat
python main.py

REM （可選）暫停視窗，以便查看輸出
pause
```