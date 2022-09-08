import array

def test1():
    lis =[11, 22, 33, 44, 55, 66, 77, 3,2,1,3,3]
    arr = array.array('i', lis)
    print(arr)

    if 3 in arr:
        arr.remove(3) # only remove one

    print(arr)

def test2():
    lis =[11, 22, 33, 44, 55, 66, 77, 3,2,1,3,3]
    arr = array.array('i', lis)
    print(arr)

    while 3 in arr:  # remove all
        arr.remove(3)

    print(arr)

if __name__ == '__main__':
    test2()