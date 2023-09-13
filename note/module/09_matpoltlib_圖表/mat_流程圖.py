import matplotlib.pyplot as plt
import matplotlib.patches as patches

def test1():
    fig, ax = plt.subplots() # 取得圖 與 軸
    ax.set_aspect(1) # 長寬比
    # data
    lis_caption = ['step1', 'step2']
    lis_pos = [(0.3, 0.5),(0.7, 0.5)]
    for i, (caption, pos) in enumerate(zip(lis_caption, lis_pos)):
        x, y = pos

        # 基準點
        # circle = plt.Circle((x, y), 0.01, color='gray' )
        # ax.add_artist(circle) # 添加圓

        font_size = 12
        plt.text(x, y, caption, ha='center', fontsize=font_size) # 文字

        # 矩形
        rect_w = len(caption)*0.03
        rect_h = font_size * 0.003
        lb_x, lb_y = x-(rect_w/2), y-(rect_h/2) # 左下xy
        rt_x, rt_y = x+(rect_w/2), y+((rect_h/2)*2.85) # 右上xy
        len_x = abs(lb_x-rt_x) # 長度
        len_y = abs(lb_y-rt_y) # 長度
        # test
        # circle = plt.Circle((lb_x, lb_y), 0.012, color='blue' )
        # ax.add_artist(circle) # 添加圓
        # circle = plt.Circle((rt_x, rt_y), 0.012, color='purple' )
        # ax.add_artist(circle) # 添加圓

        rect = patches.Rectangle((lb_x, lb_y), len_x, len_y, linewidth=0, edgecolor='none', facecolor='yellowgreen')
        ax.add_patch(rect)

        # 點
        circle = plt.Circle((x ,y-0.05), 0.01, color='gray' )
        ax.add_artist(circle) # 添加圓
        # 線與箭頭
        if i != len(lis_caption)-1:
            next_x, next_y = lis_pos[i+1]
            plt.annotate('', xytext=(x, y-0.05), xy=(next_x, y-0.05), arrowprops=dict(arrowstyle='->'))

    # plt.title('test')
    plt.axis('off')  # 隱藏坐標軸
    plt.show()

if __name__ == '__main__':
    test1()
