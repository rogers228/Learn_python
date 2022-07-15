import time

ticks= time.time()
print(ticks)

localtime=time.localtime(time.time())
print(localtime)

atime = time.asctime(time.localtime(time.time()))
print('本地時間為 :',atime)

print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))

print(time.strftime("%Y%m%d%H%M%S", time.localtime()))
