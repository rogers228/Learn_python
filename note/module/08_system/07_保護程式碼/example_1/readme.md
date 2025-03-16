# 說明

將關鍵源代碼編碼為二進位，無法輕易檢視，實現保護源代碼，並且能正常工作。
文件為01010101組成

# 正常匯入說明

1. 建立正常模組 tool_module.py
2. 正常匯入為 normal_import.py


# 加密匯入說明

1. 使用 binary.py 將 tool_module.py 轉換為 tool_module.py 二進位，即編碼加密
2. 使用 special_import.py 為匯入二進位源碼
