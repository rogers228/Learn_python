import os
a = r'\\192.168.2.127\設計部\個人工作區\AA0031\02程式設計\06Python\test\01_basic_基礎\09_檔案\tmp\af\inaf.txt'
b = r'\\192.168.2.127\設計部\個人工作區\AA0031\02程式設計\06Python\test\01_basic_基礎\09_檔案\tmp\bf\inaf.txt'
try:
    if os.path.exists(a): #檔案存在
        os.rename(a, b)
        print('移動完成')
except:
    print('err')
    pass
