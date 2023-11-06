# 各種繪圖計算
import numpy as np
import math
import matplotlib.pyplot as plt

def circle_border(center, radius, angle_radian):
    # 求圓上座標
    # 使用三角函數計算點的座標
    # center 圓心座標
    x = center[0] + radius * np.cos(angle_radian)
    y = center[1] + radius * np.sin(angle_radian)
    return x, y

def arc_length(angle_radian, radius):
    # 使用弧度計算弧長
    # angle_radians 弧度
    # radius 半徑
    arc_length = angle_radian * radius
    return arc_length

def deg2rad(degrees):
    return np.deg2rad(degrees)

def sin(rad):
    return np.sin(rad)

def cos(rad):
    return np.cos(rad)

def tan(rad):
    return np.tan(rad)

def sqrt(x): # 平方根
    return np.sqrt(x)

def is_approach(val, x, tol=0.001):
    # val 是否逼近 x 小於tol
    return abs(val-x) <= tol

def get_nps(lis_angle_radian):
    # 判斷一個弧度的端點，在直角坐標系的落點 若在軸線或象限上
    # 回傳值 1,2,3,4 象限
    # 5 +x軸線
    # 6 +y軸線
    # 7 -x軸線
    # 8 -y軸線
    # angle_radians 弧度 lis
    atol = 0.00001
    lis_x = np.cos(lis_angle_radian)
    lis_y = np.sin(lis_angle_radian)
    lis_nps = []
    for x, y in zip(lis_x, lis_y):
        if is_approach(x, 1, atol) and is_approach(y, 0, atol):
            lis_nps.append(5)
        elif is_approach(x, 0, atol) and is_approach(y, 1, atol):
            lis_nps.append(6)
        elif is_approach(x, -1, atol) and is_approach(y, 0, atol):
            lis_nps.append(7)
        elif is_approach(x, 0, atol) and is_approach(y, -1, atol):
            lis_nps.append(8)
        elif x > 0 and y > 0:
            lis_nps.append(1)
        elif x < 0 and y > 0:
            lis_nps.append(2)
        elif x < 0 and y < 0:
            lis_nps.append(3)
        elif x > 0 and y < 0:
            lis_nps.append(4)
        else:
            lis_nps.append(9)
    return lis_nps

def th_involute(center, lis_angle_radian, radius):
    # 圓心角 求漸開線 的點座標
    # center 圓心座標
    # lis_angle_radian 弧度 應小於90度
    # radius 半徑

    lis_a = arc_length(lis_angle_radian, radius)
    lis_b = tan(lis_angle_radian)*lis_a
    lis_c = sqrt(lis_b**2 + lis_a**2)
    lis_x = cos(lis_angle_radian)*(radius+lis_b)
    lis_Y = sin(lis_angle_radian)*(radius+lis_b)
    lis_y = lis_Y- lis_c
    # print(lis_a)
    # print(lis_b)
    nps = get_nps(lis_angle_radian)
    # print(nps)

    lis_result = []
    for i in range(len(lis_angle_radian)):
        a = lis_a[i]
        b = lis_b[i]
        c = lis_c[i]
        x = lis_x[i]
        Y = lis_Y[i]
        y = lis_y[i]
    
        if nps[i] in [1,2,3,4]:
            lis_result.append((x+center[0], y+center[1]))
        elif nps[i] in [5, 7]:
            lis_result.append((radius+center[0], 0+center[1]))
        elif nps[i] in [6, 8]:
            # lis_result.append((0+center[0], arc_length(deg2rad(90),radius)+center[1]))
            lis_result.append((arc_length(deg2rad(90),radius)+center[0], radius+center[1]))
        else:
            print('error')
    return lis_result


def calculate_points_on_arc(center, radius, start_angle, end_angle, num_points):
    # 依照圓弧求線上點座標
    # mode 特殊調整 1
    points = []
    angle_increment = (end_angle - start_angle) / (num_points - 1)
    for i in range(num_points):
        angle = math.radians(start_angle + i * angle_increment)
        x = round((center[0] + radius * math.cos(angle)),3)
        y = round((center[1] + radius * math.sin(angle)),3)
        points.append((x, y))
    return points

def points2draw(points):
    # 繪製連續曲線
    x = [p[0] for p in points]
    y = [100-p[1] for p in points]
    plt.figure(figsize=(500/80, 500/80))
    plt.scatter(x, y, marker='o', color='gray')  # 使用 scatter 绘制点

    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi+2, yi-2, str(i), color='red', fontsize=10, ha='center', va='center')  # 在点旁边加上索引

    plt.xlim(0, 100); plt.ylim(0, 100)
    plt.title('points'); plt.xlabel('x'); plt.ylabel('y')
    plt.show()