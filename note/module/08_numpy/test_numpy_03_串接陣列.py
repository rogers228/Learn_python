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
    
if __name__ == '__main__':
    test3()