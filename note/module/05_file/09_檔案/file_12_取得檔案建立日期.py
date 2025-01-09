import os
import time

a = r'\\192.168.2.127\設計部\個人工作區\AA0031\02程式設計\06Python\test\01_basic_基礎\09_檔案\file_12_取得檔案建立日期.py'
modifiedTime = os.path.getmtime(a) #最後修改日期
createTime = os.path.getctime(a) #建立日期
print(modifiedTime)
print(createTime)

#or
print('last modified:{}'.format(time.ctime(os.path.getmtime(a))))
print('creaated:{}'.format(time.ctime(os.path.getctime(a))))
