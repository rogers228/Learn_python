# 原本在不同資料夾的py檔  引用相同的模組時
# 會使用不同的import寫法  相當不便
# 使用sys.path.append 可以加入搜尋模組的路徑


import sys, os
sys.path.append(r'U:\dsprog\py_excel\tools') #加入資料夾路徑   使用絕對路徑  cmd執行才會正確
import test_module_a as ts #這樣就可以方便引用了  不同的執行檔  寫法已可以相同了



sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)))  #加入上層目錄的路徑
if __name__ == '__main__':
    print(ts.t_func_a())