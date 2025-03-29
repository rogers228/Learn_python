#alist=[]
alist=[11,22,33,'bons_t',55,11,22,33,'bons_t',55,11,22,33,'bons_f',55]
print('len: %d' % len(alist))
print('count: %d' % alist.count('bons_f'))
print('bons_f' in alist)

if 0 == 0:
    print('True')
if True:
    print('True')

if True and 0 or 0:
    print('True')


if ('bons_f' in alist) or (len(alist) == 0):
    print('a_go')
else:
    print('a_stop')

for index in range(len(alist)):
    if alist[index] == 'bons_f':
        print(int(index/5)+1)
        break

blist=[11,22,33,44,55,66,77,211,222,233,244,255,266,277]
print(blist)
print(blist[0:1*7])
print(blist[2*7-7:])

