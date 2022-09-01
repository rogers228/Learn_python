from functools import partial
# partial偏函數
# 為函數添加固定引數，減少重複

def add(a, b):
    return (a+b)

def test1():
    print(add(3,4))
    print(add(3,8))
    print(add(3,12))
    print(add(3,46))
    # 以上3為固定引數

    # 在不改變原函式的情況下 將 3 作為固定引數 重新包裝
    add_n = partial(add, 3) # 建立add_n函數  使用add函數，第一個引數為3
    print(add_n(4))
    print(add_n(8))
    print(add_n(12))
    print(add_n(46))

if __name__ == '__main__':
    test1()