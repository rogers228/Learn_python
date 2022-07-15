import re #引用正則式
'''使用正則式找出是否符合
findStr: 被尋找的字串
regStr: 正則表達式
'''

def isRegMath(findStr, regStr):
    if findStr == None:
        return False
    mRegex = re.compile(regStr)
    match = mRegex.search(findStr)
    if match:
        return True
    
    else:
        return False


#使用範例
#find = None
find = '6AA030564456'
print(isRegMath(find, r'^6AA03.*'))


#使用範例2

if isRegMath(find, r'^6AA03.*'):
    print('YES')
else:
    print('N')


