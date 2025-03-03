# py_compile_編譯加密



## 編譯

```
cd /d path
python -m py_compile secure.py
```

這會在 __pycache__/ 目錄下產生 secure.cpython-37.pyc 檔案（37 是 Python 版本）。


## 注意事項

.pyc 檔案必須與 Python 的版本對應（例如 Python 3.8 檔案不能在 3.9 版本上直接運行）。

