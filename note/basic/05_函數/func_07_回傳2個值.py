#回傳2個值

def func(x):
    a = x
    b = x + 1
    return a, b

x = 45
r, s = func(x)
print('r:{}, s:{}'.format(r, s))
