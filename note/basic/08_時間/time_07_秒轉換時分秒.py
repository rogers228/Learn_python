def gerhms(g):
    #g 秒 轉換為時分秒 範例 00:05:27
    h= int(g / 3600) #時
    m = int((g - (h * 3600)) / 60) #分
    s = g - (h * 3600) - (m* 60)
    return '{:0>2d}:{:0>2d}:{:0>2d}'.format(h,m,s)




print(gerhms(260))
