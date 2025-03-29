def test1():
    # 集合內將自動轉為亂序不重複的元素
    # 元素可任意類型
    s1 = set() # 建立空集合
    print(s1)
    print(len(s1))
    s1 = {2,5,6,7,8} # set集合
    print(s1)
    print(len(s1))
    lis = [5,6,7,'7',7]
    s2 = set(lis) # 由list建立集合
    print(s2)

    s3 = set('abcd') # 文字
    print(s3)
    s3.add('g') # 新增
    print(s3)
    s3.remove('a') # 刪除
    print(s3)

def test2():
    #判斷式
    s0 = {1,2,3,4}
    s1 = {3,4,5,6,7}
    s2 = {1,2,3}

    print(s2<=s0)
    print(s2<s0)
    print(s0>s2)
    print(s0>s0)

def test3():
    #運算
    s0 = {1,2,3,4}
    s1 = {3,4,5,6,7}
    s2 = {1,2,3}
    print(s0.union(s1))        # 聯集  全部+起來
    print(s0.intersection(s1)) # 交集  僅重複者   &
    print(s1.difference(s0))   # 差集  減去相同的元素
    print(s0.difference(s1))   # 差集  減去相同的元素
    print(s1.symmetric_difference(s0))  # 反向差集  僅保留  未重複的元素
    print(s0.symmetric_difference(s1))  # 結果同上

def test4():
    lis = ['SCM415', '415','綠十字','綠']
    pdstr = 'SCM415 HRC55~60 E0.5 噴砂'
    lis_in = [(e in pdstr) for e in lis]
    print(True in set(lis_in))


if __name__ == '__main__':
    test4()
    print('ok')