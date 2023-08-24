import math
import matplotlib.pyplot as plt
from itertools import cycle

# 依照圓弧求線上點座標
def calculate_points_on_arc(center, radius, start_angle, end_angle, num_points, mode=0):
    # mode 特殊調整 1
    if mode == 1:
        start_angle, end_angle = end_angle, start_angle # 角度對調 
    points = []
    angle_increment = (end_angle - start_angle) / (num_points - 1)
    for i in range(num_points):
        angle = math.radians(start_angle + i * angle_increment)
        x = round((center[0] + radius * math.cos(angle)),3)
        y = round((center[1] + radius * math.sin(angle)),3)
        points.append((x, y))
    return points

def points2txt(points):
    lis_points = [f'({x}, {y})' for x, y in points]
    points_string = '[' + ', '.join(lis_points) +']'
    with open('points.txt', 'w', encoding='utf-8') as f:
        f.write(points_string)

def points2draw(points):
    x = [p[0] for p in points]
    y = [100-p[1] for p in points]
    plt.figure(figsize=(500/80, 500/80))
    # plt.plot(x, y, marker='o', linestyle='-')

    colors = cycle(['red', 'yellow', 'green'])  # 使用 itertools.cycle 创建颜色迭代器
    for i in range(len(x) - 1):
        color = next(colors) 
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]], marker='o', linestyle='-', color=color)

    plt.xlim(0, 100); plt.ylim(0, 100)
    plt.title('points'); plt.xlabel('x'); plt.ylabel('y')
    plt.show()

def test1():
    ps = []
    line = [(10, 16),(36, 16)]; ps += line
    arc = calculate_points_on_arc(
        center = (50, 16),
        radius = -14,
        start_angle = 180,
        end_angle = 0,
        num_points = 10, mode=1); ps += arc
    # points2txt(ps)
    points2draw(ps)



if __name__ == '__main__':
    test1()