# 避免__file__失效 與 os.getcwd() 錯誤

1. __file__ 有些環境會失效
2. os.getcwd() 工作目錄 有些環境會不同

以上 2 個初始路徑都有缺陷


統一使用cmd.bat來啟動python
```bat
python script.py
```

使用 os.path.abspath(sys.argv[0]) 來取代 __file__

sys.argv[0] 是 script.py
os.path.abspath() 會轉換為絕對路徑

```py
import os, sys
    _p = os.path.dirname
    print('config_path0:', _p(_p(os.path.abspath(sys.argv[0]))))
```

