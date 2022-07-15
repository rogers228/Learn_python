import os
currdir = os.getcwd() #當前路徑
files = os.listdir(currdir)
#列出全部
for i in range(len(files)):
    print(files[i])


print('-----')
files_path = [os.path._getfullpathname(x) for x in os.listdir(currdir)]

#列出全部
for i in range(len(files_path)):
    print(files_path[i])

print('-----')
#僅列出檔案
for i in range(len(files_path)):
    if os.path.isfile(files_path[i]):
        print(files_path[i])

print('-----')
#僅列出資料夾
for i in range(len(files_path)):
    if not os.path.isfile(files_path[i]):
        print(files_path[i])

