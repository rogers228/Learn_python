def test_args(*args):
    s = 0
    for arg in args:
        s += arg
    return s

def test41():
    print(test_args(1,2,3,4,5))