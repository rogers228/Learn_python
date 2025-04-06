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