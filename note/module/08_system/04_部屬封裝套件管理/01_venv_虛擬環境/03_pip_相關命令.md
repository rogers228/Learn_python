
## 啟動當前虛擬環境
```
cd /d C:\Users\USER\Documents\test_venv
venv\Scripts\activate.bat
```

## 使用目前python 的模組 pip 查看已安裝的套件清單
```
python -m pip list
```

## 安裝
```
python -m pip install 
```

## 導出 requirements.txt

requirements.txt 是目前縮安裝的套件。
導出的目的是為了，方便在不同的電腦或環境重新安裝套件
因為 venv 通常都不使用 git 同步

```
python -m pip freeze > requirements.txt
```

## 依照 requirements.txt 安裝套件

詳細規則如下

1. 未安裝過套件，存在於 requirements.txt 裡面，將安裝
2. 已安裝過套件 不存在於 requirements.txt 裡面，不會強制移除
3. 已安裝過套件 與 requirements.txt 版本相同 則忽略不重新安裝
4. 已安裝過套件 與 requirements.txt 版本不同 則升版或降版安裝

```
python -m pip install -r requirements.txt
```

若要乾淨，與 requirements.txt 完全一致，請參考 04_重新建置虛擬環境.md
