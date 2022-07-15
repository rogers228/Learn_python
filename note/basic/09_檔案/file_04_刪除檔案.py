import os
oldfile = r'D:\06Python\test\01_基礎\09_檔案\456.txt'
if os.path.exists(oldfile): #檔案存在
    os.remove(oldfile)
    print('檔案已刪除')
