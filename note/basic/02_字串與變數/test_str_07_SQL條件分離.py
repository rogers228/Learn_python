whr = ''
a = '35'
b = 89
if a:
    whr += 'ma001 = {} AND '.format(a)
if b:
    whr += 'ma001 = {} AND '.format(b)
if whr:
    whr = ' WHERE ' + (whr[0:len(whr)-5])    
odr = ''
SQL = 'SELECT ma001, ma002, ma003, ma004 FROM rec_ma{}{}'.format(whr, odr)
print(SQL)
