import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


# ✅ 設定中文字體（以 Windows 為例）
matplotlib.rcParams['font.family'] = 'Microsoft JhengHei'  # 微軟正黑體
matplotlib.rcParams['axes.unicode_minus'] = False  # 正確顯示負號

def circular_motion_with_z(x0, y0, r, h, num_points=100):
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = x0 + r * np.cos(theta)
    y = y0 + r * np.sin(theta)
    y_min = y0 - r
    y_max = y0 + r
    z = ((y - y_min) / (y_max - y_min)) * h
    return x, y, z

def test1():
    # 參數設定：圓心 (3,5)，半徑 2，高度 10
    x0, y0, r, h = 3, 5, 2, 10
    x_vals, y_vals, z_vals = circular_motion_with_z(x0, y0, r, h)

    # 建立圖形
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # 繪製曲線
    ax.plot(x_vals, y_vals, z_vals, label='圓周 + 線性上升路徑', color='royalblue')
    ax.scatter([x0], [y0], [0], color='red', label='圓心', s=50)

    # 設定標籤與標題
    ax.set_title('圓周運動 + 線性Z軸上升', fontsize=14)
    ax.set_xlabel('X 軸')
    ax.set_ylabel('Y 軸')
    ax.set_zlabel('Z 軸')
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.show()

def test2(): # 動畫
    # 基本參數
    x0, y0, r, h = 3, 5, 2, 10
    num_points = 200
    x_vals, y_vals, z_vals = circular_motion_with_z(x0, y0, r, h, num_points)

    # 建立 3D 圖
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # 繪製完整軌跡線
    ax.plot(x_vals, y_vals, z_vals, label='圓周 + 線性上升路徑', color='skyblue')

    # 設定固定範圍
    ax.set_xlim(x0 - r - 1, x0 + r + 1)
    ax.set_ylim(y0 - r - 1, y0 + r + 1)
    ax.set_zlim(0, h + 2)

    # 標籤與標題
    ax.set_title('圓周運動動畫', fontsize=14)
    ax.set_xlabel('X 軸')
    ax.set_ylabel('Y 軸')
    ax.set_zlabel('Z 軸')

    # 加上移動的點 P
    point, = ax.plot([], [], [], 'ro', label='移動點 P', markersize=8)
    ax.legend()

    # 更新動畫的函數
    def update(frame):
        point.set_data([x_vals[frame]], [y_vals[frame]])           # <- 包成序列
        point.set_3d_properties([z_vals[frame]])                   # <- 同樣包成序列
        return point,

    ani = FuncAnimation(fig, update, frames=num_points, interval=10, blit=True)

    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    test2()