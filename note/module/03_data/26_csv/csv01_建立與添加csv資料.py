import os
currdir = os.getcwd() #當前路徑
file = 'test.csv' #檔名
fullname = currdir + '\\' + file

def list2csvrow(lis):
    '''List列表轉換為csv row
    預設逗號,為分隔 \n為換行
    '''
    t = ''
    for s in lis:
        t += str(s) + ','
    if len(t) > 0:
        t = t[:-1] #去除字尾,
    return t + '\n'

#檢查csv 若不存在則建立
fields = ['Name', 'Branch', 'Year', 'CGPA']
if not os.path.exists(fullname): #檔案不存在
    with open(fullname,'w+') as f: # w+ create file 
        f.write(list2csvrow(fields)) # \n在csv預設為換行
        f.close()
    print('create')

#Add
with open(fullname,'a+') as f: # a+ Append
    f.write(list2csvrow(['Rogers',23,89,46.3]))
    f.write(list2csvrow(['Allen',6,49,12.3]))
    f.close
    print('write')
