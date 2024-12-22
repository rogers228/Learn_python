import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rcParams
import numpy as np
# import math

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
    # 求過兩點的固定r的圓弧的圓心
    # 會有2個解

    # Step 1: 計算中點
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    # Step 2: 計算兩點之間的距離
    dx = x2 - x1
    dy = y2 - y1
    d = np.sqrt(dx**2 + dy**2)
    # Step 3: 檢查半徑是否有效
    if r < d / 2:
        raise ValueError("半徑太小，無法形成圓")
    # Step 4: 計算圓心到中點的垂直距離
    h = np.sqrt(r**2 - (d / 2)**2)

    # Step 5: 計算圓心座標
    cx1 = mx - h * (dy / d)
    cy1 = my + h * (dx / d)
    cx2 = mx + h * (dy / d)
    cy2 = my - h * (dx / d)

    return (cx1, cy1), (cx2, cy2)

def calculate_angle_and_direction(A, B):
    # 計算兩個向量的夾角 (0~360 度)
    # A: tuple - 向量 A 的 (x, y) 分量。
    # B: tuple - 向量 B 的 (x, y) 分量。

    # 計算內積與外積
    dot_product = A[0] * B[0] + A[1] * B[1]
    cross_product = A[0] * B[1] - A[1] * B[0]

    # 計算向量的模長
    magnitude_A = np.sqrt(A[0]**2 + A[1]**2)
    magnitude_B = np.sqrt(B[0]**2 + B[1]**2)

    # 計算夾角的餘弦值
    cos_theta = dot_product / (magnitude_A * magnitude_B)
    cos_theta = max(min(cos_theta, 1), -1)  # 限制 cos 值範圍避免數值誤差

    # 計算夾角（弧度）
    angle_rad = np.arccos(cos_theta)

    # 根據外積判斷順時針或逆時針方向
    if cross_product < 0:  # 順時針方向
        clockwise_angle = angle_rad
        counterclockwise_angle = 2 * np.pi - angle_rad
    else:  # 逆時針方向
        counterclockwise_angle = angle_rad
        clockwise_angle = 2 * np.pi - angle_rad

    return {
        "cw_angle_rad": clockwise_angle,
        "ccw_angle_rad": counterclockwise_angle,
        # "cw_angle_deg": np.degrees(clockwise_angle),
        # "ccw_angle_deg": np.degrees(counterclockwise_angle),
    }

def test4():
    # 未完成
    plt.title('繪製圓弧 已知起點、終點、半徑、方向')
    start_point = (10, 10)  # 起點
    end_point = (90, 90)    # 終點
    radius = 80            # 圓弧半徑
    direction = 'cw'       # 方向: cw順時針 | ccw逆時針

    (p1_x, p1_y) = start_point # 起點
    (p2_x, p2_y) = end_point   # 終點
    (c1_x, c1_y), (c2_x, c2_y) = find_circle_center2(*start_point, *end_point, radius) # 求過兩點的固定r的圓弧的圓心 有2個

    # 求 起點、終點 到2圓心的向量 共4個
    vector_c1p1 = (p1_x-c1_x, p1_y-c1_y) # 向量 c1p1
    vector_c1p2 = (p2_x-c1_x, p2_y-c1_y) # 向量 c1p2

    vector_c2p1 = (p1_x-c2_x, p1_y-c2_y) # 向量 c1p1
    vector_c2p2 = (p2_x-c2_x, p2_y-c2_y) # 向量 c1p2
    # print('c1:', c1_x, c1_y)
    # print('c2:', c2_x, c2_y)
    # print('vector_c1p1:', vector_c1p1)
    # print('vector_c1p2:', vector_c1p2)
    # print('vector_c2p1:', vector_c2p1)
    # print('vector_c2p2:', vector_c2p2)

    # 求向量的絕對角度
    abs_c1p1_rad = calculate_angle_and_direction((1,0), vector_c1p1)['ccw_angle_rad']
    abs_c1p2_rad = calculate_angle_and_direction((1,0), vector_c1p2)['ccw_angle_rad']
    abs_c2p1_rad = calculate_angle_and_direction((1,0), vector_c2p1)['ccw_angle_rad']
    abs_c2p2_rad = calculate_angle_and_direction((1,0), vector_c2p2)['ccw_angle_rad']
    # print('abs_c1p1_rad:', abs_c1p1_rad, 'abs_c1p1_deg:', np.degrees(abs_c1p1_rad))
    # print('abs_c1p2_rad:', abs_c1p2_rad, 'abs_c1p2_deg:', np.degrees(abs_c1p2_rad))
    # print('abs_c2p1_rad:', abs_c2p1_rad, 'abs_c2p1_deg:', np.degrees(abs_c2p1_rad))
    # print('abs_c2p2_rad:', abs_c2p2_rad, 'abs_c2p2_deg:', np.degrees(abs_c2p2_rad))

    # 以方向(cw, ccw)求兩個向量的夾角(起點到終點)
    c1_angle_rad = calculate_angle_and_direction(vector_c1p1, vector_c1p2)[f'{direction}_angle_rad']
    c2_angle_rad = calculate_angle_and_direction(vector_c2p1, vector_c2p2)[f'{direction}_angle_rad']
    # print('c1_angle_rad:', c1_angle_rad, 'c1_angle_deg:', np.degrees(c1_angle_rad))
    # print('c2_angle_rad:', c2_angle_rad, 'c2_angle_deg:', np.degrees(c2_angle_rad))

    # 以角度小者為圓弧圓心
    if c1_angle_rad <= c2_angle_rad:
        arc_c = (c1_x, c1_y)
        start_rad = abs_c1p1_rad  # 起點絕對角度(弧度)
        end_rad = abs_c1p2_rad    # 終點
    else:
        arc_c = (c2_x, c2_y)
        start_rad = abs_c2p1_rad  # 起點絕對角度(弧度)
        end_rad = abs_c2p2_rad    # 終點

    (cx, cy) = arc_c
    # print('arc_c:', cx, cy)
    # print('start_rad:', start_rad, 'start_deg:', np.degrees(start_rad))
    # print('end_rad:', end_rad, 'end_deg:', np.degrees(end_rad))

    # 生成角度範圍，根據方向選擇是否順時針或逆時針
    angles = np.linspace(start_rad, end_rad, 100)
    arc_x = cx + radius * np.cos(angles)
    arc_y = cy + radius * np.sin(angles)
    ax.plot(arc_x, arc_y, color='blue', linewidth=1.5)
    ax.plot(arc_x[0], arc_y[0], 'go')
    ax.plot(arc_x[-1], arc_y[-1], 'ro')
    plt.show()


if __name__ == '__main__':
    test4()



