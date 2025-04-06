# 32_使用run_venv.bat來執行cmd

通常需要開啟命令視窗，移動到專案，啟動虛擬環境，輸入後續命令

使用 run_venv.bat 來取代上述

```bat
@echo off
REM 執行虛擬環境 cmd視窗
REM start cmd → 開啟一個新的命令列視窗
REM /k → 表示執行完指令後「保留視窗開啟」

start cmd /k "cd /d C:\Users\USER\Documents\test_venv && venv\Scripts\activate.bat"

```