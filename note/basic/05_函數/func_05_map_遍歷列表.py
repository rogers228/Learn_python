# map 遍歷列表中的元素帶入函數做處理

def fn(x):
    return x * 2

a = [1,2,3]
c = list(map(fn, a))
print(c)

d = map((lambda x: x *2), a)
print(d)
'''
k = list(range(0,100)) #產生由0開始 共10個
j = list(map(fn, k))
print(j)
'''
