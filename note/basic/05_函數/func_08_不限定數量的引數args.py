# def test_args(*args):
#     s = 0
#     for arg in args:
#         s += arg
#     return s



def test_args(*args):
    for i, argv in enumerate(args):
        print(i, argv)



def test1():
    # print(test_args(1,2,3,4,5))
    print(test_args('a', 'b', 'c'))

if __name__ == '__main__':
    test1()