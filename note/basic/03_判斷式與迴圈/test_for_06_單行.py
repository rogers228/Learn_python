# 標準for
alis = []
for i in range(1,11):
    alis.append(i)
print(alis) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 單行for
blis = [i for i in range(1,11)]
print(blis) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 有條件複製
clis = [item for item in blis if item < 5] #使用單行for  及單行if
print(clis)