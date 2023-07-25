import os
currdir = os.getcwd() #當前路徑
print(currdir)
file = 'test.html' #檔名
fullpath = currdir + '\\' + file



'''
currdir = os.getcwd() #當前工作目錄
print(currdir)

currdirname = os.path.split(os.getcwd())[1] #當前資料夾名稱
print(currdirname)

fullname = sys.argv[0] #當前完整檔案名稱
print(fullname)

sname = os.path.basename(sys.argv[0])  #當前檔案名稱含附檔名
print(sname)

sname_a = os.path.basename(sys.argv[0]).split('.')[0] #當前檔案名稱
print(sname_a)

sname_b = os.path.basename(sys.argv[0]).split('.')[1] #當前檔案附檔名
print(sname_b)
'''


# 取得所有附檔名為js的檔案
from glob import glob
currdir = os.getcwd() #當前路徑
def test2():
    path_public = os.path.join(currdir, 'public')
    print(path_public)
    py_files = glob(os.path.join(path_public, "*.js"))
    print(py_files)