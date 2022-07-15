def test38():
    # filter 迭代篩選 為True者
    lis = [1,2,2,2,3]
    lis = list(filter(lambda e: e != 2,lis))
    print(lis)