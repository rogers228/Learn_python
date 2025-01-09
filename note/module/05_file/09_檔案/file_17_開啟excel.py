# 使用cmd 使用excel啟動 最大化 該檔案
cmd = r'start "" /max EXCEL.EXE "' + self.xlsfile + '"'
# print(cmd)
os.system(cmd)