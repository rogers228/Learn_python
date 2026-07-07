02 基本操作


## 步驟一：在專案內建立虛擬環境

```
cd /d C:\Users\USER\Documents\test_venv
python -m venv venv
```
會自動產生一個 venv/ 資料夾，裡面就是乾淨獨立的 Python 環境。


## 步驟二：啟用虛擬環境

```
venv\Scripts\activate.bat
```

啟用成功後，命令列前面會看到 (venv)，代表已切換到虛擬環境。



## 在linux建立虛擬python 環境

cd ~/projects/test_linux              linux ~代表本機 路徑使用/ (右斜) 與windows不同
python3 -m venv venv                  python3 是使用linux主要的 python3
source venv/bin/activate              啟動虛擬環境  終端機最前面出現 (venv)
deactivate                            退出虛擬環境