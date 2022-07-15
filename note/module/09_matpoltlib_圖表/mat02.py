import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50) #-1~1 個數50
y1 = 2*x + 1
y2 = x** 2

#plt.figure() #建立圖形
#plt.plot(x, y1) #繪圖
#plt.show()


plt.figure(num = 3, figsize=(8,5),) #建立圖形
plt.plot(x, y2) #繪圖
plt.plot(x, y1, color = 'red', linewidth = 1.5, linestyle = '--') #繪圖
plt.show()
