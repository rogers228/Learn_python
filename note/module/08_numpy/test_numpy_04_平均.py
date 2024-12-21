import numpy as np

def test1():
    arr1 = np.array([88, 82, 93, 74, 75, 83])
    print(arr1)

    # 計算平均值
    average = np.mean(arr1)
    print(average)

    difference = arr1 - average # 平均差
    print(difference)

    max_index = np.argmax(difference)
    min_index = np.argmin(difference)
    print(f'差異往上最大值是第{max_index+1}個 值是{arr1[max_index]}')
    print(f'差異往下最大值是第{min_index+1}個 值是{arr1[min_index]}')

if __name__ == '__main__':
    test1()