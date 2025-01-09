from multiprocessing import Process, Pool
import os , time

def func1(i):
    result = i * i
    time.sleep(0.1)
    return result

def test3():
    # pool.apply_async  益步執行
    lis_inputs = [x for x in range(10)]
    print(lis_inputs)

    with Pool(4) as pool:
        for x in lis_inputs:
            # print(x)
            result = pool.apply_async(func1, (x,))
            print(result.get())

    pool.close() #池關閉
    print('123')    
    pool.join() #開始執行

def test2():
    # cpu 數量
    # pool數量 大於cpu會降低處理效率
    cpus = os.cpu_count()
    print('cpus', cpus)

def test1():
    # 處理程序數量 pool
    lis_inputs = [x for x in range(1000)]
    # print(lis_inputs)
    pool = Pool(4) #處理程序數量
    lis_outputs = pool.map(func1, lis_inputs) # map
    print(lis_outputs)

if __name__ == '__main__':
    test3()