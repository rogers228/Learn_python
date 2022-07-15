print('===字串與變數的使用===')
a=5
b='Rogers'
print('my name is %s and i\'m %d years old' %(b, a))

temp = 'my name is %s and i\'m %d years old'
print(temp %(b, a))

lis=['Tony',25]
print(temp %(lis[0], lis[1]))

