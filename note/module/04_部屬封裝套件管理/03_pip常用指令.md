pip是管理python模組的程式，它沒有圖形介面，是用命令視窗cmd視窗直接下命令。

cmd
執行 cmd 呼叫出cmd視窗 切換到path
windows檔案總管空白處shift+滑鼠右鍵 在此處開啟命令視窗，等同上列指令

    cd /d path

查看pip版本

    python -m pip --version

列出所有模組

    python -m pip list

更新pip至最新版
    
    python -m pip install -U pip


安裝套件

    python -m pip install flask

更新套件

    python -m pip install -U flask

移除套件

    python -m pip uninstall flask

指定安裝版本

    python -m pip install -v flask==1.0 

產生安裝requirements.txt

    python -m pip freeze > requirements.txt

依照文件安裝

    python -m pip install -r requirements.txt


指定資料夾離線安裝 依照文件安裝

    python -m pip install --no-index --find-links flask_files -r requirements.txt

僅下載套件安裝檔

    python -m pip download flask