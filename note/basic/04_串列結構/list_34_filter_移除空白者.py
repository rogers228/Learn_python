def test1():
    lis = ['PPV1-', 'PPV2-', 'PPV3-', 'PPV4-', 'PPV5-' , '']
    lis = list(filter(None, lis))
    print(lis)

if __name__ == '__main__':
    test1()