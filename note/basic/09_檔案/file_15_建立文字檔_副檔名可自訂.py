f= open("test.py","w+")
print("ok")


currdir = os.getcwd() #當前路徑
file = 'test.csv' #檔名
filename = currdir + '\\' + file

#create csv
f= open(filename,"w+")
