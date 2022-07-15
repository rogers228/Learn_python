text = '123,456,78,9'
textList = text.split(',')
print(textList)

#有些文字陣列包含,逗號  可以採用多個符號來分隔
a = 'fsdafda__%__bf,bbb,d nn__%__eeeee,eee__%__4fdf'
aList =a.split('__%__')
print(aList)
print(aList[0])
print(aList[1])
print(aList[2])
print(aList[3])

'''
a = 'text:abc'
aList =a.split(':')
print(aList)
print(aList[0])
print(a.split(':')[0])

da = '2005-10-03 00:00:00'
dalist = da.split('-')
print(dalist)
print(dalist[0]+'/'+dalist[1]+'/'+dalist[2][:2]) #取年月日

'''
