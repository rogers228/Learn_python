def test1():
    i = 2
    if i == 0:
        print('z')
    elif i == 1:
        print('one')
    elif i == 2:
        print('two')
    elif i == 3:
        print('three')
    else:
        print('else')

def test2():
    # python select case
    i = 3
    dic_case = {
        0: 'z',
        1: 'one',
        2: 'two',
        3: 'three'}
    print(dic_case.get(i, 'else'))

if __name__ == '__main__':
    test2()