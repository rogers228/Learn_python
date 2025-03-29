mlis = ['a','b','c','d','e','f','g','h']
print(mlis)

'''
mlis[2] = 'ready_del'
print(mlis)
'''

delis = [5,6] #要刪除的索引直

for d in range(len(delis)):
    mlis[delis[d]] = 'ready_del'
print(mlis)

tmplis = []
for m in range(len(mlis)):
    if mlis[m] != 'ready_del':
        tmplis.append(mlis[m])

print(delis)
mlis = tmplis
print(mlis)
