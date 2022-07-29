#莫凡教學
import multiprocessing as mp
import time

#--------7 進程鎖lock
def job7(v, num, lock):
    lock.acquire() # 鎖定
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)

    lock.release() # 釋放

def multicore7():
    #v 可視為公用變數 叫好理解
    lock = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job7, args=(v, 1, lock)) # args 必有逗號,
    p2 = mp.Process(target=job7, args=(v, 3, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

#--------6 共享記憶體(內存)
def test6():
    value = mp.Value('d',1) # type, value
    array = mp.Array('i',[1,2,3]) # type,  array

#--------5
def job5(x):
    return x*x

def multicore5():
    # pool 池 
    print('multicore5')
    # pool = mp.Pool() #自動計算cpu數量
    pool = mp.Pool(processes=4) #指定線程數量 通常符合cpu數量即可
    
    # map 將多個引數(列表) 使用map處理
    result = pool.map(job5, range(10))
    print(result)

    # apply_async 僅單個引數
    result = pool.apply_async(job5, (456,))
    print(result.get())

    # apply_async 使用列表生成式  即可多個引數處理  等同map
    result = [pool.apply_async(job5,(i,)) for i in range(10)]
    print([res.get() for res in result])

#--------3
def job2(q):
    result = 0
    for i in range(1000):
        result += i+ i**2 + i**3
    q.put(result) # queue

def test2():
    #q 可視為公用變數 叫好理解

    q =mp.Queue() # 駐列池(暫時存放)  
    p1 = mp.Process(target=job2, args=(q,)) # args 必有逗號,
    p2 = mp.Process(target=job2, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('res1', res1)
    print('res2', res2)
    print('res1+res2', res1+res2)

#--------2
def job1(a,b):
    print('aaaaa')

def test1():
    p1 = mp.Process(target=job1, args=(1,2))
    p1.start()
    p1.join()

if __name__ == '__main__':
    multicore7()