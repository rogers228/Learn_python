def test2():
    #lis不足時補滿
    c_max = 5 #預設數量
    lis = [12,65]
    if len(lis) < c_max:
        lis.extend([0]*(c_max-len(lis)))
    print(lis)

def test3():
    #lis超過時截斷
    c_max = 5 #預設數量
    lis = [12,65,5,9,8,1,5,6,8]
    if len(lis) > c_max:
        lis = [lis[i] for i in range(len(lis)) if i < c_max]
    print(lis)