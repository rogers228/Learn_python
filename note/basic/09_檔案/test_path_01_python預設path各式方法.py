import os

def test1():

    f = r'C:\Users\user\Desktop\test.xlsx'
    # f = r'C:\Users\user\Desktop'

    print(f)
    print(os.path.exists(f)) #是否存在
    print(os.path.isabs(f))  #是否為絕對路徑
    print(os.path.isfile(f)) #是否為檔案
    print(os.path.isdir(f))  #是否為目錄
    print(os.path.islink(f)) #是否為連結

    if os.path.isfile(f): #是否為檔案
        print(os.path.basename(f)) #檔案名稱(含副檔名)
        print(os.path.dirname(f))  #目錄名稱(最後無斜線)
        print(os.path.getsize(f))  #檔案大小
        print(os.path.getmtime(f)) #修改時間

        print(os.path.split(f))    #元組 (目錄名稱, 檔案名稱)
        print(os.path.splitext(f)) #元組 (附檔名之前部分, 附檔名)

        #檔案名稱不含副檔名
        print('Filename: {0}'.format(
            os.path.split(f)[1].replace(os.path.splitext(f)[1],'')))

        #副檔名
        print('Extension: {0}'.format(os.path.splitext(f)[1]))

if __name__ == '__main__':
    test1()
    print('ok')