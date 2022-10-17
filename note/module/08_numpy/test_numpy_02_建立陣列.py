import numpy as np
import pandas as pd

def test2():
    #使用預設值 建立陣列
    np1 = np.zeros(10) #1維
    print(np1)

    np2 = np.ones(5) #1維
    print(np2)

    np3 = np.zeros([2,4]) #2維
    print(np3)

def test1():
    #使用list 建立array
    np1 = np.array([1, 2, 3])
    print(np1)

    lis2 = [5.8, 25.4, 763.0]
    np2 = np.array(lis2)
    print(np2)

    lis3 = ['a','b', 6.05] #無法建立不同型別的陣列   將強制轉為文字
    np3 = np.array(lis3)
    print(np3)

    lis4 = [True, True, False]
    np4 = np.array(lis4)
    print(np4)

    # lis5 = list(i for i in range(10))
    np5 = np.array([i*2 for i in range(1, 11)]) #使用for建立list
    print(np5)
    print(np5[9]) # 索引取值

def test3():
    # 二維陣列
    arr = np.array([[10.2, 'yo'], [4, 'bro'],
                    [4, 'low'], [1, 'NumPy']])
    print(type(arr))
    print(arr)
    print(arr[0,0].dtype)
    # df = pd.DataFrame(arr)
    # print(df)
    # print(df.dtypes)

if __name__ == '__main__':
    test3()