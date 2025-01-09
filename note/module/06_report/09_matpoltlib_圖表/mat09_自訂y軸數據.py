import matplotlib.pyplot as plt
import numpy as np

y_data = [2,3,5,7,8,9,12,5,4,3,2,3,5,8,9]
#print(y_data)
x = list(range(0,len(y_data))) #產生由0開始 共y_data數量個
#print(x)

plt.figure() #建立圖形
plt.plot(x, y_data) #繪圖
plt.show()



