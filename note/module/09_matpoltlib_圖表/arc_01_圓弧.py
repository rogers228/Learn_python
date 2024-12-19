import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rcParams
import numpy as np
import math

if True:
    rcParams['font.family'] = 'Microsoft JhengHei' # 微軟正黑體
    fig, ax = plt.subplots() # 建立圖表
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    ax.set_aspect('equal') # 設定比例，確保圓形為正圓
    ax.grid(which='major', color='black', linestyle='-', linewidth=0.5) # 添加主格線
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.5) # 添加副格線
    ax.set_xticks(range(0, 101, 10), minor=True)  # x 軸副刻度每 10
    ax.set_yticks(range(0, 101, 10), minor=True)  # y 軸副刻度每 10

def test1():
    plt.title('繪製圓形')
    x = 50
    y = 50
    r = 15
    circle = patches.Circle((x, y), r, edgecolor='blue', facecolor='none', linewidth=1.5)
    ax.add_patch(circle)
    plt.show()

def test2():
    plt.title('繪製圓弧 已知圓心x,y 半徑r 起始角度(絕對), 結束角度(絕對)')
    x = 50; y = 50; r = 25
    th_start = 0; th_start_rad = np.radians(th_start)
    th_end = 135;  th_end_rad   = np.radians(th_end)

    lis_th = np.linspace(th_start_rad, th_end_rad, 100)

    arc_x = x + r * np.cos(lis_th)
    arc_y = y + r * np.sin(lis_th)
    ax.plot(arc_x, arc_y, color='blue', linewidth=1.5)
    ax.plot(arc_x[0], arc_y[0], 'go')    # 'go' 表示綠色圓點
    ax.plot(arc_x[-1], arc_y[-1], 'ro')  # 'ro' 表示紅色圓點

    plt.show()

def test3():
    plt.title('繪製圓弧 已知圓心x,y 半徑r 起始角度(絕對), 增量圓弧角度')
    x = 50; y = 50; r = 30
    th_start = 180; # 起始角度(絕對)
    th_value = -180; # 圓弧角 (以起始角度的增量值)

    th_end = th_start + th_value # 結束角度
    th_start_rad = np.radians(th_start) # 起始角度 弧度
    th_end_rad   = np.radians(th_end)   # 結束角度 弧度

    lis_th = np.linspace(th_start_rad, th_end_rad, 100)
    arc_x = x + r * np.cos(lis_th)
    arc_y = y + r * np.sin(lis_th)
    ax.plot(arc_x, arc_y, color='blue', linewidth=1.5)
    ax.plot(arc_x[0], arc_y[0], 'go')
    ax.plot(arc_x[-1], arc_y[-1], 'ro')
    plt.show()


def find_circle_center2(x1, y1, x2, y2, r):
    # 求通過兩點的固定r的圓弧的圓心
    # 會有2個解

    # Step 1: 計算中點
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    # Step 2: 計算兩點之間的距離
    dx = x2 - x1
    dy = y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    # Step 3: 檢查半徑是否有效
    if r < d / 2:
        raise ValueError("半徑太小，無法形成圓")
    # Step 4: 計算圓心到中點的垂直距離
    h = math.sqrt(r**2 - (d / 2)**2)

    # Step 5: 計算圓心座標
    cx1 = mx - h * (dy / d)
    cy1 = my + h * (dx / d)
    cx2 = mx + h * (dy / d)
    cy2 = my - h * (dx / d)

    return (cx1, cy1), (cx2, cy2)

def test4():
    # 未完成
    plt.title('繪製圓弧 已知起點、終點、半徑、方向')
    start_point = (0, 0)  # 起點
    end_point = (4, 0)    # 終點
    radius = 3            # 圓弧半徑

    (x1, y1) = start_point
    (x2, y2) = end_point
    (cx1, cy1), (cx2, cy2) = find_circle_center2(*start_point, *end_point, radius)
    print(cx1, cy1)
    print(cx2, cy2)

    # # # 2. 計算起點和終點的角度
    # th_start_rad = np.arctan2(y1 - cy, x1 - cx)  # 起點角度
    # th_end_rad = np.arctan2(y2 - cy, x2 - cx)    # 終點角度
    # # print(th_start_rad, th_end_rad)
    # print(np.degrees(th_start_rad), np.degrees(th_end_rad))

    # # 3. 生成角度範圍，根據方向選擇是否順時針或逆時針
    # angles = np.linspace(th_start_rad, th_end_rad, 100)
    # arc_x = cx + radius * np.cos(angles)
    # arc_y = cy + radius * np.sin(angles)

    # ax.plot(arc_x, arc_y, color='blue', linewidth=1.5)
    # ax.plot(arc_x[0], arc_y[0], 'go')
    # ax.plot(arc_x[-1], arc_y[-1], 'ro')
    # plt.show()

if __name__ == '__main__':
    test4()