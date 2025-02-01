# 經典_建立免安裝的python環境_含pip
參考網址https://www.readfog.com/a/1636357495152807936

# 1.下載Python Releases for Windows

使用https://www.python.org/downloads/windows/
下載 python-3.11.9-embed-amd64
embed 代表可鑲入版本 不必正式安裝，
amd64 代表執行環境是windows64位元，
可以選擇所需要的版本，下載後是一個壓縮檔，解壓縮到一個資料夾就建立了一個免安裝的環境資料夾。

## 檢查python是否成功  
    
CMD到該資料夾，輸入以下回得到python版本，代表建立環境成功可以運行。
```cmd
    cd /d C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64
    python --version
```

# 2.為您的python環境建立pip  

使用以下連結可下載get-pip.py  
將get-pip.py移動放在 python-3.10.6-embed-amd64 資料夾  
最後安裝完成後可移除減少檔案大小  

https://bootstrap.pypa.io/get-pip.py

CMD到該資料夾，輸入以下可安裝pip  

```cmd
.\python get-pip.py  --no-warn-script-location
.\python get-pip.py --force-reinstall
```
.\是本資料夾環境的python, 非全域的python

## 檢查是否安裝pip成功
```cmd
.\python -m pip --version
```
python.exe: No module named pip
python解釋器 回應沒有 pip 模組，代表找不到 pip
是路徑的問題

## 使用python解釋器 檢查路徑
```
python 開啟python解釋器
import sys
for path in sys.path:
    print(path) 前方要按tab

    enter
```
輸出以下 2個路徑
```
C:\Users\USER\Documents\py_env\py312\python312.zip
C:\Users\USER\Documents\py_env\py312
```

## 修改python環境路徑

修改環境路徑，使用編輯器開啟 python312._ pth
修改如下，1.加入上層的相對路徑符號 2.取消註解import site 使其有作用  
加入上層路徑可以將專案資料夾放在其上層，避免汙染環境  
import site 會將 Lib\site-packages 自動添加到 sys.path 使其可抓取環境的套件

```python312._pth
python310.zip
.
..
# Uncomment to run site.main() automatically
import site
```

## 重啟cmd, 再次使用python解釋器 檢查路徑，可以得到以下，已增加了環境路徑  
輸出以下 4個路徑
```
C:\Users\USER\Documents\py_env\py312\python312.zip
C:\Users\USER\Documents\py_env\py312
C:\Users\USER\Documents\py_env
C:\Users\USER\Documents\py_env\py312\Lib\site-packages
```
ctrl + z 離開python解釋器

## 再次檢查是否安裝pip成功
```cmd
.\python -m pip --version
```
輸出以下代表成功安裝
```
pip 25.0 from C:\Users\USER\Documents\py_env\py312\Lib\site-packages\pip (python 3.12)
```

#  3.將該資料夾壓縮為.7z

移除 get-pip.py 
將資料夾壓縮後約11M，為已經有包含PIP的Poython環境，可作為專案初始開發環境  
該專案所需要的套件直接安裝在該環境  
專案資料夾放在上層，或其他位置，使用者不須安裝Python即可執行
