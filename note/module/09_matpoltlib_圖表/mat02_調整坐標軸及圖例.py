import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50) #-1~1 個數50
y1 = 2*x + 1
y2 = x** 2


plt.figure
l1 = plt.plot(x, y1, label = 'linear line') #繪圖
l2 = plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--', label = 'square line') #繪圖


#設定坐標軸範圍
plt.xlim((-1, 2)) #設定x軸範圍
plt.ylim((-2, 3)) #設定x軸範圍
plt.xlabel('i am x') #設定x軸標籤


#設定圖例
#plt.legend(loc='upper right') #圖例在右上
#plt.legend(loc='best')    #圖例在左下
plt.legend(loc=4)    #圖例在右下 圖例位置0~10
plt.show()
