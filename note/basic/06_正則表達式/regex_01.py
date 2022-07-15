import re #引用正則式
findStr = '559A7.jeijij ji 270-6A65A733RRR4 dfef. 1551A5340-15A3.561A7.' #被尋找的字串
#regStr = r'(\d\d\d)-(\d\d\d)' #設定正則字串
#regStr = r'(\d{3})-(\d\d\d)'
#regStr = r'290-|144-'
#regStr = r'A3+\d'
regStr = r'A[1-9].*?A7'

#使用search 返回第一個Match物件
#mRegex = re.compile(regStr) #設定正則查找物件
#m = mRegex.search(findStr) #依正則式尋找字串

'''
if m:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
else:
    print('no match')
'''


#使用findall 返回所有Macth的List物件
mRegex = re.compile(regStr) #設定正則查找物件
mList = mRegex.findall(findStr) #依正則式尋找字串 返回第一個Match物件

if mList:
    print(mList)
else:
    print('no match')


