import numpy as np

def test1():
    # 陣列屬性
    # ndim 維度
    # shape 長度
    # dtype 型別
    
    np1 = np.array([i*2 for i in range(1, 11)]) #使用for建立list
    print(np1)
    print(type(np1)) # python class
    print(len(np1))
    
    print('ndim:{0}, shape:{1}, dtype:{2}'.format(np1.ndim, np1.shape, np1.dtype)) #屬性

if __name__ == '__main__':
    test1()