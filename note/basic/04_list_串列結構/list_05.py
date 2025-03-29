#nlist=['5A090600001', 1, 2, 3, 4, 5, 6]
nlist=[]
print(nlist)

#nlist.insert(1,['a','b','c']) #插在哪裡前面
nlist.insert(len(nlist),['a','b','c']) #插在哪裡前面
print(nlist)

'''
a=[]
a.extend(['1','2','3'])
print(a)
'''

mlis = [[],[],[]]
tmp = [['a','b','c']]
mlis[1].append(tmp)
print(mlis)

tmp = ['x','y','z']
mlis[1].append(tmp)
print(mlis)
