def test5():
    lis_a = 'sdfdfsda'
    lis_b = '121344889413103224848'

    #共同迭代  多餘截斷
    for e,n in zip(lis_a,lis_b):
        print(e,n)

    #共同迭代  以最長的為主 不足為None
    from itertools import zip_longest
    for e,n in zip_longest(lis_a,lis_b):
        print(e,n)


    # 指定不足的值
    # zip_longest(lis_a, lis_b, fillvalue=0)