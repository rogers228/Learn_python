import random

def test1():
    # 對 lis1的元素 的出現機率使用權種  k為產生元數數量
    lis1 = [0, 1, 2, 3]
    lis2 = random.choices(lis1, weights=(5, 10, 80 , 5), k=100)
    # print(lis2)
    print(f'共有{len(lis2)}個元素')
    print(f'0出現{lis2.count(0)}次')
    print(f'1出現{lis2.count(1)}次')
    print(f'2出現{lis2.count(2)}次')
    print(f'3出現{lis2.count(3)}次')
    
if __name__ == '__main__':
    test1()