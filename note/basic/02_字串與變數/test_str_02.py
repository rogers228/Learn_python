a = 'test'
b = 52
print(a)
print(b)
print(a+str(b))


pd = '6AA03AA001B31B01'
pd = pd.ljust(40) #空格補滿字元，文字靠左
print(pd)

pd = '6AA03AA001B31B01'
pd = pd.rjust(40) #空格補滿字元，文字靠右
print(pd)

pd = '  6AA0  3AA001B31  B01  '
pd = pd.replace(' ','') #f去除空白
print(pd)
