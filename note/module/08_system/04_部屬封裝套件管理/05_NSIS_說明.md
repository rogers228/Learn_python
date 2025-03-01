# NSIS

以下已經測試成功。
NSIS（Nullsoft Scriptable Install System）是一個免費的 Windows 安裝程式工具，可以製作 .exe

功能如下
1. 自訂解壓縮目錄
2. 建立桌面捷徑
3. 顯示安裝進度
4. 執行解壓縮後的程式

## 下載及安裝

https://www.azotaiwan.com/_dl_rC5CFd3nVq/NSISPortableUnicode_2.4.6.5_azo.exe.htm

## 準備
準備專案資料夾，並將欲部屬的資料夾 test_env，按右鍵 > 壓縮至 > 7zip檔案

## 建立 installer.nsi

```
!define InstallDir "C:\Users\USER\Desktop\work_c\project_env"  ; 指定解壓縮路徑
; 路徑最後應是資料夾，解壓時不存在則會建立

!define SourceFolder "C:\Users\USER\Desktop\Test\project_env"  ; 打包來源


Outfile "MyInstaller.exe"   ; 輸出自解壓縮exe
InstallDir "${InstallDir}"  ; 設定預設解壓縮目錄

RequestExecutionLevel admin ; 需要管理員權限  若安裝於系統目錄
; RequestExecutionLevel user  ; 不要求管理員權限

Section "解壓縮檔案"

    RMDir /r "${InstallDir}"    ; 若存在則先刪除
    SetOutPath "${InstallDir}"  ; 設定解壓縮目標資料夾
    File /r "${SourceFolder}\*"  ; 打包來源資料夾內所有檔案
    MessageBox MB_OK "解壓縮完成！已安裝至 ${InstallDir}" ; 解壓縮完成提示

SectionEnd

```

## 編譯 NSIS 腳本

1. 找到安裝後NISI資料夾，點兩下NSISPortable.exe
2. 點擊 Compile NSI Script
3. 點擊 load Script 開啟，讀取後即執行，並產生MyInstaller.exe

或使用cmd命令
```
cd /d C:\Users\USER\Desktop\Test
"C:\NSISPortableUnicode\NSISPortable.exe" installer.nsi
```

