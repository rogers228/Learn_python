s = '5,R,6,A,9,11'
l = s.split(',')
for i in range(0,len(l), 2):
    print('{0},{1}'.format(l[i],l[i+1]))
