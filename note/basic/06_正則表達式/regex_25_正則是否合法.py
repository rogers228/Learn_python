import re

def is_valid_pattern(pattern):
    try:
        re.compile(pattern)  # 嘗試編譯正則表達式
        return True          # 若無錯誤，則 pattern 合法
    except re.error as e:
        print(f"正則錯誤: {e}")
        return False         # 捕捉錯誤，pattern 非法

# 測試範例
patterns = [
    r'^.{11}2.*',     # 正確
    r'^.*{11}2.*',    # 錯誤
    r'[a-z]+(\d{3})', # 正確
    r'(?P<id>\w+)(',  # 錯誤 (括號未閉合)
]

for p in patterns:
    print(f"Pattern: {p} -> 合法" if is_valid_pattern(p) else f"Pattern: {p} -> 非法")
