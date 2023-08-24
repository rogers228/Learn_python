import math
import matplotlib.pyplot as plt

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
    plt.scatter(x, y, marker='o', color='gray')  # 使用 scatter 绘制点

    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi+2, yi-2, str(i), color='red', fontsize=10, ha='center', va='center')  # 在点旁边加上索引

    plt.xlim(0, 100); plt.ylim(0, 100)
    plt.title('points'); plt.xlabel('x'); plt.ylabel('y')
    plt.show()

def test1():
    ps = []
    line = [(8, 14),(36, 14)]; line.pop(); ps += line
    arc = calculate_points_on_arc(
        center = (50, 14),
        radius = 14,
        start_angle = -180,
        end_angle = 0,
        num_points = 20); arc.pop(); ps += arc
    line = [(64, 14),(92, 14), (92, 78)]; line.pop(); ps += line
    arc = calculate_points_on_arc(
        center = (72, 78),
        radius = 20,
        start_angle = 0,
        end_angle = 90,
        num_points = 16); arc.pop(); ps += arc
    line = [(72, 98),(8, 98),(8, 70)]; line.pop(); ps += line
    arc = calculate_points_on_arc(
        center = (8, 56),
        radius = -14,
        start_angle = 270,
        end_angle = 90,
        num_points = 20); ps += arc

    points2txt(ps) # ouput to text
    # points2draw(ps) # 預覽點
    

if __name__ == '__main__':
    test1()