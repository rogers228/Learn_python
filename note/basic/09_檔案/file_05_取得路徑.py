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
