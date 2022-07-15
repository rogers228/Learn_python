# 字串引用函數

class Myfuncs():
    def func1(self, a, b):
        return (a + b)

    def func2(self, a, b):
        return (a + b) *3.14

    def func3(self, a, b, c):
        return (a + b) * c


def tes1():
    ms = Myfuncs()
    dic_args ={'func': 'func2', 'a':2, 'b':5}
    ss = 'ms.{0}({1},{2})'.format(dic_args['func'], dic_args['a'], dic_args['b'])
    print(ss)
    ans = eval(ss)
    print('ans:', ans)
