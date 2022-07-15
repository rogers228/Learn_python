# 函數內引用函數
# 優點不需要引用模組
# 缺點是函數冗長  可使用IDE折疊

def tes1():
    def func1(a, b):
        return (a + b)

    def func2(a, b):
        return (a + b) *3.14

    def func3(a, b, c):
        return (a + b) * c

    dic_args ={'func': 'func1', 'a':2, 'b':5}
    ss = '{0}({1},{2})'.format(dic_args['func'], dic_args['a'], dic_args['b'])
    print(ss)
    ans = eval(ss)
    print('ans:', ans)

if __name__ == '__main__':
    tes1()