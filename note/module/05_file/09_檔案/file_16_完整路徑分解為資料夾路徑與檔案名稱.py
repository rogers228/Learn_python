import os, sys

#分解檔案與路徑
mypath = r'C:\Users\user\Dropbox\yshr\error\123.txt'
print(mypath)
parts = os.path.split(mypath)
print(parts)
print(parts[0])
print(parts[1])