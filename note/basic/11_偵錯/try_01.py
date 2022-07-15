a=22
b=33
try:
    if a<b:
        print(n) #錯誤
except:
    #錯誤執行
    print('except')
print('after ..')


#-----------------------
a=22
b=33
try:
    if a<b:
        print(a) #錯誤
except:
    #錯誤執行
    print('except')
else:
    #沒有錯誤時
    print('else')

print('after ..')







#-----------------------

print('-----------------------')
a=22
b=33
try:
    # raise NameError #直接引發錯誤
    if a<b:
        print(a) #錯誤
except:
    #錯誤時執行
    print('except')
else:
    #沒有錯誤時
    print('else')
finally:
    #不管有沒有錯誤都執行
    print('finally')

print('after ..')
