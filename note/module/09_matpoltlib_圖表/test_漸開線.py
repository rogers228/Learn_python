import matplotlib.pyplot as plt
import numpy as np

from tool_draw import *

def test1():
    radians = np.linspace(0, 2* np.pi, 100)
    x, y = circle_border((0,0), 50, radians)
    plt.figure()
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.gca().set_aspect('equal') # 等比例
    plt.plot(x, y, color='blue', linewidth=1) #繪圖
    plt.plot(50, 0, 'ro', markersize=5)  # point
    plt.show()

def test2():
    print(get_nps(deg2rad([0,1,270.0009])))

def test3():
    radians = np.linspace(0, deg2rad(90), 100)
    radius = 50
    points = th_involute((0,0), radians, radius)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.figure()
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.gca().set_aspect('equal') # 等比例
    plt.plot(x, y, color='blue', linewidth=1) # 繪圖
    plt.plot(50, 0, 'ro', markersize=5) # point
    plt.show()

if __name__ == '__main__':
    test3()
