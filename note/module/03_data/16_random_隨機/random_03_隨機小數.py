import random

def test1():
    # 0~1 隨機小數
    x = random.random()
    print(x)

def test2():
    # 特定範圍內7~9 隨機小數
    # x = random.uniform(7,9)
    x = round(random.uniform(7,9),3) # 取小數三位
    print(x)

if __name__ == '__main__':
    test2()