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
    direction = 'ccw' # ccw | cw

    th_start = 0; th_start_rad = np.radians(th_start)
    th_end = 135;  th_end_rad   = np.radians(th_end)

    if direction == 'ccw':  # 逆時針
        lis_th = np.linspace(th_start_rad, th_end_rad, 100)
    elif direction == 'cw':  # 順時針
        lis_th = np.linspace(th_start_rad, th_end_rad- 2*np.pi , 100)
    else:
        raise ValueError("direction 必須是 'ccw' 或 'cw'")


    arc_x = x + r * np.cos(lis_th)
    arc_y = y + r * np.sin(lis_th)
    ax.plot(arc_x, arc_y, color='blue', linewidth=1.5)
    ax.plot(arc_x[0], arc_y[0], 'go')    # 'go' 表示綠色圓點
    ax.plot(arc_x[-1], arc_y[-1], 'ro')  # 'ro' 表示紅色圓點
    plt.show()

def vector_to_polar_angle(dx, dy):
    # 向量 (dx, dy) 轉換為標準極角。
    angle_rad = np.arctan2(dy, dx)
    if angle_rad < 0:
        angle_rad += 2 * np.pi
    return angle_rad

def polar_angle_to_vector(angle_rad, r=1):
    # 標準極角（弧度）轉換為向量。
    dx = r * np.cos(angle_rad)
    dy = r * np.sin(angle_rad)
    return (dx, dy)

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

def find_intersection(line_a, line_b):
    # 計算兩條直線的交點，若直線平行或重合，返回 None。
    # 直線line_a, line_b (tuple): (起點 x0, 起點y0, 向量dx, dy)
    # 返回交點座標 (x, y)，若平行或重合，返回 None

    x0_a, y0_a, dx_a, dy_a = line_a
    x0_b, y0_b, dx_b, dy_b = line_b

    # 形成係數矩陣和常數項向量
    A = np.array([[dx_a, -dx_b], [dy_a, -dy_b]])
    B = np.array([x0_b - x0_a, y0_b - y0_a])

    # 計算行列式
    det = np.linalg.det(A)

    if det == 0:
        return None  # 平行或重合，無交點
    else:
        # 求解方程組
        t, s = np.linalg.solve(A, B)
        # 使用 t 求解交點座標
        x_intersection = x0_a + t * dx_a
        y_intersection = y0_a + t * dy_a
        return (x_intersection, y_intersection)

def distance_2point(coord1, coord2):
    # 使用畢式定理計算兩個平面座標之間的距離。
    # coord1, coord1: (x1, y1), (x2, y2)
    x1, y1 = coord1
    x2, y2 = coord2
    dx = x2 - x1
    dy = y2 - y1
    distance = np.sqrt(dx**2 + dy**2)
    return distance

def normalize_angle(angle_rad):
    # 將弧度角度歸一化到範圍 (0, 2π)
    return np.mod(angle_rad, 2 * np.pi)

def test3():
    # 向量 (dx, dy) 轉換為標準極角。
    point = (20, 5); angle_rad = vector_to_polar_angle(*point)
    print('point:', point, 'angle_rad:', angle_rad, 'angle_deg:', np.degrees(angle_rad))
    point = (-15, 25); angle_rad = vector_to_polar_angle(*point)
    print('point:', point, 'angle_rad:', angle_rad, 'angle_deg:', np.degrees(angle_rad))
    point = (-25, -30); angle_rad = vector_to_polar_angle(*point)
    print('point:', point, 'angle_rad:', angle_rad, 'angle_deg:', np.degrees(angle_rad))
    point = (18, -3); angle_rad = vector_to_polar_angle(*point)
    print('point:', point, 'angle_rad:', angle_rad, 'angle_deg:', np.degrees(angle_rad))
    # 標準極角（弧度）轉換為向量。
    angle_deg = 280; vector = polar_angle_to_vector(np.radians(angle_deg), r=10)
    print('vector:', vector)


def test4():
    # 未完成
    plt.title('繪製圓弧 已知起點、終點、半徑、方向')
    start_point = (10, 50)  # 起點
    end_point = (90, 51)    # 終點
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

    # 求向量的標準極角
    abs_c1p1_rad = vector_to_polar_angle(*vector_c1p1)
    abs_c1p2_rad = vector_to_polar_angle(*vector_c1p2)
    abs_c2p1_rad = vector_to_polar_angle(*vector_c2p1)
    abs_c2p2_rad = vector_to_polar_angle(*vector_c2p2)
    print('abs_c1p1_rad:', abs_c1p1_rad, 'abs_c1p1_deg:', np.degrees(abs_c1p1_rad))
    print('abs_c1p2_rad:', abs_c1p2_rad, 'abs_c1p2_deg:', np.degrees(abs_c1p2_rad))
    print('abs_c2p1_rad:', abs_c2p1_rad, 'abs_c2p1_deg:', np.degrees(abs_c2p1_rad))
    print('abs_c2p2_rad:', abs_c2p2_rad, 'abs_c2p2_deg:', np.degrees(abs_c2p2_rad))


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

def test5():
    # 兩直線交點
    line_a = (10, 2, 15, 8)  # 直線 a 的起點 (1, 2) 和方向向量 (3, 4)
    line_b = (10, 50, 15, 12)  # 直線 b 的起點 (1, 5) 和方向向量 (1, -1)
    intersection = find_intersection(line_a, line_b)
    if intersection:
        print(f"交點為: {intersection}")
    else:
        print("兩條直線平行或重合，無交點")


def test6():
    plt.title('以飛行圓弧，飛行偏角，由a點至b點畫圓弧')

    start_point = (10, 10)  # 起點
    end_point = (90, 80)    # 終點
    angle_fly_deg = 25 # 飛行偏角 >0 <90, >-90  負值為向左飛逆時鐘 正值為向右飛順時針

    if angle_fly_deg == 0:
        raise ValueError("飛行偏角不可為0度")
    elif abs(angle_fly_deg) >= 90:
        raise ValueError("飛行偏角必須小於等於90度")

    # print('angle_fly_deg:', angle_fly_deg)

    direction = 'ccw' if angle_fly_deg > 0 else 'cw'
    # print('direction:', direction)

    # 向量
    (p1_x, p1_y) = start_point # 起點
    (p2_x, p2_y) = end_point   # 終點
    vector_p1p2 = (p2_x - p1_x, p2_y - p1_y)
    # print(vector_p1p2)
    p1p2_rad = vector_to_polar_angle(*vector_p1p2)
    # print('p1p2_rad:', p1p2_rad, 'p1p2_deg:',np.degrees(p1p2_rad))

    # 飛行出角 與 飛行入角
    angle_fly_rad = np.radians(angle_fly_deg) # 飛行偏角
    angle_flyout_rad = p1p2_rad + (-1 * angle_fly_rad) # 飛行出角
    # print('angle_flyout_rad:', angle_flyout_rad, 'angle_flyout_deg:',np.degrees(angle_flyout_rad))
    angle_flyin_rad = p1p2_rad - (-1 * angle_fly_rad) # 飛行入角
    # print('angle_flyin_rad:', angle_flyin_rad, 'angle_flyin_deg:',np.degrees(angle_flyin_rad))

    # 求p1 p2 指向圓心的向量

    switch_direction = 1 if angle_fly_deg > 0 else -1 # switch_direction 飛行角度切換為標準極角 切換角度方向
    # print('switch_direction:', switch_direction)
    vector_p1_to_circle = polar_angle_to_vector(angle_flyout_rad + (switch_direction * 0.5 * np.pi))
    # print('vector_p1_to_circle:', np.degrees(vector_to_polar_angle(*vector_p1_to_circle)))
    vector_p2_to_circle = polar_angle_to_vector(angle_flyin_rad + (switch_direction * 0.5 * np.pi))
    # print('vector_p2_to_circle:', np.degrees(vector_to_polar_angle(*vector_p2_to_circle)))

    # 求圓心到p1, p2的 標準極角
    angle_circle_to_p1 = normalize_angle(vector_to_polar_angle(*vector_p1_to_circle) + np.pi)
    # print('angle_circle_to_p1:', angle_circle_to_p1, 'angle_circle_to_p1_deg:', np.degrees(angle_circle_to_p1))
    angle_circle_to_p2 = normalize_angle(vector_to_polar_angle(*vector_p2_to_circle) + np.pi)
    # print('angle_circle_to_p2:', angle_circle_to_p2, 'angle_circle_to_p2_deg:', np.degrees(angle_circle_to_p2))

    # 求圓心與半徑
    line_p1_to_circle = (p1_x, p1_y, *vector_p1_to_circle)
    line_p2_to_circle = (p2_x, p2_y, *vector_p2_to_circle)
    # print(line_p1_to_circle)
    # print(line_p2_to_circle)
    circle_o = find_intersection(line_p1_to_circle, line_p2_to_circle) # 圓心
    (ox, oy) = circle_o
    if circle_o is None:
        raise ValueError("兩條直線平行或重合，無交點")
    # print('circle_o:', circle_o)

    radius = distance_2point(circle_o, start_point)
    print('radius:', radius)

    # 作圖
    if direction == 'ccw':
        if angle_circle_to_p2 < angle_circle_to_p1:
            lis_th = np.linspace(angle_circle_to_p1, angle_circle_to_p2 + 2*np.pi, 100)
        else:
            lis_th = np.linspace(angle_circle_to_p1, angle_circle_to_p2, 100)

    elif direction == 'cw':
        if angle_circle_to_p2 > angle_circle_to_p1:
            lis_th = np.linspace(angle_circle_to_p1+ 2*np.pi, angle_circle_to_p2, 100)
        else:
            lis_th = np.linspace(angle_circle_to_p1, angle_circle_to_p2, 100)

    lis_deg =  np.round(np.degrees(lis_th),2)
    # print(lis_deg)

    # print(lis_th)
    arc_x = ox + radius * np.cos(lis_th)
    arc_y = oy + radius * np.sin(lis_th)
    ax.plot(arc_x, arc_y, color='blue', linewidth=1.5)
    ax.plot(arc_x[0], arc_y[0], 'go')    # 'go' 表示綠色圓點
    ax.plot(arc_x[-1], arc_y[-1], 'ro')  # 'ro' 表示紅色圓點

    plt.show()

if __name__ == '__main__':
    test1()



