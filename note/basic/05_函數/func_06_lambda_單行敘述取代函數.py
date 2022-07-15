#lambda 只有一行的function 指令程式碼
#lambda param1, param2, ... : expression
#lambda 參數1, 參數2, …: 回傳值(運算式A) if 關係運算式 else 運算式B
#Lambda函式的程式碼只能有一行

#範例1
#原func
def func_1(x,y,z):
    return x + y + z
print(func_1(3,10,6))

#使用lambda
func_2 = lambda x,y,z: x+y+z
print(func_2(3,10,6))
print('----------')

#範例2 包含if
#原func
def _max(a, b):
    if a >= b:
        return a
    else:
        return b
print(_max(9,15))

l_max = lambda a, b: a if a >= b else b
print(l_max(9,15))


#範例3 當成iif使用
def func_n(x):
    if x:
        return x + 2
    else:
        return 'is null'
a = None
a = ''
print(func_n(a))
l_func_n = lambda a: a if a else 'is null'
print(l_func_n(a))
    

