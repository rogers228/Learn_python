def test8():
    lis_a = [1,65,3]
    lis_b = [15,16,17]
    #共同迭代  多餘截斷
    func_max = lambda a,b: a if a>b else b
    lis_c = [func_max(a,b) for a, b in zip(lis_a,lis_b)]
    print(lis_c)