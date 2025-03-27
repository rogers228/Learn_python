# Type Hint（型別註解）詳細說明

這行中的作用是 「型別註解（Type Hint）」，用來標註變數 db 的型別。這屬於 Python 的型別提示（Type Hinting） 機制，讓開發者更容易閱讀程式碼，並幫助工具（如 IDE 或靜態分析工具）進行型別檢查。

然而，Python 不會強制執行型別檢查，以下程式碼仍然可以執行：

```python
def add(x: int, y: int) -> int:
    return x + y
```

x: int 和 y: int 表示 x 和 y 變數應該是 int 型別。
-> int 表示函式的返回值應該是 int。