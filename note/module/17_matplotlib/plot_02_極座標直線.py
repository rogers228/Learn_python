import matplotlib.pyplot as plt
import numpy as np

def test2():
    #2點線段
    coor  = [(0, 5),(10,17)] #座標點
    print(coor)
    x = [c[0] for c in coor]
    y = [c[1] for c in coor]
    plt.plot(x, y, c='b')

    #增加紅色點標註
    for c in coor:
        plt.gca().add_patch(plt.Circle(c, 0.5, color='r'))

    plt.gca().set_aspect('equal') #等比
    plt.show()

def test1():
    #多點線段
    f = plt.figure()
    coor  = [(0, 5),(10,17),(35,17),(36,12)] #座標點 2點以上
    x = [c[0] for c in coor]
    y = [c[1] for c in coor]
    plt.plot(x, y, c='b')
    plt.show()
    f.savefig("test1.pdf", bbox_inches='tight')

if __name__ == '__main__':
    test2()
    print('ok')