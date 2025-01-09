import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import math

if True:
    w_width = 700 # 窗體大小
    w_height = 500
    dpi = 120
    width_inch = w_width / dpi
    height_inch = w_height / dpi
    cf = FontProperties(fname = r'C:\Windows\Fonts\mingliu.ttc') #新細明體
    # https://robkerr.ai/matplotlib-color-keys/
    colors = ['mediumblue', 'maroon', 'green']

def test1():
    caption = '鑽頭刀具中心出水孔\n孔徑-面積對照表'
    plt.figure(figsize=(width_inch, height_inch), dpi=dpi) #建立圖形
    plt.xlim(0.2, 1.6) # 圖表x界線範圍
    plt.ylim(0, 5) # 圖表y界線範圍

    x = np.linspace(0.4, 1.5, 100) # 生成範圍從 a 到 b 的 n 個數值
    r = x / 2
    area_1 = math.pi * (r ** 2)
    area_2 = math.pi * (r ** 2) * 2
    area_3 = math.pi * (r ** 2) * 3


    plt.plot(x, area_1, color=colors[0]) #繪圖
    plt.plot(x, area_2, color=colors[1]) #繪圖
    plt.plot(x, area_3, color=colors[2]) #繪圖

    plt.xlabel('出水孔直徑(mm)', fontproperties = cf)
    plt.ylabel('出水總截面積(mm²)', fontproperties = cf)
    plt.grid(True, which='major', linestyle='-', linewidth=0.8, color='gray')  # 主格線
    plt.minorticks_on()  # 打開副刻度
    plt.grid(True, which='minor', linestyle=':', linewidth=0.5)  # 副格線
    # plt.legend(loc='best', prop=cf)  # 顯示圖例，位置自動選擇最佳
    plt.figtext(0.136, 0.798, caption, ha="left", fontsize=11, fontproperties=cf,
        bbox=dict(facecolor='lightgray', edgecolor='none'))

    plt.text(1.2, 1.3, "1出水孔", fontsize=11, color=colors[0], rotation=20, ha='center', va='center', fontproperties=cf)
    plt.text(1.2, 2.5, "2出水孔", fontsize=11, color=colors[1], rotation=38, ha='center', va='center', fontproperties=cf)
    plt.text(1.2, 3.7, "3出水孔", fontsize=11, color=colors[2], rotation=49, ha='center', va='center', fontproperties=cf)
    plt.show()

def chart_power1():
    rpm = 1740
    hz = 60
    interval = 10 # 線段的精度
    caption = f'壓力與所需電機馬力、功率\n({hz}Hz {rpm}rpm)'
    fig, ax1 = plt.subplots(figsize=(width_inch, height_inch), dpi=dpi)
    # 主 X 軸顯示 kg/cm²
    plt.xlim(0, 70)  # 圖表 x 軸範圍
    plt.ylim(0, 5)   # 馬力的 y 軸範圍
    max_hp = 5  # 最大馬力 (HP)

    # 計算排量和對應的馬力
    def_max_p = lambda hp, q: (450*hp)/q        # 最大壓力 = (450*馬力)/流量
    def_cc2l = lambda cc, rpm: cc * rpm / 1000  # 公升

    cc1 = 19; q1 = def_cc2l(cc1, rpm) # 排量: cc 公升
    x_p1 = np.linspace(0, def_max_p(max_hp, q1), interval)  # 生成壓力數據 0 ~ 最大壓力
    y_hp1 = (x_p1 * q1)  / 450           # 馬力計算

    cc2 = 24; q2 = def_cc2l(cc2, rpm)
    x_p2 = np.linspace(0, def_max_p(max_hp, q2), interval)
    y_hp2 = (x_p2 * q2)  / 450

    cc3 = 28; q3 = def_cc2l(cc3, rpm)
    x_p3 = np.linspace(0, def_max_p(max_hp, q3), interval)
    y_hp3 = (x_p3 * q3)  / 450

    # 第一個 Y 軸 (馬力 HP)
    ax1.plot(x_p1, y_hp1, color=colors[0], label="19cc")
    ax1.plot(x_p2, y_hp2, color=colors[1], label="24cc")
    ax1.plot(x_p3, y_hp3, color=colors[2], label="28cc")

    ax1.set_xlabel('出水泵最高壓力(kg/cm²)', fontproperties=cf)
    ax1.set_ylabel('電機所需出力(HP)', fontproperties=cf)
    ax1.grid(True, which='major', linestyle='-', linewidth=0.8, color='gray')
    ax1.minorticks_on()
    ax1.grid(True, which='minor', linestyle=':', linewidth=0.5)

    # 添加文字標籤
    ax1.text(50, 3.9, f"{cc1}cc ({q1}L)", fontsize=11, color=colors[0], rotation=37, ha='center', va='center')
    ax1.text(40, 3.9, f"{cc2}cc ({q2}L)", fontsize=11, color=colors[1], rotation=42, ha='center', va='center')
    ax1.text(30, 3.5, f"{cc3}cc ({q3}L)", fontsize=11, color=colors[2], rotation=47, ha='center', va='center')

    # 第二個 Y 軸 (功率 kW)
    ax2 = ax1.twinx()  # 創建第二個共享 X 軸的 Y 軸
    ax2.set_ylim(0, 5 * 0.7457)  # 將最大馬力轉換為 kW
    ax2.set_ylabel('電機所需出力(kW)', fontproperties=cf)

    # 第二個 X 軸 (壓力 MPa)
    ax3 = ax1.twiny()  # 創建第二個共享 X 軸
    ax3.set_xlim(ax1.get_xlim())  # 保持 X 軸對應範圍相同
    ax3.set_xlabel('出水泵最高壓力(MPa)', fontproperties=cf)
    ax3.set_xticks(ax1.get_xticks())  # 保持刻度相同
    ax3.set_xticklabels([f'{x * 0.0980665:.2f}' for x in ax1.get_xticks()])  # 轉換 kg/cm² 為 MPa

    # 添加圖表標題
    plt.figtext(0.136, 0.798, caption, ha="left", fontsize=11, fontproperties=cf,
        bbox=dict(facecolor='lightgray', edgecolor='none'))

    plt.show()

def chart_power2():
    rpm = 1420
    hz = 50
    interval = 10 # 線段的精度
    caption = f'壓力與所需電機馬力、功率\n({hz}Hz {rpm}rpm)'
    fig, ax1 = plt.subplots(figsize=(width_inch, height_inch), dpi=dpi)
    # 主 X 軸顯示 kg/cm²
    plt.xlim(0, 85)  # 圖表 x 軸範圍
    plt.ylim(0, 5)   # 馬力的 y 軸範圍
    max_hp = 5  # 最大馬力 (HP)

    # 計算排量和對應的馬力
    def_max_p = lambda hp, q: (450*hp)/q        # 最大壓力 = (450*馬力)/流量
    def_cc2l = lambda cc, rpm: cc * rpm / 1000  # 公升

    cc1 = 19; q1 = def_cc2l(cc1, rpm) # 排量: cc 公升
    x_p1 = np.linspace(0, def_max_p(max_hp, q1), interval)  # 生成壓力數據 0 ~ 最大壓力
    y_hp1 = (x_p1 * q1)  / 450           # 馬力計算

    cc2 = 24; q2 = def_cc2l(cc2, rpm)
    x_p2 = np.linspace(0, def_max_p(max_hp, q2), interval)
    y_hp2 = (x_p2 * q2)  / 450

    cc3 = 28; q3 = def_cc2l(cc3, rpm)
    x_p3 = np.linspace(0, def_max_p(max_hp, q3), interval)
    y_hp3 = (x_p3 * q3)  / 450

    # 第一個 Y 軸 (馬力 HP)
    ax1.plot(x_p1, y_hp1, color=colors[0], label="19cc")
    ax1.plot(x_p2, y_hp2, color=colors[1], label="24cc")
    ax1.plot(x_p3, y_hp3, color=colors[2], label="28cc")

    ax1.set_xlabel('出水泵最高壓力(kg/cm²)', fontproperties=cf)
    ax1.set_ylabel('電機所需出力(HP)', fontproperties=cf)
    ax1.grid(True, which='major', linestyle='-', linewidth=0.8, color='gray')
    ax1.minorticks_on()
    ax1.grid(True, which='minor', linestyle=':', linewidth=0.5)

    # 添加文字標籤
    ax1.text(62, 3.9, f"{cc1}cc ({q1}L)", fontsize=11, color=colors[0], rotation=37, ha='center', va='center')
    ax1.text(49, 3.9, f"{cc2}cc ({q2}L)", fontsize=11, color=colors[1], rotation=42, ha='center', va='center')
    ax1.text(37, 3.5, f"{cc3}cc ({q3}L)", fontsize=11, color=colors[2], rotation=47, ha='center', va='center')

    # 第二個 Y 軸 (功率 kW)
    ax2 = ax1.twinx()  # 創建第二個共享 X 軸的 Y 軸
    ax2.set_ylim(0, 5 * 0.7457)  # 將最大馬力轉換為 kW
    ax2.set_ylabel('電機所需出力(kW)', fontproperties=cf)

    # 第二個 X 軸 (壓力 MPa)
    ax3 = ax1.twiny()  # 創建第二個共享 X 軸
    ax3.set_xlim(ax1.get_xlim())  # 保持 X 軸對應範圍相同
    ax3.set_xlabel('出水泵最高壓力(MPa)', fontproperties=cf)
    ax3.set_xticks(ax1.get_xticks())  # 保持刻度相同
    ax3.set_xticklabels([f'{x * 0.0980665:.2f}' for x in ax1.get_xticks()])  # 轉換 kg/cm² 為 MPa

    # 添加圖表標題
    plt.figtext(0.136, 0.798, caption, ha="left", fontsize=11, fontproperties=cf,
        bbox=dict(facecolor='lightgray', edgecolor='none'))

    plt.show()

if __name__ == '__main__':
    chart_power2()
