# 使用 dev c++ 建立啟動程式

## Orwell Dev-C++ 5.11

 Dev-C++ 是C, C++ 的老牌免費IDE

## 下載 安裝
https://www.azofreeware.com/2006/03/dev-c-50-beta-92-4992.html#google_vignette
免安裝版直接解壓縮指定C即可



## 開發時執行 python
在執行python通常使用cmd命令，執行以下
```
python test1.py
```
但是發布gui程式時，不可能由使用者打命令，
應建立一個啟動程式exe



1. 開啟 dev c++ 新增專案 project1.dev
2. main.cpp 內容如下

```c
#include <windows.h>

int main() {
    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi;

    if (CreateProcess(
        NULL,
        (LPSTR)"pythonw C:\\Users\\USER\\Documents\\Learn_python\\note\\module\\01_gui\\03_pyqt\\test1.py", // 指定要執行的命令
        NULL, NULL, FALSE,
        0,
        NULL, NULL, &si, &pi)) {
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    }
    return 0;
}

```

## 說明
python test1.py 命令改為
```
pythonw C:\\Users\\USER\\Documents\\Learn_python\\note\\module\\01_gui\\03_pyqt\\test1.py
```
python 改為 pythow
c++中windows的路徑 \ 為轉義符號 應改為 \\

## 使用 dev c++ 編譯
使用dev c++ IDE 功能表>執行>編譯，最終產出project1.exe

## 使用 cmd 命令 編譯
cd /d C:\Users\USER\Documents\Learn_python\note\module\08_system\04_部屬封裝套件管理\test_open_gui_hide_cmd
C:\DevCppPortable\MinGW64\bin\g++.exe main.cpp -o project1.exe





