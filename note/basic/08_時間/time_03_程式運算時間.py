import time
'''
time.clock 非常精確的cpu時間
用來檢測程式的時間
'''

timer1 = time.perf_counter()
i = 1
t=''
while i <= 100:
    t = t + str(i) + ','
    i += 1 
print(t)
print('運算時間:',time.perf_counter()-timer1)
