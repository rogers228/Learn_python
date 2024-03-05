
# 任意字元
pattern = r'[\s\S]' # 任何字元  包含換行
pattern = r'.'      # 任何字元  不包含換行符

# 空格
pattern = r'\s' # 空白符 包含 \r\n\t\f\v
pattern = r'\S' # 非 空白符
pattern = r'[^\S\n]' # 不包含換行符號的空格

# 字符
pattern = r'\w' # 字符，包括 字母a-z、數字0-9、底線_
                # 不包含 小數點.
pattern = r'\W' # 非 字符

# 數字
pattern = r'/d'     # 數字0~9  無副號
pattern = r'[0-9]'  # 數字0~9  無副號
pattern = r'\d+(\.\d+)?'  # 小數  無副號

# 次數
pattern = r'*'  # 任意次 0次或多次
pattern = r'?'  # 任意次 0次或1次
pattern = r'+'  # 任意次 1次獲多次
pattern = r'{n}'  # 指定n次
pattern = r'{1}'   # 指定1次  不可為負數
pattern = r'{1,}'  # 至少符合1次  等同 +
pattern = r'{1,2}' # 至少1到2次

pattern = r'[^a]'  # 0次a 使用^ not 表達式

# 位置
pattern = r'^Hello' # 指定開頭 *******
pattern = r'World$' # 指定結尾
pattern = r'World(\n+)$ ' # 指定結尾  結尾可以有換行 或 無 換行
pattern = r'World\b' # 單字邊界
pattern = r'World\B' # 非 單字邊界


# 括號說明
pattern = r'{1}'          # 大括號 次數  指定1次
pattern = r'[\s\S]'       # 中括號 一個字元為   任何字元  包含換行
pattern = r'\d+(\.\d+)?'  # 小括號 正則使用括號 為一起搭配次數

# 邏輯
pattern = r'[^\S\n]'  # ^ not 相反 不是 非  (在中括號的^)
pattern = r'a|b'      # | or 或

# 轉義 \
pattern = r'\n '    # 轉義字符  將標準字符轉換為特殊意義，例如 \n
pattern = r'\( '   # 將特殊含義字符12個 ^$()* +?.[\{| 轉換為 普通字符

# 文本特殊符號
# 通常都看不出來
# \r表示回車符（Carriage Return），ASCII碼為13。
# \n表示換行符（Line Feed），ASCII碼為10。
# \t表示製表符（Tab），ASCII碼為9。
# \f表示換頁符（Form Feed），ASCII碼為12。
# \v表示垂直製表符（Vertical Tab），ASCII碼為11。

# ^ 有2含意  開頭, 及not
