# 隱藏cmd視窗

使用cmd來執行python時，通常會有cmd視窗，
如果用來執行gui時，通常會希望隱藏cmd視窗，
以下有3種方式

## 使用pythonw.exe
原來使用python.exe 改用pythonw.exe 來執行 .pyw
缺點：習慣必須改變


## 使用vbs
在windows通常有vb script
編寫.vbs
```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "C:\python_venv\python.exe \\220.168.100.104\pdm\python_program\rd_start\eel_main.py", 0
Set WshShell = Nothing
```
缺點：vbs通常被視為危險檔案

## 使用autohotkey
編寫.ahk
```ahk
; 使用 Run 指令來運行 Python 腳本
; 使用 Hide 參數來隱藏命令提示符窗口
Run, C:\python_venv\python.exe \\220.168.100.104\pdm\python_program\rd_start\eel_main.py, , Hide
```
缺點：需另外安裝ahk，或直接編譯為exe