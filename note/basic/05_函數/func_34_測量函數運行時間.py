import time



def measureTime(func, num):
    tStart = time.time() #計時開始
    for i in range(1000000):
        func(num)
    tEnd = time.time() #計時結束
    print(f"{func.__name__} 總共執行了{(tEnd - tStart):.4f}秒")


