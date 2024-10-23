import matplotlib.pyplot as plt
import numpy as np

# 通常x為固定數, y為應變數
x = np.linspace(-1, 1, 50) #-1~1 個數50
y = 2*x + 1

plt.figure() #建立圖形
plt.plot(x, y) #繪圖
plt.show()

