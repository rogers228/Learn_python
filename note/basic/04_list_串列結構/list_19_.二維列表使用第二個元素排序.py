#二維列表 使用第二個元素排序

lis=[['ford',2000,5],['bmw',1999,8],['hyundai',1988,3],['ford_B',2000,4]]
print(lis)


lis.sort(key = lambda x: (x[1], -x[2])) #使用多個元素進行排序 - 代表倒轉
print(lis)
