from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt



y_data = [2,3, 5,7,8,
          9,12,5,4,3,
          2,3, 5,8,9]

#print(y_data)
x = [10,20,30,40,50,
     60,70,80,90,100,
     120,140,170,200,250]
#print(x)

#style
cf = FontProperties(fname = r'C:\Windows\Fonts\mingliu.ttc') #新細明體
# cf = FontProperties(fname = r'C:\Windows\Fonts\msjhbd.ttf') #微軟正黑體 粗體


plt.figure() #建立圖形
plt.plot(x, y_data) #繪圖
plt.xlabel('pressure壓力', fontproperties = cf)
plt.ylabel('flow流量', fontproperties = cf)
plt.show()



