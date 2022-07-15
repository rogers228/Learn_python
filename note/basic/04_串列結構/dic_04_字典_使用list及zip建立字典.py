def test78():
    #list 使用zip建立字典
    name = ['Muffin', 'Scone', 'Biscuit']
    price = [39, 25, 20]
    dic = dict(zip(name, price))
    print(dic)