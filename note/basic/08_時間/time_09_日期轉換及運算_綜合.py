import datetime
import time

# 日期轉換
mydate_Str = '2012/11/19'  # str字串
print('日期字串 mydate_Str: {0}'.format(mydate_Str))

mydate_datetime = datetime.datetime.strptime(mydate_Str,'%Y/%m/%d')  # str字串 轉 日期時間
print('str字串 轉 日期時間: {0}'.format(mydate_datetime))

mydate_datetime2Str = mydate_datetime.strftime('%Y/%m/%d') # 日期時間 轉 str字串
print('日期時間 轉 str字串: {0}'.format(mydate_datetime2Str))

mydate_time = time.mktime(mydate_datetime.timetuple()) #日期時間 轉 時間軸
print('mydate_time: {0}'.format(mydate_time))

mydate_time2Str = time.strftime('%Y/%m/%d', time.localtime(mydate_time)) # 時間軸 轉  str字串
print('時間軸 轉  str字串: {0}'.format(mydate_time2Str))

# 日期運算  2日期相差天數
d1 = datetime.datetime.strptime('2020/10/28','%Y/%m/%d')
d2 = datetime.datetime.strptime('2020/7/28','%Y/%m/%d')
delta = d1 - d2
print(delta.days) #2日期相差天數

# 日期運算  1日期+-天數
d3 = d1 + datetime.timedelta(days=3) #1日期+-天數
print(d3.strftime('%Y/%m/%d'))