import numpy as np


def test1():
    #1維取值
    np5 = np.array([i*2 for i in range(1, 11)]) #使用for建立list
    print(np5)
    print(np5[9]) # 1維  索引取值


    #2維取值
    np1 = np.array([[1, 2, 3, 4], 
                    [31, 32, 33, 34],
                    [241,242,243,244]])
    print(np1)
    print('ndim:{0}, shape{1}, dtype:{2}'.format(np1.ndim, np1.shape, np1.dtype)) #屬性
    print(np1[1]) # 索引取值  整列
    print(np1[1,3]) # 索引取值

if __name__ == '__main__':
    test1()