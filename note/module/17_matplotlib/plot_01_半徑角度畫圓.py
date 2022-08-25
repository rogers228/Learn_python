import matplotlib.pyplot as plt
import numpy as np
import math

def test5():
    spar = 100 # 漸開線解析度

    k_m  = 1.25 # 模數
    k_z  = 13   # 齒數
    k_th = 30  # 壓力角
    k_s = 2.18 #齒厚

    k_d  = k_m*k_z  # 節圓直徑
    k_d_r = k_d/2
    # print('k_d', k_d)
    k_db = k_m*k_z*np.cos(np.radians(k_th))  # 基圓直徑
    k_db_r = k_db/2 # 基圓半徑

    k_da1 = 17.75 # 外齒大徑da1
    k_da1_r = k_da1/2
    k_df1 = 15.25 # 外齒小徑df1
    k_df1_r = k_df1/2
    
    # 漸開線函數
    
    # print(inv(49))

    #基圓
    th1 = np.linspace(np.radians(0), np.radians(360), 100)
    x1 = np.cos(th1) * k_db_r # x = cos*r
    y1 = np.sin(th1) * k_db_r # x = sin*r
    plt.plot(x1, y1, c='r', linewidth=0.5)

    # 外齒大徑da1
    th2 = np.linspace(np.radians(0), np.radians(360), 100)
    x2 = np.cos(th2) * (k_da1/2) # x = cos*r
    y2 = np.sin(th2) * (k_da1/2) # x = sin*r
    plt.plot(x2, y2, c='b', linewidth=0.5)

    #節圓
    th3 = np.linspace(np.radians(0), np.radians(360), 100)
    x3= np.cos(th3) * (k_d/2)
    y3 = np.sin(th3) * (k_d/2)
    plt.plot(x3, y3, color='m', linewidth=0.5)

    # 外齒小徑df1
    th4 = np.linspace(np.radians(0), np.radians(360), 100)
    x4 = np.cos(th4) * k_df1_r # x = cos*r
    y4 = np.sin(th4) * k_df1_r # x = sin*r
    plt.plot(x4, y4, c='b', linewidth=0.5)

    #漸開線(從基圓)
    inv = lambda x: np.tan(np.radians(x))- np.radians(x)
    s_r = np.linspace(k_db_r, k_da1_r, spar)
    uk_deg = np.degrees(np.arccos(k_db_r/s_r)) #展角α
    uk_x = s_r * np.cos(inv(uk_deg))
    uk_y = s_r * np.sin(inv(uk_deg))
    plt.plot(uk_x, uk_y, color='b', linewidth=0.5)
    plt.plot(uk_x, -uk_y, color='b', linewidth=0.5) #對y軸鏡射

    #漸開線在節圓上的點
    d_deg = np.degrees(np.arccos(k_db_r/k_d_r)) #節圓展角α
    print('d_deg',d_deg)
    d_x = k_d_r * np.cos(inv(d_deg))
    d_y = k_d_r * np.sin(inv(d_deg))
    print('d_x, d_y', d_x, d_y)
    plt.plot(d_x, d_y, 'o', color='black');

    #漸開線在da1上的點
    da1_deg = np.degrees(np.arccos(k_db_r/k_da1_r)) #節圓展角α
    print('da1_deg',da1_deg)
    da1_x = k_da1_r * np.cos(inv(da1_deg))
    da1_y = k_da1_r * np.sin(inv(da1_deg))
    print('da1_x, da1_y', da1_x, da1_y)
    plt.plot(da1_x, da1_y, 'o', color='black');

    #漸開線在df1上的點
    df1_deg = np.degrees(np.arccos(k_db_r/k_df1_r)) #節圓展角α
    print('df1_deg',df1_deg)
    df1_x = k_df1_r * np.cos(inv(df1_deg))
    df1_y = k_df1_r * np.sin(inv(df1_deg))
    print('df1_x, df1_y', df1_x, df1_y)
    plt.plot(df1_x, df1_y, 'o', color='black');

    #漸開線
    sf_r = np.linspace(k_df1_r, k_da1_r, spar)
    uf_deg = np.degrees(np.arccos(k_db_r/sf_r)) #展角α
    uf_x = sf_r * np.cos(inv(uf_deg))
    uf_y = sf_r * np.sin(inv(uf_deg))
    plt.plot(uf_x, uf_y, color='r', linewidth=1.0)

    #斜率
    p_d1 = ger_emdg(ger_em(0,0,d_x,d_y))
    print('p_d1', p_d1)

    #齒厚求點
    # k_s = 2.18 #齒厚 在上
    t1 = ger_seg(k_d_r, k_s) #齒厚半角
    print('k_d_r', k_d_r)
    print('k_s', k_s)
    print('t1', t1)

    th_ehk = ger_seg(k_d_r, k_s)/2 #齒厚半角
    print('th_ehk', th_ehk)
    x_s = k_d_r * np.sin(np.radians(th_ehk))
    print('x_s',x_s)
    y_s = ger_spe_y(k_d_r,0,0,x_s)
    print('y_s',y_s)
    p_d2 = ger_emdg(ger_em(0,0,x_s,y_s))
    print('p_d1', p_d1)
    print('p_d2', p_d2)
    plt.plot(x_s, y_s, 'o', color='black');

    #旋轉繪製正上方齒
    th_wh1= p_d2-p_d1 #旋轉角度
    print('th_wh1', th_wh1)
    uf_r = np.sqrt(uf_x**2 + uf_y**2)
    ug_th = ger_emdg(ger_em(0,0,uf_x,uf_y))
    ug_th = ug_th+th_wh1

    ug_x = uf_r * np.cos(np.radians(ug_th))
    ug_y = uf_r * np.sin(np.radians(ug_th))
    ug_x_rev = -ug_x
    plt.plot(ug_x, ug_y, color='r')
    plt.plot(ug_x_rev, ug_y, color='r')

    #畫弧
    #漸開線齒頂點

    pr_x0, pr_y0 = ug_x[0], ug_y[0]
    print('pr_x0, pr_y0', pr_x0, pr_y0)
    plt.plot(pr_x0, pr_y0, 'o', color='c');
    pr_d0 = ger_emdg(ger_em(0,0,pr_x0, pr_y0))
    print('pr_d0',pr_d0)
    pr_r0 = np.sqrt(pr_x0**2 + pr_y0**2)

    pr_x1, pr_y1 = ug_x[-1], ug_y[-1]
    print('pr_x1, pr_y1', pr_x1, pr_y1)
    plt.plot(pr_x1, pr_y1, 'o', color='black');
    pr_d1 = ger_emdg(ger_em(0,0,pr_x1, pr_y1))
    print('pr_d1',pr_d1)
    pr_d1c = pr_d1 + ((90-pr_d1)*2)
    th = np.linspace(np.radians(pr_d1),
                    np.radians(pr_d1c), 100)
    x = np.cos(th) * k_da1_r # x = cos*r
    y = np.sin(th) * k_da1_r # x = sin*r
    plt.plot(x, y, c='r')

    pr_x2, pr_y2 = -ug_x[0], ug_y[0]
    print('pr_x2, pr_y2', pr_x2, pr_y2)
    plt.plot(pr_x2, pr_y2, 'o', color='black');
    

    pr_d2 = 90+(90-pr_d0)
    print('pr_d2',pr_d2)

    ar_mth = 360/ k_z # 等分角
    pr_x3 = pr_r0 * np.cos(np.radians(pr_d0+ar_mth))
    pr_y3 = pr_r0 * np.sin(np.radians(pr_d0+ar_mth))
    plt.plot(pr_x3, pr_y3, 'o', color='black');
    pr_d3 = 180+ger_emdg(ger_em(0,0,pr_x3, pr_y3))
    print('pr_d3',pr_d3)
    
    th = np.linspace(np.radians(pr_d2),
                    np.radians(pr_d3), 100)
    x = np.cos(th) * k_df1_r # x = cos*r
    y = np.sin(th) * k_df1_r # x = sin*r
    plt.plot(x, y, c='r')

    #陣列正上方齒
    ar_mth = 360/ k_z # 等分角
    print('等分角',ar_mth)
    ug_r = np.sqrt(ug_x**2 + ug_y**2)
    # ug_r_rev = np.sqrt(ug_x_rev**2 + ug_y**2)
    for i in range(1,k_z): # 1始  k_z
        ug_th = ger_emdg(ger_em(0,0,ug_x, ug_y))
        # print(ug_th)
        ar_th = ug_th + i*ar_mth
        # print(ar_th)
        ar_x = ug_r * np.cos(np.radians(ar_th))
        ar_y = ug_r * np.sin(np.radians(ar_th))
        plt.plot(ar_x, ar_y, color='r')

    for i in range(1,k_z): # 1始  k_z
        ug_th_rev = 180+ger_emdg(ger_em(0,0,ug_x_rev, ug_y))
        # print(ug_th_rev)
        ar_th_rev = ug_th_rev + i*ar_mth
        # # print(ar_th_rev)
        ar_x_rev = ug_r * np.cos(np.radians(ar_th_rev))
        ar_y_rev = ug_r * np.sin(np.radians(ar_th_rev))
        plt.plot(ar_x_rev, ar_y_rev, color='r')

    plt.gca().set_aspect('equal') #等比
    plt.show()

def test4():
    spar = 100 # 漸開線解析度

    k_m  = 1.25 # 模數
    k_z  = 13   # 齒數
    k_th = 30  # 壓力角
    k_s = 2.18 #齒厚

    k_d  = k_m*k_z  # 節圓直徑
    k_d_r = k_d/2
    # print('k_d', k_d)
    k_db = k_m*k_z*np.cos(np.radians(k_th))  # 基圓直徑
    k_db_r = k_db/2 # 基圓半徑

    k_da1 = 17.75 # 外齒大徑da1
    k_da1_r = k_da1/2
    k_df1 = 15.25 # 外齒小徑df1
    k_df1_r = k_df1/2
    
    # 漸開線函數
    
    # print(inv(49))

    #基圓
    th1 = np.linspace(np.radians(0), np.radians(360), 100)
    x1 = np.cos(th1) * k_db_r # x = cos*r
    y1 = np.sin(th1) * k_db_r # x = sin*r
    plt.plot(x1, y1, c='r', linewidth=0.5)

    # 外齒大徑da1
    th2 = np.linspace(np.radians(0), np.radians(360), 100)
    x2 = np.cos(th2) * (k_da1/2) # x = cos*r
    y2 = np.sin(th2) * (k_da1/2) # x = sin*r
    plt.plot(x2, y2, c='b', linewidth=0.5)

    #節圓
    th3 = np.linspace(np.radians(0), np.radians(360), 100)
    x3= np.cos(th3) * (k_d/2)
    y3 = np.sin(th3) * (k_d/2)
    plt.plot(x3, y3, color='m', linewidth=0.5)

    # 外齒小徑df1
    th4 = np.linspace(np.radians(0), np.radians(360), 100)
    x4 = np.cos(th4) * k_df1_r # x = cos*r
    y4 = np.sin(th4) * k_df1_r # x = sin*r
    plt.plot(x4, y4, c='b', linewidth=0.5)

    #漸開線
    inv = lambda x: np.tan(np.radians(x))- np.radians(x)
    s_r = np.linspace(k_db_r, k_da1_r, spar)
    uk_deg = np.degrees(np.arccos(k_db_r/s_r)) #展角α
    uk_x = s_r * np.cos(inv(uk_deg))
    uk_y = s_r * np.sin(inv(uk_deg))
    plt.plot(uk_x, uk_y, color='b', linewidth=0.5)
    plt.plot(uk_x, -uk_y, color='b', linewidth=0.5) #對y軸鏡射

    #漸開線在節圓上的點
    d_deg = np.degrees(np.arccos(k_db_r/k_d_r)) #節圓展角α
    print('d_deg',d_deg)
    d_x = k_d_r * np.cos(inv(d_deg))
    d_y = k_d_r * np.sin(inv(d_deg))
    print('d_x, d_y', d_x, d_y)
    plt.plot(d_x, d_y, 'o', color='black');

    #漸開線在da1上的點
    da1_deg = np.degrees(np.arccos(k_db_r/k_da1_r)) #節圓展角α
    print('da1_deg',da1_deg)
    da1_x = k_da1_r * np.cos(inv(da1_deg))
    da1_y = k_da1_r * np.sin(inv(da1_deg))
    print('da1_x, da1_y', da1_x, da1_y)
    plt.plot(da1_x, da1_y, 'o', color='black');

    #漸開線在df1上的點
    df1_deg = np.degrees(np.arccos(k_db_r/k_df1_r)) #節圓展角α
    print('df1_deg',df1_deg)
    df1_x = k_df1_r * np.cos(inv(df1_deg))
    df1_y = k_df1_r * np.sin(inv(df1_deg))
    print('df1_x, df1_y', df1_x, df1_y)
    plt.plot(df1_x, df1_y, 'o', color='black');

    #漸開線
    sf_r = np.linspace(k_df1_r, k_da1_r, spar)
    uf_deg = np.degrees(np.arccos(k_db_r/sf_r)) #展角α
    uf_x = sf_r * np.cos(inv(uf_deg))
    uf_y = sf_r * np.sin(inv(uf_deg))
    plt.plot(uf_x, uf_y, color='r', linewidth=1.0)


    #斜率
    p_d1 = ger_emdg(ger_em(0,0,d_x,d_y))
    print('p_d1', p_d1)

    #齒厚求點
    # k_s = 2.18 #齒厚 在上
    t1 = ger_seg(k_d_r, k_s) #齒厚半角
    print('k_d_r', k_d_r)
    print('k_s', k_s)
    print('t1', t1)

    th_ehk = ger_seg(k_d_r, k_s)/2 #齒厚半角
    print('th_ehk', th_ehk)
    x_s = k_d_r * np.sin(np.radians(th_ehk))
    print('x_s',x_s)
    y_s = ger_spe_y(k_d_r,0,0,x_s)
    print('y_s',y_s)
    p_d2 = ger_emdg(ger_em(0,0,x_s,y_s))
    print('p_d1', p_d1)
    print('p_d2', p_d2)
    plt.plot(x_s, y_s, 'o', color='black');

    #旋轉繪製正上方齒
    th_wh1= p_d2-p_d1 #旋轉角度
    print('th_wh1', th_wh1)
    uk_r = np.sqrt(uk_x**2 + uk_y**2)
    uk_th = ger_emdg(ger_em(0,0,uk_x,uk_y))
    ug_th = uk_th+th_wh1

    ug_x = uk_r * np.cos(np.radians(ug_th))
    ug_y = uk_r * np.sin(np.radians(ug_th))
    ug_x_rev = -ug_x

    plt.plot(ug_x, ug_y, color='r')
    plt.plot(ug_x_rev, ug_y, color='r')

    #陣列正上方齒
    ar_mth = 360/ k_z # 等分角
    print('等分角',ar_mth)
    ug_r = np.sqrt(ug_x**2 + ug_y**2)
    # ug_r_rev = np.sqrt(ug_x_rev**2 + ug_y**2)
    for i in range(1,k_z): # 1始  k_z
        ug_th = ger_emdg(ger_em(0,0,ug_x, ug_y))
        # print(ug_th)
        ar_th = ug_th + i*ar_mth
        # print(ar_th)
        ar_x = ug_r * np.cos(np.radians(ar_th))
        ar_y = ug_r * np.sin(np.radians(ar_th))
        plt.plot(ar_x, ar_y, color='r')

    for i in range(1,k_z): # 1始  k_z
        ug_th_rev = 180+ger_emdg(ger_em(0,0,ug_x_rev, ug_y))
        # print(ug_th_rev)
        ar_th_rev = ug_th_rev + i*ar_mth
        # # print(ar_th_rev)
        ar_x_rev = ug_r * np.cos(np.radians(ar_th_rev))
        ar_y_rev = ug_r * np.sin(np.radians(ar_th_rev))
        plt.plot(ar_x_rev, ar_y_rev, color='r')

    plt.gca().set_aspect('equal') #等比
    plt.show()

def test3():
    k_m  = 1.25 # 模數
    k_z  = 13   # 齒數
    k_th = 30  # 壓力角
    k_d  = k_m*k_z  # 節圓直徑

    k_db = k_m*k_z*np.cos(np.radians(k_th))  # 基圓直徑
    k_db_r = k_db/2 # 基圓半徑

    #基圓
    th1 = np.linspace(np.radians(0), np.radians(360), 100)
    x1= np.cos(th1) * k_db_r # x = cos*r
    y1 = np.sin(th1) * k_db_r # x = sin*r
    plt.plot(x1, y1, c='b')

    #漸開線
    uk_start = 0  # 展角起始
    uk_close = 90 # 展角結束
    # th2 = np.linspace(np.radians(deg_start),
    #                 np.radians(deg_close), 100)
    uk = np.linspace(uk_start, uk_close, 100)
    # print(th2)
    x2 = k_db_r * np.sin(np.radians(uk)) - k_db_r * np.radians(uk) * np.cos(np.radians(uk))
    y2 = k_db_r * np.cos(np.radians(uk)) + k_db_r * np.radians(uk) * np.sin(np.radians(uk))
    plt.plot(x2, y2, color='r')
    
    #節圓
    th3 = np.linspace(np.radians(0), np.radians(360), 100)
    x3= np.cos(th3) * k_d/2
    y3 = np.sin(th3) * k_d/2
    plt.plot(x3, y3, color='m',  linewidth=0.5)

    #外齒大徑da1
    da1 = 17.75
    th4 = np.linspace(np.radians(0), np.radians(360), 100)
    x4= np.cos(th4) * da1/2
    y4 = np.sin(th4) * da1/2
    plt.plot(x4, y4, color='r',  linewidth=0.5)

    #外齒小徑df1
    df1 = 14.75
    th5 = np.linspace(np.radians(0), np.radians(360), 100)
    x5= np.cos(th5) * df1/2
    y5 = np.sin(th5) * df1/2
    plt.plot(x5, y5, color='r',  linewidth=0.5)

    plt.gca().set_aspect('equal') #等比
    plt.show()


def test2():
    #畫圓及圓上一點
    r= 40.25 # r半徑
    deg_start = 0 # 起始角度
    deg_close = 360 # 結束角度
    th = np.linspace(np.radians(deg_start),
                    np.radians(deg_close), 100) 
    x = np.cos(th) * r # x = cos*r
    y = np.sin(th) * r # x = sin*r
    plt.plot(x, y, c='b')

    #增加點
    pnt_th = 138.5 #圓上點的角度
    pnt_x = np.cos(np.radians(pnt_th)) * r # x = cos*r
    pnt_y = np.sin(np.radians(pnt_th)) * r # x = sin*r
    plt.gca().add_patch(plt.Circle((pnt_x, pnt_y), 2, color='r'))

    #旋轉角度

    plt.gca().set_aspect('equal') #等比
    plt.show()

def test1():
    r= 40.25 # r半徑
    x_circle, y_circle = 10, 35 # 圓心座標
    deg_start = 0 # 起始角度
    deg_close = 360 # 結束角度
    th = np.linspace(np.radians(deg_start),
                    np.radians(deg_close), 100)

    x = np.cos(th) * r + x_circle # x = cos*r
    y = np.sin(th) * r + y_circle # x = sin*r
    plt.plot(x, y, c='b')
    plt.gca().set_aspect('equal') #等比
    plt.show()

# def ger_gkr(r,a,b,x,y_rev=False):
#     #以知半徑r 圓心a,b 圓上座標x, y 求極座標徑度
#     #x 任何直
#     #y_rev 是否為負值
#     y = np.sqrt(r**2 - (x-a)**2)
#     if y_rev:
#         y=-y
#     rad = np.arctan((y-b)/(x-a))
#     return rad

def ger_rxy(r,a,b,rad):
    #以知半徑r 圓心a,b 徑度rad 求圓上座標
    x = a + r*np.cos(rad)
    y = b + r*np.sin(rad)
    return (x, y)

def ger_emrad(m):
    # 斜率求徑度
    return (np.arctan(m))

def ger_emdg(m):
    # 斜率求角度
    return np.degrees(np.arctan(m))

def ger_em(x1,y1,x2,y2):
    # 2點求斜率m
    return (y2-y1)/(x2-x1)

def ger_dim(x1,y1,x2,y2):
    # 2點求距離m
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)

def ger_seg(r, rl):
    # r半徑 rl弧長 求圓心角
    return np.degrees(rl/r)

def ger_spe_x(r, a, b, y):
    # r半徑 圓心(a,b), y求x
    return np.sqrt(r**2 -(y-b)**2) + a

def ger_spe_y(r, a, b, x):
    # r半徑 圓心(a,b), x求y
    return np.sqrt(r**2 -(x-a)**2) + b

def test6():
    x1, y1 = -20,20
    x2, y2 = 20, -10

    print(ger_dim(x1, y1, x2, y2))

if __name__ == '__main__':
    test3()
    # print(np.degrees(ger_gkr(8.125,0,0,-2,True)))
    # print(np.radians(45))
    # print(ger_rxy(8.125,0,0,np.radians(20)))
    # print(ger_rxy(8.125,3,4,np.radians(35)))
    # print(ger_emdg(4/3))
    # print(ger_emdg(1))
    # print(ger_emrad(1))
    # print(ger_em(0,0,3,30))
    # print(ger_seg(25,19.63))
    # print(ger_spe_x(5,0,0,4))
    # print(ger_spe_x(5,10,8,11))
    # print(ger_spe_y(5,10,8,14))
    print('ok')