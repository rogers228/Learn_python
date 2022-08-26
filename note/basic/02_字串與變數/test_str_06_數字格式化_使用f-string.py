# https://www.twblogs.net/a/5b822eca2b717737e032da80
# https://steam.oxxostudio.tw/category/python/basic/format.html
def test1():
    # {content:format}
    a = 7789451.23456 # content
    print(f'and is {a}')
    print(f'and is {a:.3f}') # 小數3位
    print(f'and is {a:.0f}') # 小數0位  無小數點
    print(f'and is {a:,.3f}') # ,千位符號 小數3位

if __name__ == '__main__':
    test1()