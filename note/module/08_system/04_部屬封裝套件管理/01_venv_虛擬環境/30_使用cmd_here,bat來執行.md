使用 sublime text 套件 SideBarEnhancements
他有右鍵功能表 run 功能
我建立了一個 cmd_here.bat
右鍵run，即執行cmd here

```
@echo off
REM start cmd 開啟一個新的命令列視窗 /k 保留視窗開啟
rem %~dp0 代表目前這個 .bat 檔所在的資料夾
start cmd /k "cd /d %~dp0"
```