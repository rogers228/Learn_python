import re #引用正則式
'''使用正則式找出第一個數字
findStr: 被尋找的字串
regStr: 正則表達式
'''

def isRegMath(findStr):
    if findStr == None:
        return ''
    mRegex = re.compile(r'\d+\.?\d*')
    match = mRegex.search(findStr)
    if match:
        return match.group() #返回第一個被找到的值
    else:
        return ''

#使用範例

find = None
#find = ''
a = isRegMath(find)
if a != '':
    print(a)
    print(type(a))
else:
    print("is \'\'")


