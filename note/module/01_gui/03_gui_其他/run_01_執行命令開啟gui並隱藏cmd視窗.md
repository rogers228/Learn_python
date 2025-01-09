# 執行命令開啟gui並隱藏cmd視窗

在windows底下，執行命令開啟gui並隱藏cmd視窗，
在windows底下，使用vbs不需安裝無其他依賴

## 準備好python 及腳本

## 建立run.vbs

```cmd
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run """C:\python_venv\python.exe"" ""\\220.168.100.104\pdm\python_program\mini_script\show_computer_name.py""", 0, False
```

## 說明

```py
# Set WshShell = CreateObject("WScript.Shell")
# WshShell.Run "命令", 0, False
#                                 命令前後須以雙引號包裹
#                      0          代表隱藏cmd視窗
#                         False   不等待命令執行完成，立即繼續（非同步，預設值）
# ""C:\python_venv\python.exe""   
#                                 命令的內部是路徑 故需使用雙引號避免路徑中的空白
#                                 命令的內部 若有雙引號 須使永2個雙引號進行轉一
#
# """C:\python_venv\python.exe"" ""\\220.168.100.104\pdm\python_program\mini_script\show_computer_name.py"""
#                                 結合後如上
```
