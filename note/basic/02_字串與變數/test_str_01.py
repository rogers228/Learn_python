#字串與變數的使用


a=5
b='Rogers'
print(a) #列印變數

'''
將文字與變數連接
變數為數字時要使用str()函數，轉換為文字才能連接
'''
print('it is ' + str(a)) #符號+ 等於連接
print('it is' , str(a)) #符號, 等於連接，會自動補空白
print('my name is ' + b)
print('my name is',b)


'''
將文字中直接包含變數
%s 代表文字類型的變數
%d 代表數字類型的變數
'''
cn='Tony'
dn='Curry'
print('my name is %s' %cn)
print('my name is %s and your name is %s' %(cn,dn) )
print('my name is %s and i\'m %d years old' %(cn,a))
print('my name is %s' %cn + ' and i\'m %d years old' %a)

print('''12315615615616
1561611891
48948489489''')


