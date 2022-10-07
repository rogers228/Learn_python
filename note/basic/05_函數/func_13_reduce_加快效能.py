from functools import reduce

def test1():
    mav_value = 100
    lis = [e**2 for e in range(1,mav_value+1)]
    # print(lis)
    s = 0
    for e in lis:
        s += e

    print(s)

def test2():
    mav_value = 100
    lis = [e**2 for e in range(1,mav_value+1)]
    # print(lis)

    # (((1+2)+3)+4)
    s = reduce(lambda x,y:x+y, lis)
    print(s)
    return

if __name__ == '__main__':
    test2()