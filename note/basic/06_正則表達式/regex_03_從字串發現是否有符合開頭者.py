import re #引用正則式
'''使用正則式找出是否符合
findStr: 被尋找的字串
regStr: 正則表達式
'''

def is_reg_match(find_str, reg_str):
    if not find_str:
        return False
    return bool(re.search(reg_str, find_str))

#使用範例
#find = None
find = '6AA030564456'
print(is_reg_match(find, r'^6AA03.*'))



