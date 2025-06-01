import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from scipy.interpolate import make_interp_spline

if True:
    w_width = 700 # 窗體大小
    w_height = 500
    dpi = 120
    width_inch = w_width / dpi
    height_inch = w_height / dpi
    cf = FontProperties(fname = r'C:\Windows\Fonts\mingliu.ttc') #新細明體
    colors = ['mediumblue', 'maroon', 'green']

def test1():
    values_1 = [(0, 32.6),(10, 32.0),(20, 31.6), (30, 30.9), (40, 30.0), (50,29.5), (60, 28.4), (65, 17.0), (70, 9.7)]
    x1 = [e[0] for e in values_1] # 壓力 kg/cm²
    y1 = [e[1] for e in values_1] # 流量 LPM

    values_2 = [(0, 25.6),(10, 25.0),(20, 23.6), (30, 21.9), (40, 17.0), (50,15.5), (60, 13.4), (65, 11.0), (70, 6.7)]
    x2 = [e[0] for e in values_2]
    y2 = [e[1] for e in values_2]
    # 建立圖表
    plt.figure(figsize=(width_inch, height_inch))
    plt.plot(x1, y1, marker='o', linestyle='-', color='blue', label='PQ 曲線')
    plt.plot(x2, y2, marker='o', linestyle='-', color='maroon', label='PQ 曲線')
    # 標題與軸標籤
    plt.title('PQ曲線圖', fontsize=16, fontproperties = cf)
    plt.xlabel('Pressure 壓力 (kg/cm²)', fontsize=12, fontproperties = cf)
    plt.ylabel('Flow 流量 (LPM)', fontsize=12, fontproperties = cf)

    # 設定座標軸範圍
    plt.xlim(0, 80)
    plt.ylim(0, 50)

    # 顯示網格與圖例
    plt.grid(True)
    # plt.legend()

    # 顯示圖表
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test1()