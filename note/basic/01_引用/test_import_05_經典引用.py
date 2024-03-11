import sys, os
_p = os.path.dirname # 上層
sys.path.append(_p(__file__)) # 加入路徑  以本檔案為始的上層  非工作目錄為始  可以避免錯誤
from tool_string import (get_random_str)  # 引用該路徑的py
