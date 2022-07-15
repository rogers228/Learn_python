def test7():
    lis_a = 'sdfdfsda'
    lis_b = '121344889413103224848'
    #共同迭代  多餘截斷
    for idx, (e, n) in enumerate(zip(lis_a,lis_b)):
        print(f'index:{idx}, e:{e}, n:{n}')