參考網址https://www.readfog.com/a/1636357495152807936

# 1.下載Python Releases for Windows，使用https://www.python.org/downloads/windows/  

可以選擇所需要的版本，下載是一個壓縮檔，解壓縮到一個資料夾就建立了一個免安裝的環境資料夾  

檢查是否成功  
CMD到該資料夾，輸入以下回得到python版本，代表建立環境成功可以運行。

    cd /d C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64
    python --version

# 2.為您的python環境建立pip  

    使用以下連結可下載get-pip.py  
    將get-pip.py放在 python-3.10.6-embed-amd64 資料夾  
    最後安裝完成後可移除減少檔案大小  

    https://bootstrap.pypa.io/get-pip.py

CMD到該資料夾，輸入以下可安裝pip  
.\是本資料夾環境的python, 非全域的python

    .\python get-pip.py  --no-warn-script-location

CMD到該資料夾輸入以下，進入python解釋器，查詢我的免安裝系統的環境路徑

    cd /d C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64
    python
    import sys
    for e in sys.path:
        print(e)

僅有預設的路徑

    C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64\python310.zip
    C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64

修改環境路徑，使用編輯器開啟python310._pth_  
修改如下，1.加入上層的相對路徑符號 2.取消註解import site 使其有作用  
加入上層路徑可以將專案資料夾放在其上層，避免汙染環境  
import site 會將 Lib\site-packages 自動添加到 sys.path 使其可抓取環境的套件  

    python310.zip
    .
    ..
    # Uncomment to run site.main() automatically
    import site

重啟cmd, 再次查詢環境路徑，可以得到以下，已增加了環境路徑  

    C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64\python310.zip
    C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64
    C:\Users\user\Documents\Rogers\Temp
    C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64\lib\site-packages

CMD到該資料夾輸入以下，檢查該環境的pip是否安裝成功，輸入以下可查詢pip版本  
.\是本資料夾環境的python, 非全域的python  
    
    cd /d C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64
    .\python -m pip --version
    pip 22.2.2 from C:\Users\user\Documents\Rogers\Temp\python-3.10.6-embed-amd64\lib\site-packages\pip (python 3.10)

#  3.將該資料夾壓縮為.7z檔案不到10M，為已經有包含PIP的Poython環境，可作為專案初始開發環境  

該專案所需要的套件直接安裝在該環境  
專案資料夾放在上層，或其他位置，使用者不須安裝Python即可執行

    python-3.10.6-embed-amd64_initi_pip.7z