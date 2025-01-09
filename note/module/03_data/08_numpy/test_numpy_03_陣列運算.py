import numpy as np

# ndarray 的四則運算就是  直接相同索引的元素運算
# 大幅提升效能

def test1():
    # 一維 ndarray 加 減 乘 除
    # 會直接將相同index相加 減 乘 除
    a = np.array([2, 4, 6])
    b = np.array([4, 5, 6])
    # b = np.array([4, 5, 6, 0])
    result = a + b  # 若長度不同 則接報錯
    print(result)

def test2():
    # 二維 ndarray 加 減 乘 除
    # 會直接將相同 row 相同 index相 加 減 乘 除
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [1, 2, 3]])
    print(a)
    print(b)
    result = a * b
    print(result)



if __name__ == '__main__':
    test2()