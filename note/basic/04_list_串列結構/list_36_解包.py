# 解包

def test1():
    lis1 = [1,3,5]
    lis2 = [77, *lis1]
    print(lis1)
    print(lis2)

if __name__ == '__main__':
    test1()