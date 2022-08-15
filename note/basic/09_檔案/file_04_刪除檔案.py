# https://blog.gtwang.org/programming/python-howto-check-whether-file-folder-exists/

import os
oldfile = r'D:\06Python\test\01_基礎\09_檔案\456.txt'
if os.path.exists(oldfile): #檔案存在
    os.remove(oldfile)
    print('檔案已刪除')

# 要檢查的檔案路徑
filepath = "/etc/motd"

# 檢查檔案是否存在
if os.path.isfile(filepath):
    print("檔案存在。")
else:
    print("檔案不存在。")


# 要檢查的目錄路徑
folderpath = "/var/log"

# 檢查目錄是否存在 
if os.path.isdir(folderpath):
    print("目錄存在。")
else:
    print("目錄不存在。")