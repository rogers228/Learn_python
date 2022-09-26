import numpy as np

def test3():
    # 串接陣列
    np1 = np.array([1.0, 2.0, 3.0])
    print(np1)

    np2 = np.array([4.0, 5.0, 6.0])
    print(np2)

    np_a = np.append(np1, np2, 0) # 串接
    print(np_a)
    # [1. 2. 3. 4. 5. 6.]
    
def test4():
    # 以知頭尾 及元素數量 建立陣列
    np_arr = np.linspace(0.0, 2.5, num=33)
    print(np_arr)
    print(type(np_arr))
    print(type(np_arr[0]))
if __name__ == '__main__':
    test4()