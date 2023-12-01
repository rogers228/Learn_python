html_str='''156125613156
1256156
15615656
1561651556
15615656
778899
123456
'''

f=r'D:\06Python\test\01_基礎\02_字串與變數\test55.txt'

html_file= open(f,"w")
#指定編碼
#file = open(filename,"w", encoding='utf-8')
html_file.write(html_str)
html_file.close()

print('finish')


with open("test.html", "r", encoding='utf-8') as f:
    text= f.read()
