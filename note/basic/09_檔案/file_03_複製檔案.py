import shutil
oldfile = r'D:\06Python\test\01_基礎\09_檔案\123.txt'
newfile = r'D:\06Python\test\01_基礎\09_檔案\456.txt'
shutil.copy2(oldfile, newfile)
print('複製完畢')
