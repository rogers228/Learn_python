#�G���C�� �ϥβĤG�Ӥ����Ƨ�

lis=[['ford',2000,5],['bmw',1999,8],['hyundai',1988,3],['ford_B',2000,4]]
print(lis)


lis.sort(key = lambda x: (x[1], -x[2])) #�ϥΦh�Ӥ����i��Ƨ� - �N�����
print(lis)
