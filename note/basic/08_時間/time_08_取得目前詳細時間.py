from datetime import datetime
now = datetime.now()
print(now)

#取得詳細時間
y, m, d, h, n, s = now.year, now.month, now.day, now.hour, now.minute, now.second
print(y, m, d, h, n, s)

#自訂時間
mydate = datetime(2019,10,10,18,30,29) 
print(mydate)

#取得自訂時間的時數
print(now.minute)

#格式化
print('{:0>4d}{:0>2d}{:0>2d}{:0>2d}{:0>2d}{:0>2d}'.format(y, m, d, h, n, s))

print('{:0>4d}{:0>2d}{:0>2d}000000'.format(y, m, d))
