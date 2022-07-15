#以完整路徑取得檔名+副檔名
b = r'\\192.168.2.127\設計部\個人工作區\AA0031\02程式設計\06Python\test\01_basic_基礎\02_字串與變數\test_str_13_find_instr_尋找字串.py'
print(b)
newb = b[b.rfind('\\') + 1:]
print(newb)
