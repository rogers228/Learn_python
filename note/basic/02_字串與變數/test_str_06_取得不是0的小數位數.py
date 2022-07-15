def gerDum(dum):
    #返還不是0的小數位數  最大取小數6位
    sn = '{:.6f}'.format(dum - int(dum))
    sn = '{:0>6f}'.format(float(sn))
    i = 6 + 1 #由小數點後第六位開始，前兩位為0.
    while True: 
        if sn[i:i+1] == '0':
            i = i -1
        else:
            break
    return i - 1

d = 3.141592654
d = 1.03
print('原{}, 返回{}'.format(d, gerDum(d)))
