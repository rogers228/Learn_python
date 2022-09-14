def test1():
    dic = { 'one':'oneasfasf',
            'two':'twodsffsafd'}
    print(dic)
    
    mykey = 'r'
    if mykey in list(dic.keys()):
        print(dic[mykey])
    else:
        print('no key')

    # 使用get 輕鬆取值
    print(dic.get(mykey, 'no key'))

if __name__ == '__main__':
    test1()