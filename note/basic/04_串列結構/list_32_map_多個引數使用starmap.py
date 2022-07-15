def mfd(a, b):
    return a*b

def test74():
    from itertools import starmap
    lis_a = [1,2,3,4,5]
    lis_b = [6,5,2,2,2]
    lic_ab = list(starmap(mfd, zip(lis_a, lis_b)))
    print(lic_ab)
    # [6, 10, 6, 8, 10]