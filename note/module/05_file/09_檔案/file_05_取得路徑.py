import os
currdir = os.getcwd() #當前路徑
print(currdir)

file = '123.txt' #檔名
fullpath = currdir + '\\' + file
print(fullpath)

cnstr = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;'
print(cnstr)

cnstr = cnstr % fullpath
print(cnstr)


# 完整檔案路徑
__file__
# 完整檔案路徑  使用 cmd 執行時  用以下 才不會錯誤
full_file = os.path.join(os.getcwd(), os.path.basename(__file__))